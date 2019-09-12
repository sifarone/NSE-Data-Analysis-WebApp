import motor.motor_asyncio

from . import config
from . import responses
from . import stkOptDataWrapper
from . import fnoUtils as utils

class StkOptDbAPIs:
    def __init__(self):
        self.dbClient = motor.motor_asyncio.AsyncIOMotorClient(config.DB_HOST, config.DB_PORT)
        self.db = self.dbClient[config.DATABASE]
        self.collection = self.db[config.STKOPT_COLLECTION]

    async def getFnOSymbolList(self):
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
            return responses.errorMessage('Symbol List Error!!')

    async def getStkOptDailyData(self, symbol, expiryDate, strikePrice, optionType):
        '''
        Returns all the fno dailyData for a stock.
        expiryDate: Type is datetime.date()
        Ideallly only one such record should be present in Database. which will have a list of multiple dailyData according to date.
            Input parameters: <symbol, expiryDate, strikePrice, optionType>
            Output: Daily Data in ofthe following format sorted wrt dates.
                    {
                    date : [date1-string | date2-string | date3-string | ...], Ascending order ->
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
                dailyData = stkOptDataWrapper.StkOptDataWrapper(document)
                return dailyData.getDailyData()
            else:
                return responses.errorMessage('getStkOptDailyData() : Data Not Found!!')

        except Exception as e:
            print(e)
            return responses.errorMessage('getStkOptDailyData() : Fatal Error')


    async def getStkOptStrikePriceData(self, symbol, expiryDate, strikePrice):
        '''
         expiryDate: Type is datetime.date()
         Input parameters: <symbol, expiryDate, strikePrice>
         Output:  Data in the following format, with keys as Option Types.
                 {
                     CE : {  'date': ["2019-6-3", "2019-6-4", "2019-6-6", "2019-6-7", "2019-6-10",.......)],
                             'open': [54.0, 0.0, 48.0, 41.15, 49.3, 45.0, 0.0, 42.0, 0.0, 42.6, 38.1, 44.1, 37.85],
                             'low': [51.9, 0.0, 40.95, 38.55, 44.0, 45.0, 0.0, 42.0, 0.0, 40.95, 35.1, 37.55, 37.85],
                             'close': [56.95, 56.95, 40.95, 43.05, 44.0, 45.25, 45.25, 42.0, 42.0, 40.95, 40.65, 39.9, 41.0],
                             'settlePrice': [56.95, 54.3, 40.95, 43.05, 44.0, 45.25, 45.25, 42.0, 44.7, 40.95, 40.65, 39.9, 41.0],
                             'contracts': [7, 0, 13, 10, 2, 2, 0, 1, 0, 8, 10, 5, 5],
                             'valueInLakhs': [74.22, 0.0, 134.63, 102.22, 20.79, 20.7, 0.0, 10.26, 0.0, 81.98, 102.05, 51.09, 51.06],
                             'openInterest': [138000, 138000, 135000, 123000, 126000, 126000, 126000, 126000, 126000, 120000, 108000, 99000, 93000],
                             'changeInOpenInterest': [-9000, 0, -3000, -12000, 3000, 0, 0, 0, 0, -6000, -12000, -9000, -6000]
                         }
                     PE : Put Option DailyData Wrapper Object like above
                 }
         '''
        returnData = {}
        returnData.update({
            'CE': await self.getStkOptDailyData(symbol, expiryDate, strikePrice, 'CE'),
            'PE': await self.getStkOptDailyData(symbol, expiryDate, strikePrice, 'PE')
        })
        return returnData

    async def getStkOptExpiryDateData(self, symbol, expiryDate):
        '''
                expiryDate: Type is datetime.date()
                Input parameters: <symbol, expiryDate>
                Output:  Data in the following format, with keys as Strike Prices.
                        {
                            strikePrice1: {
                                            CE : Call Option DailyData Wraper Object
                                            PE : Put Option DailyData Wrapper Object
                                        },
                            strikePrice2: {
                                            CE : Call Option DailyData Wraper Object
                                            PE : Put Option DailyData Wrapper Object
                                        },
                                        .
                                        .
                                        .
                        }
        '''
        returnData = {}
        strikePrices = set()
        #print('getStkOptExpiryDateData --> ExpiryDate : ', expiryDate)

        try:
            async for document in self.collection.find({'symbol': symbol,
                                                        'expiryDate': expiryDate}):
                strikePrices.add(document['strikePrice'])

            if strikePrices:
                for strikePrice in sorted(strikePrices):
                    returnData.update({
                        strikePrice: await self.getStkOptStrikePriceData(symbol, expiryDate, strikePrice)
                    })
                #print('getStkOptExpiryDateData() : Requested Data Found.')
                return sorted(list(strikePrices)), returnData
            else:
                print('getStkOptExpiryDateData() : Requested Data NOT Found.')
                return sorted(list(strikePrices)), returnData # {}, {} in case of else

        except Exception as e:
            print('getStkOptExpiryDateData() : Fatal Error : ',e)
            return sorted(list(strikePrices)), returnData # {}, {} in case of exception

    async def getStkOptData(self, symbol):
        '''
        Input parameters: <symbol>
        Output:  Data in the following format, with keys as Expiry Dates.
                {
                    ExpiryDate1: {
                                    strikePrice1: {
                                                    CE : Call Option DailyData Wraper Object
                                                    PE : Put Option DailyData Wrapper Object
                                                },
                                    strikePrice2: {
                                                    CE : Call Option DailyData Wraper Object
                                                    PE : Put Option DailyData Wrapper Object
                                                },
                                            .
                                            .
                                            .
                                },
                    ExpiryDate2: {
                                    strikePrice1: {
                                                    CE : Call Option DailyData Wraper Object
                                                    PE : Put Option DailyData Wrapper Object
                                                },
                                    strikePrice2: {
                                                    CE : Call Option DailyData Wraper Object
                                                    PE : Put Option DailyData Wrapper Object
                                                },
                                            .
                                            .
                                            .
                                },
                                .
                                .
                                .
                }
        '''
        optionData = {}
        optionInfo = {}
        expiryDates = set()

        try:
            async for document in self.collection.find({'symbol': symbol}):
                expiryDates.add(document['expiryDate'])

            if expiryDates:
                for expiryDate in sorted(expiryDates):
                    strikePrices, data = await self.getStkOptExpiryDateData(symbol, expiryDate)
                    optionData.update({ utils.convertDateToString(expiryDate): data })
                    optionInfo.update({ utils.convertDateToString(expiryDate): strikePrices })
            else:
                print('getStkOptData () : Requested Data NOT Found.')

            return symbol, optionInfo, optionData # {}, {} in case of else

        except Exception as e:
            print('getStkOptData () : Fatal Error : ', e)
            return symbol, optionInfo, optionData # {}, {} in case of exception


    ### SPECIFIC DATA REQUEST functions For CHARTING MODULE ----------------------------------------------------------

    # This function will be used to construct the OPTION CHAIN
    async def getStkOptDataForADate(self, symbol, expiryDate, optionType, date):
        returnInfo = {}
        returnData = {}
        tempData = {}
        info, allSpData = await self.getStkOptExpiryDateData(symbol, expiryDate)
        if allSpData:
            spList = list(allSpData.keys())  # List of all strike prices on that date for a particular expiry

            for sp in spList:
                spDailyData = allSpData[sp][optionType]
                dateList = spDailyData['date']  # list of date strings
                indexOfDate = dateList.index(utils.convertDateToString(date))
                data = {}
                for field in utils.stkOptDailyDataFields.keys():
                    data.update({field: spDailyData[field][indexOfDate]})
                tempData.update({sp: data})
        else:
            print('getStrikePriceDetailsOnADate(): Requested Data NOT found.')

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

            for field in utils.stkOptDailyDataFields.keys():
                l = []
                for sp in spList:
                    l.append(tempData[sp][field])
                returnData.update({field: l})

        returnInfo.update({utils.convertDateToString(expiryDate): info})
        return symbol, returnInfo, returnData

    async def getStrikePricePutCallDetailsForADate(self, symbol, expiryDate, date):
        #print('------> date: ', date)

        returnData = {}
        tempCEData = {}
        tempPEData = {}
        info, allSpData = await self.getStkOptExpiryDateData(symbol, expiryDate)

        def isolateDataByDate(spDailyData, tempData):
            #print('getStrikePriceDetailsOnADate(): isolateDataByDate : ')
            dateList = spDailyData['date']  # list of date strings
            #print('isolateDataByDate(): dateList : ', dateList)
            #print('isolateDataByDate(): utils.convertDateToString(date) : ', utils.convertDateToString(date))
            indexOfDate = dateList.index(utils.convertDateToString(date))
            #print('getStrikePriceDetailsOnADate(): indexOfDate : ', indexOfDate)
            data = {}
            for field in utils.stkOptDailyDataFields.keys():
                data.update({field: spDailyData[field][indexOfDate]})
            tempData.update({sp: data})

        def reStructureData(tempData):
            rtData = {}
            spList = list(tempData.keys())
            rtData.update({'strikePrice': spList})

            for f in utils.stkOptDailyDataFields.keys():
                l = []
                for sp in spList:
                    l.append(tempData[sp][f])
                rtData.update({f: l})
            return rtData

        if allSpData:
            #print('getStrikePriceDetailsOnADate(): allSpData.')
            strikePriceList = list(allSpData.keys())  # List of all strike prices on that date for a particular expiry
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

    async def getFirstDateForAStrikePriceInAllExpiryMonth(self, symbol, strikePrice):
        '''

        :param symbol:
        :param expiryDate: exact expiryDate in datetime.date() format
        :return:
        '''

        '''
        optData = await self.getStkOptStrikePriceData(symbol, expiryDate, strikePrice)

        print('getFirstDateForAStrikePriceInAExpiryMonth() **** : ', optData)

        strDateList = optData['CE']['date']  # assuming CE and PE have equal frequency of data
        print('getFirstDateForAStrikePriceInAExpiryMonth() strDateList : ', strDateList)
        if strDateList:
            return strDateList[0]
            '''

        #################################################################################
        returnData = {}
        s, i, optData = await self.getStkOptData(symbol)
        #print('getFirstDateForAStrikePriceInAExpiryMonth() : optData : ', optData)
        for expDate in optData.keys():
            #print()
            #print('expDate  : ', expDate)
            #print('sp  : ', strikePrice)
            #print('spList  : ', optData[expDate].keys())
            if strikePrice in optData[expDate].keys():
                #print('expDate with strikePrice : ', expDate  )
                returnData.update({
                    expDate: optData[expDate][strikePrice]['CE']['date'][0]
                })
            #print('getFirstDateForAStrikePriceInAExpiryMonth() FDate : ', optData[expDate][strikePrice]['CE']['date'][0])
        return returnData

        #################################################################################

    async def getInfoForAllStkOptSymbols(self):

        returnData = {}
        try:
            symbolList = await self.getFnOSymbolList()
            for symbol in symbolList:
                #optionData = {}
                optionInfo = {}
                expiryDates = set()

                async for document in self.collection.find({'symbol': symbol}):
                    expiryDates.add(document['expiryDate'])

                if expiryDates:
                    for expiryDate in sorted(expiryDates):
                        strikePrices, data = await self.getStkOptExpiryDateData(symbol, expiryDate)
                        #optionData.update({ utils.convertDateToString(expiryDate): data })
                        optionInfo.update({ utils.convertDateToString(expiryDate): strikePrices })
                    returnData.update({symbol:optionInfo})
                else:
                    print('getInfoForAllStkOptSymbols () : Requested Data NOT Found.')

            return returnData

        except Exception as e:
            print('getInfoForAllStkOptSymbols () : Fatal Error : ', e)
            return returnData



