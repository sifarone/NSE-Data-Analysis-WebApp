import motor.motor_asyncio
from dateutil import parser

from . import config
from . import csvUtils
from . import cashUtils as utils

class LoadBhavDataFromCsvToDB:
    def __init__(self, file):
        self.dbClient   = motor.motor_asyncio.AsyncIOMotorClient(config.DB_HOST, config.DB_PORT)
        self.db         = self.dbClient[config.DATABASE]
        self.collection = self.db[config.COLLECTION]
        self.csvData    = csvUtils.ReadStockBhavDataCSV(file)
        self.columns    = self.csvData.getCSVColumnList()

    async def loadDataWithoutCheck(self):
        entryCount = 0
        updateCount = 0
        skippedCount = 0

        data = self.csvData.getStockFlatData()
        for row in data:
            bhavData = {
                'date'            : parser.parse(str(row['date']).strip()), # as a gatetime.date() object
                'prevClose'       : float(row['prevClose'] if (utils.is_number(row['prevClose'])) else '0.0'),
                'openPrice'       : float(row['openPrice'] if (utils.is_number(row['openPrice'])) else '0.0'),
                'highPrice'       : float(row['highPrice'] if (utils.is_number(row['highPrice'])) else '0.0'),
                'lowPrice'        : float(row['lowPrice'] if (utils.is_number(row['lowPrice'])) else '0.0'),
                'lastPrice'       : float(row['lastPrice'] if (utils.is_number(row['lastPrice'])) else '0.0'),
                'closePrice'      : float(row['closePrice'] if (utils.is_number(row['closePrice'])) else '0.0'),
                'avgPrice'        : float(row['avgPrice'] if (utils.is_number(row['avgPrice'])) else '0.0'),
                'ttlTrdQtnty'     : int(row['ttlTrdQtnty'] if (utils.is_number(row['ttlTrdQtnty'])) else '0'),
                'turnoverLacs'    : float(row['turnoverLacs'] if (utils.is_number(row['turnoverLacs'])) else '0.0'),
                'noOfTrades'      : int(row['noOfTrades'] if (utils.is_number(row['noOfTrades'])) else '0'),
                'delivQty'        : int(row['delivQty'] if (utils.is_number(row['delivQty'])) else '0'),
                'delivPer'        : float(row['delivPer'] if (utils.is_number(row['delivPer'])) else '0.0')
            }

            try:
                document = await self.collection.find_one({'symbol': str(row['symbol']).strip()})
                if document:
                    result = await self.collection.update_one({'symbol': str(row['symbol']).strip()},
                                                              {'$push': {'bhavData': bhavData}})
                    updateCount += 1
                else:
                    result = await self.collection.insert_one( { 'symbol' : str(row['symbol']), 'bhavData' : [bhavData] } )
                    entryCount += 1

            except Exception as e:
                print('loadDataWithoutCheck () - ERROR : ', e)

        return entryCount, updateCount, skippedCount

    async def loadDataWithCheck(self):
        entryCount = 0
        updateCount = 0
        skippedCount = 0

        data = self.csvData.getStockFlatData()
        for row in data:
            bhavData = {
                'date'          : parser.parse(str(row['date']).strip()),  # as a gatetime.date() object
                'prevClose'     : float(row['prevClose'] if (utils.is_number(row['prevClose'])) else '0.0'),
                'openPrice'     : float(row['openPrice'] if (utils.is_number(row['openPrice'])) else '0.0'),
                'highPrice'     : float(row['highPrice'] if (utils.is_number(row['highPrice'])) else '0.0'),
                'lowPrice'      : float(row['lowPrice'] if (utils.is_number(row['lowPrice'])) else '0.0'),
                'lastPrice'     : float(row['lastPrice'] if (utils.is_number(row['lastPrice'])) else '0.0'),
                'closePrice'    : float(row['closePrice'] if (utils.is_number(row['closePrice'])) else '0.0'),
                'avgPrice'      : float(row['avgPrice'] if (utils.is_number(row['avgPrice'])) else '0.0'),
                'ttlTrdQtnty'   : int(row['ttlTrdQtnty'] if (utils.is_number(row['ttlTrdQtnty'])) else '0'),
                'turnoverLacs'  : float(row['turnoverLacs'] if (utils.is_number(row['turnoverLacs'])) else '0.0'),
                'noOfTrades'    : int(row['noOfTrades'] if (utils.is_number(row['noOfTrades'])) else '0'),
                'delivQty'      : int(row['delivQty'] if (utils.is_number(row['delivQty'])) else '0'),
                'delivPer'      : float(row['delivPer'] if (utils.is_number(row['delivPer'])) else '0.0')
            }

            try:
                dateList = []
                document = await self.collection.find_one({'symbol': str(row['symbol']).strip()})
                if document:
                    for items in document['bhavData']:
                        dateList.append(items['date'])

                    if bhavData['date'] in dateList:
                        # Data for this date is already present in Database
                        skippedCount += 1
                    else:
                        result = await self.collection.update_one({'symbol': str(row['symbol']).strip()},
                                                              {'$push': {'bhavData': bhavData}})
                        updateCount += 1
                else:
                    result = await self.collection.insert_one({'symbol': str(row['symbol']), 'bhavData': [bhavData]})
                    entryCount += 1

            except Exception as e:
                print('loadDataWithoutCheck () - ERROR : ', e)

        return entryCount, updateCount, skippedCount

