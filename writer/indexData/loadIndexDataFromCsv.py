import motor.motor_asyncio
from dateutil import parser
from datetime import datetime

from . import config
from . import csvUtils
from . import indexUtils as utils

dateFormatString = '%d-%m-%Y'

class LoadIndexDataFromCsv:
    def __init__(self, file):
        self.dbClient   = motor.motor_asyncio.AsyncIOMotorClient(config.DB_HOST, config.DB_PORT)
        self.db         = self.dbClient[config.DATABASE]
        self.collection = self.db[config.COLLECTION]
        self.csvData    = csvUtils.ReadConsolidatedIndicesCSV(file)
        self.columns    = self.csvData.getCSVColumnList()

    async def loadDataWithoutCheck(self):
        entryCount = 0
        updateCount = 0
        skippedCount = 0

        data = self.csvData.getConsolidatedIndicesFlatData()
        for row in data:
            dailyData = {
                #'date'              : parser.parse(str(row['date']).strip()), # as a gatetime.date() object
                'date'              : datetime.strptime(str(row['date']).strip(), dateFormatString),
                'openValue'         : float(row['openValue'] if (utils.is_number(row['openValue'])) else '0.0'),
                'highValue'         : float(row['highValue'] if (utils.is_number(row['highValue'])) else '0.0'),
                'lowValue'          : float(row['lowValue'] if (utils.is_number(row['lowValue'])) else '0.0'),
                'closingValue'      : float(row['closingValue'] if (utils.is_number(row['closingValue'])) else '0.0'),
                'pointsChange'      : float(row['pointsChange'] if (utils.is_number(row['pointsChange'])) else '0.0'),
                'percentChange'     : float(row['percentChange'] if (utils.is_number(row['percentChange'])) else '0.0'),
                'volume'            : int(row['volume'] if (utils.is_number(row['volume'])) else '0'),
                'turnover'          : float(row['turnover'] if (utils.is_number(row['turnover'])) else '0.0'),
                'peRatio'           : float(row['peRatio'] if (utils.is_number(row['peRatio'])) else '0.0'),
                'pbRatio'           : float(row['pbRatio'] if (utils.is_number(row['pbRatio'])) else '0.0'),
                'divYield'          : float(row['divYield'] if (utils.is_number(row['divYield'])) else '0.0')
            }


            try:
                document = await self.collection.find_one({'indexName': str(row['indexName']).strip().upper()})
                if document:
                    result = await self.collection.update_one({'indexName': str(row['indexName']).strip().upper()},
                                                              {'$push': {'dailyData': dailyData}})
                    updateCount += 1
                else:
                    result = await self.collection.insert_one( { 'indexName' : str(row['indexName']).strip().upper(), 'dailyData' : [dailyData] } )
                    entryCount += 1

            except Exception as e:
                print('Index loadDataWithoutCheck () - ERROR : ', e)

        return entryCount, updateCount, skippedCount

    async def loadDataWithCheck(self):
        entryCount = 0
        updateCount = 0
        skippedCount = 0

        data = self.csvData.getConsolidatedIndicesFlatData()
        for row in data:
            dailyData = {
                #'date'              : parser.parse(str(row['date']).strip()), # as a gatetime.date() object
                'date'              : datetime.strptime(str(row['date']).strip(), dateFormatString),
                'openValue'         : float(row['openValue'] if (utils.is_number(row['openValue'])) else '0.0'),
                'highValue'         : float(row['highValue'] if (utils.is_number(row['highValue'])) else '0.0'),
                'lowValue'          : float(row['lowValue'] if (utils.is_number(row['lowValue'])) else '0.0'),
                'closingValue'      : float(row['closingValue'] if (utils.is_number(row['closingValue'])) else '0.0'),
                'pointsChange'      : float(row['pointsChange'] if (utils.is_number(row['pointsChange'])) else '0.0'),
                'percentChange'     : float(row['percentChange'] if (utils.is_number(row['percentChange'])) else '0.0'),
                'volume'            : int(row['volume'] if (utils.is_number(row['volume'])) else '0'),
                'turnover'          : float(row['turnover'] if (utils.is_number(row['turnover'])) else '0.0'),
                'peRatio'           : float(row['peRatio'] if (utils.is_number(row['peRatio'])) else '0.0'),
                'pbRatio'           : float(row['pbRatio'] if (utils.is_number(row['pbRatio'])) else '0.0'),
                'divYield'          : float(row['divYield'] if (utils.is_number(row['divYield'])) else '0.0')
            }

            try:
                dateList = []
                document = await self.collection.find_one({'indexName': str(row['indexName']).strip().upper()})
                if document:
                    for items in document['dailyData']:
                        dateList.append(items['date'])

                    if dailyData['date'] in dateList:
                        # Data for this date is already present in Database
                        skippedCount += 1
                    else:
                        result = await self.collection.update_one({'indexName': str(row['indexName']).strip().upper()},
                                                              {'$push': {'dailyData': dailyData}})
                        updateCount += 1
                else:
                    result = await self.collection.insert_one({'indexName': str(row['indexName']).strip().upper(), 'dailyData': [dailyData]})
                    entryCount += 1

            except Exception as e:
                print('Index loadDataWithoutCheck () - ERROR : ', e)

        return entryCount, updateCount, skippedCount

