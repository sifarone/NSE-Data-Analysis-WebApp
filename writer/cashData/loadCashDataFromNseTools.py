import motor.motor_asyncio
from nsetools import Nse
from dateutil import parser

from . import config
from . import cashUtils as utils

'''
TO BE RUN only after Market close i.e. after 4:00 PM 
'''
class LoadCashDataFromNseTools:
    def __init__(self):
        self.nseClient  = Nse()
        self.dbClient   = motor.motor_asyncio.AsyncIOMotorClient(config.DB_HOST, config.DB_PORT)
        self.db         = self.dbClient[config.DATABASE]
        self.collection = self.db[config.TEMP_COLLECTION] # <- TBD

    async def loadBhavdataToDB(self):
        entryCount = 0
        updateCount = 0
        skippedCount = 0

        try:
            stockCodes = self.nseClient.get_stock_codes()
            sList = list(stockCodes.keys())

            stockList = []
            for stock in sList:
                stockList.append(stock)

            for stock in stockList[1:]:
                stockData = self.nseClient.get_quote(stock)

                # Convert to bhavData format
                bhavData = {
                    'date': parser.parse(str(stockData['secDate']).strip()),  # as a gatetime.date() object
                    'prevClose': float(stockData['previousClose'] if (utils.is_number(stockData['previousClose'])) else '0.0'),
                    'openPrice': float(stockData['open'] if (utils.is_number(stockData['open'])) else '0.0'),
                    'highPrice': float(stockData['dayHigh'] if (utils.is_number(stockData['dayHigh'])) else '0.0'),
                    'lowPrice': float(stockData['dayLow'] if (utils.is_number(stockData['dayLow'])) else '0.0'),
                    'lastPrice': float(stockData['lastPrice'] if (utils.is_number(stockData['lastPrice'])) else '0.0'),
                    'closePrice': float(stockData['closePrice'] if (utils.is_number(stockData['closePrice'])) else '0.0'),
                    'avgPrice': float(stockData['averagePrice'] if (utils.is_number(stockData['averagePrice'])) else '0.0'),
                    'ttlTrdQtnty': int(stockData['quantityTraded'] if (utils.is_number(stockData['quantityTraded'])) else '0'),
                    'turnoverLacs': float(stockData['totalTradedValue'] if (utils.is_number(stockData['totalTradedValue'])) else '0.0'), # TBD
                    #'noOfTrades': int(stockData['noOfTrades'] if (utils.is_number(stockData['noOfTrades'])) else '0'),
                    'noOfTrades': int('0'),
                    'delivQty': int(stockData['deliveryQuantity'] if (utils.is_number(stockData['deliveryQuantity'])) else '0'),
                    'delivPer': float(stockData['deliveryToTradedQuantity'] if (utils.is_number(stockData['deliveryToTradedQuantity'])) else '0.0')
                }

                dateList = []
                document = await self.collection.find_one({'symbol': str(stockData['symbol']).strip()})
                if document:
                    for items in document['bhavData']:
                        dateList.append(items['date'])

                    if bhavData['date'] in dateList:
                        # Data for this date is already present in Database
                        skippedCount += 1
                    else:
                        result = await self.collection.update_one({'symbol': str(stockData['symbol']).strip()},
                                                                  {'$push': {'bhavData': bhavData}})
                        updateCount += 1
                else:
                    result = await self.collection.insert_one({'symbol': str(stockData['symbol']), 'bhavData': [bhavData]})
                    entryCount += 1

        except Exception as e:
            print('loadBhavdataToDB () - ERROR : ', e)

        return entryCount, updateCount, skippedCount


