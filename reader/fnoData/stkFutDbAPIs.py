import motor.motor_asyncio

from . import config
from . import responses
from . import stkFutDataWrapper
from . import fnoUtils as utils

class StkFutDbAPIs:
    def __init__(self):
        self.dbClient = motor.motor_asyncio.AsyncIOMotorClient(config.DB_HOST, config.DB_PORT)
        self.db = self.dbClient[config.DATABASE]
        self.collection = self.db[config.STKFUT_COLLECTION]

    async def getStkFutSymbolList(self):
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
            return responses.errorMessage('StkFut Symbol List Error!!')

    async def getStkFutDailyData(self, symbol, expiryDate):
        '''
            Ideallly only one such record should be present in Database. which will have a list of multiple dailyData according to date.
            Input parameters: <symbol, expiryDate>
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
                                                       'expiryDate': expiryDate
                                                       })

            if document:
                dailyData = stkFutDataWrapper.StkFutDataWrapper(document)
                return dailyData.getDailyData()
            else:
                return responses.errorMessage('getStkOptDailyData() : Data Not Found!!')

        except Exception as e:
            print('getStkFutDailyData() : Data NOT Found : ', e)
            return responses.errorMessage('getStkFutDailyData() : Fatal Error')

    async def getStkFutData(self, symbol):
        '''
        Input parameters: <symbol, expiryDate>
        Output:  Data in the following format, with keys as Strike Prices.
                {
                    expiryDate1: {
                                    DailyData list
                                },
                    ExpiryDate2: {
                                    DailyData list
                                },
                                .
                                .
                                .
                }
        '''
        futureInfo = []
        futureData = {}
        expiryDates = set()

        try:
            async for document in self.collection.find({'symbol': symbol}):
                # print(document)
                expiryDates.add(document['expiryDate'])

            if expiryDates:
                for expiryDate in sorted(expiryDates):
                    data = await self.getStkFutDailyData(symbol, expiryDate)
                    futureData.update({ utils.convertDateToString(expiryDate): data })
                    futureInfo.append(utils.convertDateToString(expiryDate))
            else:
                return responses.errorMessage('getStkFutData () : Requested Data NOT Found.')

            return symbol, futureInfo, futureData # {}, {} in case of else

        except Exception as e:
            print('getStkFutData () : Fatal Error : ', e)
            return symbol, futureInfo, futureData  # {}, {} in case of exception

    ### SPECIFIC DATA REQUEST functions FOR CHARTING MODULE -----------------------------------------------------------

    async def getStkFutDataForAExpiryMonth(self, symbol, expiryDate):
        s, info, data = await self.getStkFutData(symbol)
        return data[utils.convertDateToString(expiryDate)]

    async def getInfoForAllStkFutSymbols(self):
        returnData = {}
        try:
            symbolList = await self.getStkFutSymbolList()
            for symbol in symbolList:

                s, info, data = await self.getStkFutData(symbol)
                returnData.update({symbol: info})

                '''
                async for document in self.collection.find({'symbol': symbol}):
                    expiryDates.add(document['expiryDate'])

                if expiryDates:
                    for expiryDate in sorted(expiryDates):
                        strikePrices, data = await self.getStkOptExpiryDateData(symbol, expiryDate)
                        # optionData.update({ utils.convertDateToString(expiryDate): data })
                        futureInfo.update({utils.convertDateToString(expiryDate): strikePrices})
                    returnData.update({symbol: futureInfo})
                else:
                    print('getInfoForAllStkFutSymbols () : Requested Data NOT Found.')
                '''

            return returnData

        except Exception as e:
            print('getInfoForAllStkFutSymbols () : Fatal Error : ', e)
            return returnData



