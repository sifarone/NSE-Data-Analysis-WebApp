import datetime
import motor.motor_asyncio

from . import config
from . import responses
from . import cashUtils as utils
from . import cashDataWrapper

class CashDbAPIs:
    def __init__(self):
        self.dbClient = motor.motor_asyncio.AsyncIOMotorClient(config.DB_HOST, config.DB_PORT)
        self.db = self.dbClient[config.DATABASE]
        self.collection = self.db[config.COLLECTION]

    async def getCashSymbolList(self):
        symbolSet = set()
        try:
            async for document in self.collection.find():
                symbolSet.add(document['symbol'])
            return sorted(list(symbolSet))

        except Exception as e:
            # Return an error message
            return responses.errorMessage(e)

    async def getCashData(self, symbol, startDate, endDate=None):
        '''

        :param symbol:
        :param startDate: in string format
        :param endDate: in string format
        :return:
        '''
        #print('getCashData : symbol : ', symbol)
        #print('getCashData : startDate : ', startDate)
        try:
            # Async DB Lookup
            document = await self.collection.find_one({'symbol': symbol})

            # Wrap the Data
            cashData = cashDataWrapper.CashDataWrapper(document)

            if startDate:
                # Convert date types from string to a datetime.date object type
                stDate = utils.convertStringToDate(startDate)
                if not endDate:
                    edDate = datetime.datetime.now().date()
                else:
                    edDate = utils.convertStringToDate(endDate)

                # Return Data for the time interval requested
                #print('getCashData : stDate : ', stDate)
                #print('getCashData : edDate : ', edDate)
                data = cashData.getDataForAInterval(stDate, edDate)
                #print('getCashData : ', data)
                return data

            # Return all data
            return cashData.getData()

        except Exception as e:
            # Return an error message
            print(e)
            return responses.errorMessage('Wrong Inputs to the server!!')

