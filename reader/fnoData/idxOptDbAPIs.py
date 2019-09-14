import motor.motor_asyncio

from . import config
from . import responses
from . import idxOptDataWrapper
from . import fnoUtils as utils

class IdxOptDbAPIs:
    def __init__(self):
        self.dbClient   = motor.motor_asyncio.AsyncIOMotorClient(config.DB_HOST, config.DB_PORT)
        self.db         = self.dbClient[config.DATABASE]
        self.collection = self.db[config.IDXOPT_COLLECTION]

    async def getIdxOptSymbolList(self):
        '''
        Returns the list of symbols in fno market segment
        /api/{marketType}
        '''
        symbolSet = set()
        try:
            async for document in self.collection.find():
                symbolSet.add(document['symbol'])
            return sorted(list(symbolSet))

        except Exception as e:
            # Return an error message
            print(e)
            return responses.errorMessage('IdxOpt Symbol List Error!!')

    async def getIdxOptDailyData(self, symbol, expiryDate, strikePrice, optionType):
        '''
        Ideallly only one such record should be present in Database. which will have a list of multiple dailyData according to date.
        Input parameters: <symbol, expiryDate, strikePrice, optionType>
        Output: Daily Data in ofthe following format sorted wrt dates.
                {
                date : [date1 | date2 | date3 | ...], Ascending order ->
                open : [open1 | open2 | open3 | ...],
                .
                .
                .
                chnageInOpenInterest : [chnageInOpenInterest1 | chnageInOpenInterest2 | chnageInOpenInterest | .....]
            }

            * Due to mongoDB limitations on nested field sorting, this has to be done at application level
        '''
        try:
            document = await self.collection.find_one({'symbol': symbol,
                                                       'expiryDate': expiryDate,
                                                       'strikePrice': strikePrice,
                                                       'optionType': optionType})

            if document:
                dailyData = idxOptDataWrapper.IdxOptDataWrapper(document)
                return dailyData.getDailyData()
            else:
                return responses.errorMessage('getIdxOptDailyData() : Data Not Found!!')

        except Exception as e:
            print(e)
            return responses.errorMessage('getIdxOptDailyData() : Fatal Error')

    async def getIdxOptStrikePriceData(self, symbol, expiryDate, strikePrice):
        returnData = {}
        returnData.update({
            'CE': await self.getIdxOptDailyData(symbol, expiryDate, strikePrice, 'CE'),
            'PE': await self.getIdxOptDailyData(symbol, expiryDate, strikePrice, 'PE')
        })
        return returnData

    async def getIdxOptExpiryDateData(self, symbol, expiryDate):
        returnData = {}
        strikePrices = set()
        #print('==::', expiryDate)

        try:
            async for document in self.collection.find({'symbol': symbol,
                                                        'expiryDate': expiryDate}):
                strikePrices.add(document['strikePrice'])

            if strikePrices:
                for strikePrice in sorted(strikePrices):
                    returnData.update({
                        strikePrice: await self.getIdxOptStrikePriceData(symbol, expiryDate, strikePrice)
                    })
                return sorted(list(strikePrices)), returnData
            else:
                print('getIdxOptExpiryDateData() : Requested Data NOT Found.')
                return sorted(list(strikePrices)), returnData  # {}, {} in case of else

        except Exception as e:
            print('getIdxOptExpiryDateData() : Fatal Error : ', e)
            return sorted(list(strikePrices)), returnData  # {}, {} in case of exception

    async def getIdxOptData(self, symbol):
        optionData  = {}
        optionInfo  = {}
        expiryDates = set()

        try:
            async for document in self.collection.find({'symbol': symbol}):
                expiryDates.add(document['expiryDate'])

            if expiryDates:
                for expiryDate in sorted(expiryDates):
                    strikePrices, data = await self.getIdxOptExpiryDateData(symbol, expiryDate)
                    optionData.update({utils.convertDateToString(expiryDate): data})
                    optionInfo.update({utils.convertDateToString(expiryDate): strikePrices})
            else:
                print('getIdxOptData () : Requested Data NOT Found.')

            return symbol, optionInfo, optionData  # {}, {} in case of else

        except Exception as e:
            print('getStkOptData () : Fatal Error : ', e)
            return symbol, optionInfo, optionData  # {}, {} in case of exception

    ### SPECIFIC DATA REQUEST functions ------------------------------------------------------------------------

    # This function will be used to construct the OPTION CHAIN
    async def getIdxOptDataForADate(self, symbol, expiryDate, optionType, date):
        returnInfo  = {}
        returnData  = {}
        tempData    = {}
        # print('-->', expiryDate)
        info, allSpData = await self.getIdxOptExpiryDateData(symbol, expiryDate)
        if allSpData:
            spList = list(allSpData.keys())  # List of all strike prices on that date for a particular expiry

            for sp in spList:
                # print(sp)
                spDailyData = allSpData[sp][optionType]
                # print(spDailyData)
                dateList = spDailyData['date']  # list of date strings
                # print('Date List: ', dateList)
                indexOfDate = dateList.index(utils.convertDateToString(date))
                # print('date Index = ', indexOfDate)
                data = {}
                for field in utils.idxOptDailyDataFields.keys():
                    data.update({field: spDailyData[field][indexOfDate]})
                tempData.update({sp: data})
        else:
            print('getStrikePriceDetailsOnADate(): Requested Data NOT found.')

        # print(returnData)
        '''
        currently tempData is of the following form:
        {
            sp1: {
                'date'                         : d1-string,    <---  date is same
                'stkOptOpenPrice'              : op1,
                'stkOptHighPrice'              : hp1,      
                'stkOptLowPrice'               : lp1,     
                'stkOptClosePrice'             : cp1,      
                'stkOptSettlePrice'            : setPrice1,
                'stkOptContracts'              : c1, 
                'stkOptValueInLakhs'           : vil1, 
                'stkOptOpenInterest'           : OI1, 
                'stkOptChangeInOpenInterest'   : deltaOI1
            },

            sp2: {
                'date'                         : d1-string,  <--- date is same
                'stkOptOpenPrice'              : op2,
                'stkOptHighPrice'              : hp2,      
                'stkOptLowPrice'               : lp2,     
                'stkOptClosePrice'             : cp2,      
                'stkOptSettlePrice'            : setPrice2,
                'stkOptContracts'              : c2, 
                'stkOptValueInLakhs'           : vil2, 
                'stkOptOpenInterest'           : OI2, 
                'stkOptChangeInOpenInterest'   : deltaOI2
            },
            .
            .
            .
        }

        Convert the tempData above in the following form before returning:
        {
            strikePrice                 : [sp1 | sp2 | sp3 | .....],
            date                        : [d1 | d1 | d1 | ......],     <--- date is same (requested date)
            stkOptOpenPrice             : [op1 | op2 | op3 | .....],
            .
            .
            stkOptOpenInterest          : [OI1 | OI2 | OI3 | .....],
            stkOptChangeInOpenInterest  : [cOI1 | cOI2 | cOI3 | .....]

        }
        '''
        if tempData:
            spList = list(tempData.keys())
            returnData.update({'strikePrice': spList})

            for field in utils.idxOptDailyDataFields.keys():
                l = []
                for sp in spList:
                    l.append(tempData[sp][field])
                returnData.update({field: l})

        returnInfo.update({utils.convertDateToString(expiryDate): info})
        return symbol, returnInfo, returnData

    async def getFirstDateForAStrikePriceInAExpiryMonth(self, symbol, expiryDate, strikePrice):
        '''

        :param symbol:
        :param expiryDate: exact expiryDate in datetime.date() format
        :return:
        '''

        optData = await self.getIdxOptStrikePriceData(symbol, expiryDate, strikePrice)

        #print('getFirstDateForAStrikePriceInAExpiryMonth() **** : ', optData)

        strDateList = optData['CE']['date']  # assuming CE and PE have equal frequency of data
        #print('getFirstDateForAStrikePriceInAExpiryMonth() strDateList : ', strDateList)
        if strDateList:
            return strDateList[0]

        return ''

    async def getStrikePricePutCallDetailsForADate(self, symbol, expiryDate, date):

        returnData = {}
        tempCEData = {}
        tempPEData = {}
        info, allSpData = await self.getIdxOptExpiryDateData(symbol, expiryDate)

        def isolateDataByDate(spDailyData, tempData):
            # print(spDailyData)
            dateList = spDailyData['date']  # list of date strings
            # print('Date List: ', dateList)
            indexOfDate = dateList.index(utils.convertDateToString(date))
            # print('date Index = ', indexOfDate)
            data = {}
            for field in utils.idxOptDailyDataFields.keys():
                data.update({field: spDailyData[field][indexOfDate]})
            tempData.update({sp: data})

        def reStructureData(tempData):
            rtData = {}
            spList = list(tempData.keys())
            rtData.update({'strikePrice': spList})

            for f in utils.idxOptDailyDataFields.keys():
                l = []
                for sp in spList:
                    l.append(tempData[sp][f])
                rtData.update({f: l})
            return rtData

        if allSpData:
            strikePriceList = list(
                allSpData.keys())  # List of all strike prices on that date for a particular expiry
            # print('******: ',spList)
            for sp in strikePriceList:
                # print(sp)

                spDailyDataCE = allSpData[sp]['CE']
                spDailyDataPE = allSpData[sp]['PE']

                isolateDataByDate(spDailyDataCE, tempCEData)
                isolateDataByDate(spDailyDataPE, tempPEData)

        else:
            print('getStrikePriceDetailsOnADate(): Requested Data NOT found.')

        # print(returnData)
        '''
        currently tempData is of the following form:
        {
            sp1: {
                'date'                         : d1-string,    <---  date is same
                'stkOptOpenPrice'              : op1,
                'stkOptHighPrice'              : hp1,      
                'stkOptLowPrice'               : lp1,     
                'stkOptClosePrice'             : cp1,      
                'stkOptSettlePrice'            : setPrice1,
                'stkOptContracts'              : c1, 
                'stkOptValueInLakhs'           : vil1, 
                'stkOptOpenInterest'           : OI1, 
                'stkOptChangeInOpenInterest'   : deltaOI1
            },

            sp2: {
                'date'                         : d1-string,  <--- date is same
                'stkOptOpenPrice'              : op2,
                'stkOptHighPrice'              : hp2,      
                'stkOptLowPrice'               : lp2,     
                'stkOptClosePrice'             : cp2,      
                'stkOptSettlePrice'            : setPrice2,
                'stkOptContracts'              : c2, 
                'stkOptValueInLakhs'           : vil2, 
                'stkOptOpenInterest'           : OI2, 
                'stkOptChangeInOpenInterest'   : deltaOI2
            },
            .
            .
            .
        }

        Convert the tempData above in the following form before returning:
        {
            strikePrice                 : [sp1 | sp2 | sp3 | .....],
            date                        : [d1 | d1 | d1 | ......],     <--- date is same (requested date)
            stkOptOpenPrice             : [op1 | op2 | op3 | .....],
            .
            .
            stkOptOpenInterest          : [OI1 | OI2 | OI3 | .....],
            stkOptChangeInOpenInterest  : [cOI1 | cOI2 | cOI3 | .....]

        }
        '''
        '''
        if tempData:
            spList = list(tempData.keys())
            returnData.update({'strikePrice': spList})

            for field in utils.stkOptDailyDataFields.keys():
                l = []
                for sp in spList:
                    l.append(tempData[sp][field])
                returnData.update({field: l})
        '''
        if tempPEData and tempCEData:
            returnData.update({'PE': reStructureData(tempPEData)})
            returnData.update({'CE': reStructureData(tempCEData)})

        #print('getStrikePricePutCallDetailsForADate () : ', returnData)

        return returnData

    async def getInfoForAllIdxOptSymbols(self):

        returnData = {}
        try:
            symbolList = await self.getIdxOptSymbolList()
            for symbol in symbolList:
                # optionData = {}
                optionInfo  = {}
                expiryDates = set()

                async for document in self.collection.find({'symbol': symbol}):
                    expiryDates.add(document['expiryDate'])

                if expiryDates:
                    for expiryDate in sorted(expiryDates):
                        strikePrices, data = await self.getIdxOptExpiryDateData(symbol, expiryDate)
                        # optionData.update({ utils.convertDateToString(expiryDate): data })
                        optionInfo.update({utils.convertDateToString(expiryDate): strikePrices})
                    returnData.update({symbol: optionInfo})
                else:
                    print('getInfoForAllIdxOptSymbols () : Requested Data NOT Found.')

            return returnData

        except Exception as e:
            print('getInfoForAllIdxOptSymbols () : Fatal Error : ', e)
            return returnData