#---------------------------------------------------------------------------------------------

class LoadArchivedIndexDataFromCsv:
    def __init__(self, file):
        self.dbClient = motor.motor_asyncio.AsyncIOMotorClient(config.DB_HOST, config.DB_PORT)
        self.db = self.dbClient[config.DATABASE]
        self.collection = self.db[config.COLLECTION]
        self.csvData = csvUtils.ReadArchivedIndexCSV(file)
        self.columns = self.csvData.getCSVColumnList()

    async def loadDataWithoutCheck(self):
        entryCount = 0
        updateCount = 0
        skippedCount = 0

        data = self.csvData.getArchivedIndicesFlatData()
        for row in data:
            dailyData = {
                #'date'          : parser.parse(str(row['date']).strip()),  # as a gatetime.date() object
                'date'          : datetime.strptime(str(row['date']).strip(), dateFormatString),
                'openValue'     : float(row['openValue'] if (utils.is_number(row['openValue'])) else '0.0'),
                'highValue'     : float(row['highValue'] if (utils.is_number(row['highValue'])) else '0.0'),
                'lowValue'      : float(row['lowValue'] if (utils.is_number(row['lowValue'])) else '0.0'),
                'closingValue'  : float(row['closingValue'] if (utils.is_number(row['closingValue'])) else '0.0'),
                'pointsChange'  : float('0.0'),
                'percentChange' : float('0.0'),
                'volume'        : int('0'),
                'turnover'      : float('0.0'),
                'peRatio'       : float(row['peRatio'] if (utils.is_number(row['peRatio'])) else '0.0'),
                'pbRatio'       : float(row['pbRatio'] if (utils.is_number(row['pbRatio'])) else '0.0'),
                'divYield'      : float(row['divYield'] if (utils.is_number(row['divYield'])) else '0.0')
            }

            try:
                document = await self.collection.find_one({'indexName': str(row['indexName']).strip().upper()})
                if document:
                    result = await self.collection.update_one({'indexName': str(row['indexName']).strip().upper()},
                                                              {'$push': {'dailyData': dailyData}})
                    updateCount += 1
                else:
                    result = await self.collection.insert_one({'indexName': str(row['indexName']).strip().upper(), 'dailyData': [dailyData]})
                    entryCount += 1

            except Exception as e:
                print('Archived Index loadDataWithoutCheck () - ERROR : ', e)

        return entryCount, updateCount, skippedCount

    async def loadDataWithCheck(self):
        entryCount = 0
        updateCount = 0
        skippedCount = 0

        data = self.csvData.getArchivedIndicesFlatData()
        for row in data:
            dailyData = {
                #'date'          : parser.parse(str(row['date']).strip()),  # as a gatetime.date() object
                'date'          : datetime.strptime(str(row['date']).strip(), dateFormatString),
                'openValue'     : float(row['openValue'] if (utils.is_number(row['openValue'])) else '0.0'),
                'highValue'     : float(row['highValue'] if (utils.is_number(row['highValue'])) else '0.0'),
                'lowValue'      : float(row['lowValue'] if (utils.is_number(row['lowValue'])) else '0.0'),
                'closingValue'  : float(row['closingValue'] if (utils.is_number(row['closingValue'])) else '0.0'),
                'pointsChange'  : float('0.0'),
                'percentChange' : float('0.0'),
                'volume'        : int('0'),
                'turnover'      : float('0.0'),
                'peRatio'       : float(row['peRatio'] if (utils.is_number(row['peRatio'])) else '0.0'),
                'pbRatio'       : float(row['pbRatio'] if (utils.is_number(row['pbRatio'])) else '0.0'),
                'divYield'      : float(row['divYield'] if (utils.is_number(row['divYield'])) else '0.0')
            }

            try:
                dateList = []
                document = await self.collection.find_one({'indexName': str(row['indexName']).strip().upper()})
                if document:
                    for items in document['dailyData']:
                        dateList.append(items['date'])

                    if dailyData['date'] in dateList:
                        # Data for this date is already present in Database
                        skippedCount += 1
                    else:
                        result = await self.collection.update_one({'indexName': str(row['indexName']).strip().upper()},
                                                                  {'$push': {'dailyData': dailyData}})
                        updateCount += 1
                else:
                    result = await self.collection.insert_one({'indexName': str(row['indexName']).strip().upper(), 'dailyData': [dailyData]})
                    entryCount += 1

            except Exception as e:
                print('Archived Index loadDataWithoutCheck () - ERROR : ', e)

        return entryCount, updateCount, skippedCount