class LoadArchivedBhavDataFromCsvToDB:
    def __init__(self, file):
        self.dbClient = motor.motor_asyncio.AsyncIOMotorClient(config.DB_HOST, config.DB_PORT)
        self.db = self.dbClient[config.DATABASE]
        self.collection = self.db[config.COLLECTION]
        self.csvData = csvUtils.ReadArchivedStockBhavDataCSV(file)
        self.columns = self.csvData.getCSVColumnList()

    async def loadDataWithoutCheck(self):
        entryCount = 0
        updateCount = 0
        skippedCount = 0

        data = self.csvData.getStockFlatData()
        for row in data:
            bhavData = {
                'date'          : parser.parse(str(row['date']).strip()),  # as a gatetime.date() object
                'prevClose'     : float(row['prevClose'] if (utils.is_number(row['prevClose'])) else '0.0'),
                'openPrice'     : float(row['openPrice'] if (utils.is_number(row['openPrice'])) else '0.0'),
                'highPrice'     : float(row['highPrice'] if (utils.is_number(row['highPrice'])) else '0.0'),
                'lowPrice'      : float(row['lowPrice'] if (utils.is_number(row['lowPrice'])) else '0.0'),
                'lastPrice'     : float(row['lastPrice'] if (utils.is_number(row['lastPrice'])) else '0.0'),
                'closePrice'    : float(row['closePrice'] if (utils.is_number(row['closePrice'])) else '0.0'),
                'avgPrice'      : float('0.0'),
                'ttlTrdQtnty'   : int('0'),
                'turnoverLacs'  : float('0.0'),
                'noOfTrades'    : int('0'),
                'delivQty'      : int('0'),
                'delivPer'      : float('0.0')
            }

            try:
                document = await self.collection.find_one({'symbol': str(row['symbol']).strip()})
                if document:
                    result = await self.collection.update_one({'symbol': str(row['symbol']).strip()},
                                                              {'$push': {'bhavData': bhavData}})
                    updateCount += 1
                else:
                    result = await self.collection.insert_one(
                        {'symbol': str(row['symbol']), 'bhavData': [bhavData]})
                    entryCount += 1

            except Exception as e:
                print('loadDataWithoutCheck () - ERROR : ', e)

        return entryCount, updateCount, skippedCount

    async def loadDataWithCheck(self):
        entryCount = 0
        updateCount = 0
        skippedCount = 0

        data = self.csvData.getStockFlatData()
        for row in data:
            bhavData = {
                'date'          : parser.parse(str(row['date']).strip()),  # as a gatetime.date() object
                'prevClose'     : float(row['prevClose'] if (utils.is_number(row['prevClose'])) else '0.0'),
                'openPrice'     : float(row['openPrice'] if (utils.is_number(row['openPrice'])) else '0.0'),
                'highPrice'     : float(row['highPrice'] if (utils.is_number(row['highPrice'])) else '0.0'),
                'lowPrice'      : float(row['lowPrice'] if (utils.is_number(row['lowPrice'])) else '0.0'),
                'lastPrice'     : float(row['lastPrice'] if (utils.is_number(row['lastPrice'])) else '0.0'),
                'closePrice'    : float(row['closePrice'] if (utils.is_number(row['closePrice'])) else '0.0'),
                'avgPrice'      : float('0.0'),
                'ttlTrdQtnty'   : int('0'),
                'turnoverLacs'  : float('0.0'),
                'noOfTrades'    : int('0'),
                'delivQty'      : int('0'),
                'delivPer'      : float('0.0')
            }

            try:
                dateList = []
                document = await self.collection.find_one({'symbol': str(row['symbol']).strip()})
                if document:
                    for items in document['bhavData']:
                        dateList.append(items['date'])

                    if bhavData['date'] in dateList:
                        # Data for this date is already present in Database
                        skippedCount += 1
                    else:
                        result = await self.collection.update_one({'symbol': str(row['symbol']).strip()},
                                                                  {'$push': {'bhavData': bhavData}})
                        updateCount += 1
                else:
                    result = await self.collection.insert_one(
                        {'symbol': str(row['symbol']), 'bhavData': [bhavData]})
                    entryCount += 1

            except Exception as e:
                print('loadDataWithoutCheck () - ERROR : ', e)

        return entryCount, updateCount, skippedCount


