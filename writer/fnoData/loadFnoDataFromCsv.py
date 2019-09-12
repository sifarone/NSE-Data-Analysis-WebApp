import motor.motor_asyncio
from dateutil import parser

from . import config
from . import csvUtils
from . import fnoUtils as utils

class LoadFnoDataFromCsvToDB:
    def __init__(self, file):
        self.dbClient = motor.motor_asyncio.AsyncIOMotorClient(config.DB_HOST, config.DB_PORT)
        self.db = self.dbClient[config.DATABASE]
        self.stkOptCollection = self.db[config.STKOPT_COLLECTION]
        self.stkFutCollection = self.db[config.STKFUT_COLLECTION]
        self.idxOptCollection = self.db[config.IDXOPT_COLLECTION]
        self.idxFutCollection = self.db[config.IDXFUT_COLLECTION]

        self.fnoData = csvUtils.ReadFnOCSV(file)
        self.columns = self.fnoData.getCSVColumnList()

    # LOAD STOCK OPTIONS DATA --------------------------------------------------------------------
    async def loadStkOptDataWithoutCheck(self):
        entryCount = 0
        updateCount = 0
        skippedCount = 0

        optionsCSVData = self.fnoData.getOptStkFlatData()
        for rows in optionsCSVData:
            dailyData = {
                'date': parser.parse(str(rows['timeStamp']).strip()),
                'stkOptOpenPrice': float(rows['open'] if (utils.is_number(rows['open'])) else '0.0'),
                'stkOptHighPrice': float(rows['high'] if (utils.is_number(rows['high'])) else '0.0'),
                'stkOptLowPrice': float(rows['low'] if (utils.is_number(rows['low'])) else '0.0'),
                'stkOptClosePrice': float(rows['close'] if (utils.is_number(rows['close'])) else '0.0'),
                'stkOptSettlePrice': float(rows['settlePrice'] if (utils.is_number(rows['settlePrice'])) else '0.0'),
                'stkOptContracts': (rows['contracts'] if (utils.is_number(rows['contracts'])) else '0'),
                'stkOptValueInLakhs': float(rows['valueInLakhs'] if (utils.is_number(rows['valueInLakhs'])) else '0.0'),
                'stkOptOpenInterest': int(rows['openInterest'] if (utils.is_number(rows['openInterest'])) else '0'),
                'stkOptChangeInOpenInterest': int(rows['changeInOpenInterest'] if (utils.is_number(rows['changeInOpenInterest'])) else '0')
            }

            try:
                document = await self.stkOptCollection.find_one({
                    'symbol': str(rows['symbol']).strip(),
                    'expiryDate': parser.parse(str(rows['expiryDate']).strip()),
                    'strikePrice': int(rows['strikePrice'] if (utils.is_number(rows['strikePrice'])) else '0'),
                    'optionType': str(rows['optionType']).strip()
                    })
                if document:
                    result = await self.stkOptCollection.update_one({
                        'symbol': str(rows['symbol']).strip(),
                        'expiryDate': parser.parse(str(rows['expiryDate']).strip()),
                        'strikePrice': int(rows['strikePrice'] if (utils.is_number(rows['strikePrice'])) else '0'),
                        'optionType': str(rows['optionType']).strip()
                        },
                        {'$push': {'dailyData': dailyData}})
                    updateCount += 1
                else:
                    result = await self.stkOptCollection.insert_one({
                        'symbol': str(rows['symbol']),
                        'expiryDate': parser.parse(str(rows['expiryDate']).strip()),
                        'strikePrice': int(rows['strikePrice'] if (utils.is_number(rows['strikePrice'])) else '0'),
                        'optionType': str(rows['optionType']).strip(),
                        'dailyData': [dailyData]})
                    entryCount += 1
            except Exception as e:
                print('loadStkOptDataWithoutCheck () - ERROR : ', e)

        return entryCount, updateCount, skippedCount

    async def loadStkOptDataWithCheck(self):
        entryCount = 0
        updateCount = 0
        skippedCount = 0

        optionsCSVData = self.fnoData.getOptStkFlatData()
        for rows in optionsCSVData:
            dailyData = {
                'date': parser.parse(str(rows['timeStamp']).strip()),
                'stkOptOpenPrice': float(rows['open'] if (utils.is_number(rows['open'])) else '0.0'),
                'stkOptHighPrice': float(rows['high'] if (utils.is_number(rows['high'])) else '0.0'),
                'stkOptLowPrice': float(rows['low'] if (utils.is_number(rows['low'])) else '0.0'),
                'stkOptClosePrice': float(rows['close'] if (utils.is_number(rows['close'])) else '0.0'),
                'stkOptSettlePrice': float(rows['settlePrice'] if (utils.is_number(rows['settlePrice'])) else '0.0'),
                'stkOptContracts': (rows['contracts'] if (utils.is_number(rows['contracts'])) else '0'),
                'stkOptValueInLakhs': float(rows['valueInLakhs'] if (utils.is_number(rows['valueInLakhs'])) else '0.0'),
                'stkOptOpenInterest': int(rows['openInterest'] if (utils.is_number(rows['openInterest'])) else '0'),
                'stkOptChangeInOpenInterest': int(rows['changeInOpenInterest'] if (utils.is_number(rows['changeInOpenInterest'])) else '0')
            }

            try:
                dateList = []
                document = await self.stkOptCollection.find_one({
                    'symbol': str(rows['symbol']).strip(),
                    'expiryDate': parser.parse(str(rows['expiryDate']).strip()),
                    'strikePrice': int(rows['strikePrice'] if (utils.is_number(rows['strikePrice'])) else '0'),
                    'optionType': str(rows['optionType']).strip()
                })
                if document:
                    for items in document['dailyData']:
                        dateList.append(items['date'])

                    if dailyData['date'] in dateList:
                        # Data for this date is already present in Database
                        skippedCount += 1
                    else:
                        result = await self.stkOptCollection.update_one({
                            'symbol': str(rows['symbol']).strip(),
                            'expiryDate': parser.parse(str(rows['expiryDate']).strip()),
                            'strikePrice': int(rows['strikePrice'] if (utils.is_number(rows['strikePrice'])) else '0'),
                            'optionType': str(rows['optionType']).strip()
                            },
                            {'$push': {'dailyData': dailyData}})
                        updateCount += 1
                else:
                    result = await self.stkOptCollection.insert_one({
                        'symbol': str(rows['symbol']),
                        'expiryDate': parser.parse(str(rows['expiryDate']).strip()),
                        'strikePrice': int(rows['strikePrice'] if (utils.is_number(rows['strikePrice'])) else '0'),
                        'optionType': str(rows['optionType']).strip(),
                        'dailyData': [dailyData]})
                    entryCount += 1
            except Exception as e:
                print('loadStkOptDataWithoutCheck () - ERROR : ', e)

        return entryCount, updateCount, skippedCount

    # LOAD STOCK FUTURE DATA --------------------------------------------------------------------
    async def loadStkFutDataWithoutCheck(self):
        entryCount = 0
        updateCount = 0
        skippedCount = 0

        futuresCSVData = self.fnoData.getFutStkFlatData()
        for rows in futuresCSVData:
            dailyData = {
                'date': parser.parse(str(rows['timeStamp']).strip()),
                'stkFutOpenPrice': float(rows['open'] if (utils.is_number(rows['open'])) else '0.0'),
                'stkFutHighPrice': float(rows['high'] if (utils.is_number(rows['high'])) else '0.0'),
                'stkFutLowPrice': float(rows['low'] if (utils.is_number(rows['low'])) else '0.0'),
                'stkFutClosePrice': float(rows['close'] if (utils.is_number(rows['close'])) else '0.0'),
                'stkFutSettlePrice': float(rows['settlePrice'] if (utils.is_number(rows['settlePrice'])) else '0.0'),
                'stkFutContracts': int(rows['contracts'] if (utils.is_number(rows['contracts'])) else '0'),
                'stkFutValueInLakhs': float(rows['valueInLakhs'] if (utils.is_number(rows['valueInLakhs'])) else '0.0'),
                'stkFutOpenInterest': int(rows['openInterest'] if (utils.is_number(rows['openInterest'])) else '0'),
                'stkFutChangeInOpenInterest': int(rows['changeInOpenInterest'] if (utils.is_number(rows['changeInOpenInterest'])) else '0')
            }

            try:
                document = await self.stkFutCollection.find_one({
                    'symbol': str(rows['symbol']).strip(),
                    'expiryDate': parser.parse(str(rows['expiryDate']).strip())
                })

                if document:
                    result = await self.stkFutCollection.update_one({
                        'symbol': str(rows['symbol']).strip(),
                        'expiryDate': parser.parse(str(rows['expiryDate']).strip())
                    }, {'$push' : {'dailyData': dailyData}})
                    updateCount += 1
                else:
                    result = await self.stkFutCollection.insert_one({
                        'symbol': str(rows['symbol']).strip(),
                        'expiryDate': parser.parse(str(rows['expiryDate']).strip()),
                        'dailyData': [dailyData]
                    })
                    entryCount += 1

            except Exception as e:
                print('loadStkFutDatawithoutCheck () - ERROR : ', e)

        return entryCount, updateCount, skippedCount

    async def loadStkFutDataWithCheck(self):
        entryCount = 0
        updateCount = 0
        skippedCount = 0

        futuresCSVData = self.fnoData.getFutStkFlatData()
        for rows in futuresCSVData:
            dailyData = {
                'date': parser.parse(str(rows['timeStamp']).strip()),
                'stkFutOpenPrice': float(rows['open'] if (utils.is_number(rows['open'])) else '0.0'),
                'stkFutHighPrice': float(rows['high'] if (utils.is_number(rows['high'])) else '0.0'),
                'stkFutLowPrice': float(rows['low'] if (utils.is_number(rows['low'])) else '0.0'),
                'stkFutClosePrice': float(rows['close'] if (utils.is_number(rows['close'])) else '0.0'),
                'stkFutSettlePrice': float(rows['settlePrice'] if (utils.is_number(rows['settlePrice'])) else '0.0'),
                'stkFutContracts': int(rows['contracts'] if (utils.is_number(rows['contracts'])) else '0'),
                'stkFutValueInLakhs': float(rows['valueInLakhs'] if (utils.is_number(rows['valueInLakhs'])) else '0.0'),
                'stkFutOpenInterest': int(rows['openInterest'] if (utils.is_number(rows['openInterest'])) else '0'),
                'stkFutChangeInOpenInterest': int(
                    rows['changeInOpenInterest'] if (utils.is_number(rows['changeInOpenInterest'])) else '0')
            }

            try:
                dateList = []
                document = await self.stkFutCollection.find_one({
                    'symbol': str(rows['symbol']).strip(),
                    'expiryDate': parser.parse(str(rows['expiryDate']).strip())
                })

                if document:
                    for items in document['dailyData']:
                        dateList.append(items['date'])

                    if dailyData['date'] in dateList:
                        # Data for this date is already present in Database
                        skippedCount += 1
                    else:
                        result = await self.stkFutCollection.update_one({
                            'symbol': str(rows['symbol']).strip(),
                            'expiryDate': parser.parse(str(rows['expiryDate']).strip())
                        }, {'$push': {'dailyData': dailyData}})
                        updateCount += 1
                else:
                    result = await self.stkFutCollection.insert_one({
                        'symbol': str(rows['symbol']).strip(),
                        'expiryDate': parser.parse(str(rows['expiryDate']).strip()),
                        'dailyData': [dailyData]
                    })
                    entryCount += 1

            except Exception as e:
                print('loadStkFutDataWithCheck () - ERROR : ', e)

        return entryCount, updateCount, skippedCount

    # LOAD INDEX OPTION DATA --------------------------------------------------------------------
    async def loadIdxOptDataWithoutCheck(self):
        entryCount = 0
        updateCount = 0
        skippedCount = 0

        optionsCSVData = self.fnoData.getOptIdxFlatData()
        for rows in optionsCSVData:
            dailyData = {
                'date': parser.parse(str(rows['timeStamp']).strip()),
                'idxOptOpenPrice': float(rows['open'] if (utils.is_number(rows['open'])) else '0.0'),
                'idxOptHighPrice': float(rows['high'] if (utils.is_number(rows['high'])) else '0.0'),
                'idxOptLowPrice': float(rows['low'] if (utils.is_number(rows['low'])) else '0.0'),
                'idxOptClosePrice': float(rows['close'] if (utils.is_number(rows['close'])) else '0.0'),
                'idxOptSettlePrice': float(rows['settlePrice'] if (utils.is_number(rows['settlePrice'])) else '0.0'),
                'idxOptContracts': (rows['contracts'] if (utils.is_number(rows['contracts'])) else '0'),
                'idxOptValueInLakhs': float(rows['valueInLakhs'] if (utils.is_number(rows['valueInLakhs'])) else '0.0'),
                'idxOptOpenInterest': int(rows['openInterest'] if (utils.is_number(rows['openInterest'])) else '0'),
                'idxOptChangeInOpenInterest': int(
                    rows['changeInOpenInterest'] if (utils.is_number(rows['changeInOpenInterest'])) else '0')
            }

            try:
                document = await self.idxOptCollection.find_one({
                    'symbol': str(rows['symbol']).strip(),
                    'expiryDate': parser.parse(str(rows['expiryDate']).strip()),
                    'strikePrice': int(rows['strikePrice'] if (utils.is_number(rows['strikePrice'])) else '0'),
                    'optionType': str(rows['optionType']).strip()
                })
                if document:
                    result = await self.idxOptCollection.update_one({
                        'symbol': str(rows['symbol']).strip(),
                        'expiryDate': parser.parse(str(rows['expiryDate']).strip()),
                        'strikePrice': int(rows['strikePrice'] if (utils.is_number(rows['strikePrice'])) else '0'),
                        'optionType': str(rows['optionType']).strip()
                    },
                        {'$push': {'dailyData': dailyData}})
                    updateCount += 1
                else:
                    result = await self.idxOptCollection.insert_one({
                        'symbol': str(rows['symbol']),
                        'expiryDate': parser.parse(str(rows['expiryDate']).strip()),
                        'strikePrice': int(rows['strikePrice'] if (utils.is_number(rows['strikePrice'])) else '0'),
                        'optionType': str(rows['optionType']).strip(),
                        'dailyData': [dailyData]})
                    entryCount += 1
            except Exception as e:
                print('loadIdxOptDataWithoutCheck () - ERROR : ', e)

        return entryCount, updateCount, skippedCount

    async def loadIdxOptDataWithCheck(self):
        entryCount = 0
        updateCount = 0
        skippedCount = 0

        optionsCSVData = self.fnoData.getOptIdxFlatData()
        for rows in optionsCSVData:
            dailyData = {
                'date': parser.parse(str(rows['timeStamp']).strip()),
                'idxOptOpenPrice': float(rows['open'] if (utils.is_number(rows['open'])) else '0.0'),
                'idxOptHighPrice': float(rows['high'] if (utils.is_number(rows['high'])) else '0.0'),
                'idxOptLowPrice': float(rows['low'] if (utils.is_number(rows['low'])) else '0.0'),
                'idxOptClosePrice': float(rows['close'] if (utils.is_number(rows['close'])) else '0.0'),
                'idxOptSettlePrice': float(rows['settlePrice'] if (utils.is_number(rows['settlePrice'])) else '0.0'),
                'idxOptContracts': (rows['contracts'] if (utils.is_number(rows['contracts'])) else '0'),
                'idxOptValueInLakhs': float(rows['valueInLakhs'] if (utils.is_number(rows['valueInLakhs'])) else '0.0'),
                'idxOptOpenInterest': int(rows['openInterest'] if (utils.is_number(rows['openInterest'])) else '0'),
                'idxOptChangeInOpenInterest': int(
                    rows['changeInOpenInterest'] if (utils.is_number(rows['changeInOpenInterest'])) else '0')
            }

            try:
                dateList = []
                document = await self.idxOptCollection.find_one({
                    'symbol': str(rows['symbol']).strip(),
                    'expiryDate': parser.parse(str(rows['expiryDate']).strip()),
                    'strikePrice': int(rows['strikePrice'] if (utils.is_number(rows['strikePrice'])) else '0'),
                    'optionType': str(rows['optionType']).strip()
                })
                if document:
                    for items in document['dailyData']:
                        dateList.append(items['date'])

                    if dailyData['date'] in dateList:
                        # Data for this date is already present in Database
                        skippedCount += 1
                    else:
                        result = await self.idxOptCollection.update_one({
                            'symbol': str(rows['symbol']).strip(),
                            'expiryDate': parser.parse(str(rows['expiryDate']).strip()),
                            'strikePrice': int(rows['strikePrice'] if (utils.is_number(rows['strikePrice'])) else '0'),
                            'optionType': str(rows['optionType']).strip()
                        },
                            {'$push': {'dailyData': dailyData}})
                        updateCount += 1
                else:
                    result = await self.idxOptCollection.insert_one({
                        'symbol': str(rows['symbol']),
                        'expiryDate': parser.parse(str(rows['expiryDate']).strip()),
                        'strikePrice': int(rows['strikePrice'] if (utils.is_number(rows['strikePrice'])) else '0'),
                        'optionType': str(rows['optionType']).strip(),
                        'dailyData': [dailyData]})
                    entryCount += 1
            except Exception as e:
                print('loadIdxOptDataWithCheck () - ERROR : ', e)

        return entryCount, updateCount, skippedCount

    # LOAD INDEX FUTURE DATA --------------------------------------------------------------------
    async def loadIdxFutDataWithoutCheck(self):
        entryCount = 0
        updateCount = 0
        skippedCount = 0

        futuresCSVData = self.fnoData.getFutIdxFlatData()
        for rows in futuresCSVData:
            dailyData = {
                'date': parser.parse(str(rows['timeStamp']).strip()),
                'idxFutOpenPrice': float(rows['open'] if (utils.is_number(rows['open'])) else '0.0'),
                'idxFutHighPrice': float(rows['high'] if (utils.is_number(rows['high'])) else '0.0'),
                'idxFutLowPrice': float(rows['low'] if (utils.is_number(rows['low'])) else '0.0'),
                'idxFutClosePrice': float(rows['close'] if (utils.is_number(rows['close'])) else '0.0'),
                'idxFutSettlePrice': float(rows['settlePrice'] if (utils.is_number(rows['settlePrice'])) else '0.0'),
                'idxFutContracts': int(rows['contracts'] if (utils.is_number(rows['contracts'])) else '0'),
                'idxFutValueInLakhs': float(rows['valueInLakhs'] if (utils.is_number(rows['valueInLakhs'])) else '0.0'),
                'idxFutOpenInterest': int(rows['openInterest'] if (utils.is_number(rows['openInterest'])) else '0'),
                'idxFutChangeInOpenInterest': int(rows['changeInOpenInterest'] if (utils.is_number(rows['changeInOpenInterest'])) else '0')
            }

            try:
                document = await self.idxFutCollection.find_one({
                    'symbol': str(rows['symbol']).strip(),
                    'expiryDate': parser.parse(str(rows['expiryDate']).strip())
                })

                if document:
                    result = await self.idxFutCollection.update_one({
                        'symbol': str(rows['symbol']).strip(),
                        'expiryDate': parser.parse(str(rows['expiryDate']).strip())
                    }, {'$push': {'dailyData': dailyData}})
                    updateCount += 1
                else:
                    result = await self.idxFutCollection.insert_one({
                        'symbol': str(rows['symbol']).strip(),
                        'expiryDate': parser.parse(str(rows['expiryDate']).strip()),
                        'dailyData': [dailyData]
                    })
                    entryCount += 1

            except Exception as e:
                print('loadIdxFutDataWithoutCheck () - ERROR : ', e)

        return entryCount, updateCount, skippedCount

    async def loadIdxFutDataWithCheck(self):
        entryCount = 0
        updateCount = 0
        skippedCount = 0

        futuresCSVData = self.fnoData.getFutIdxFlatData()
        for rows in futuresCSVData:
            dailyData = {
                'date': parser.parse(str(rows['timeStamp']).strip()),
                'idxFutOpenPrice': float(rows['open'] if (utils.is_number(rows['open'])) else '0.0'),
                'idxFutHighPrice': float(rows['high'] if (utils.is_number(rows['high'])) else '0.0'),
                'idxFutLowPrice': float(rows['low'] if (utils.is_number(rows['low'])) else '0.0'),
                'idxFutClosePrice': float(rows['close'] if (utils.is_number(rows['close'])) else '0.0'),
                'idxFutSettlePrice': float(rows['settlePrice'] if (utils.is_number(rows['settlePrice'])) else '0.0'),
                'idxFutContracts': int(rows['contracts'] if (utils.is_number(rows['contracts'])) else '0'),
                'idxFutValueInLakhs': float(rows['valueInLakhs'] if (utils.is_number(rows['valueInLakhs'])) else '0.0'),
                'idxFutOpenInterest': int(rows['openInterest'] if (utils.is_number(rows['openInterest'])) else '0'),
                'idxFutChangeInOpenInterest': int(rows['changeInOpenInterest'] if (utils.is_number(rows['changeInOpenInterest'])) else '0')
            }

            try:
                dateList = []
                document = await self.idxFutCollection.find_one({
                    'symbol': str(rows['symbol']).strip(),
                    'expiryDate': parser.parse(str(rows['expiryDate']).strip())
                })

                if document:
                    for items in document['dailyData']:
                        dateList.append(items['date'])

                    if dailyData['date'] in dateList:
                        # Data for this date is already present in Database
                        skippedCount += 1
                    else:
                        result = await self.idxFutCollection.update_one({
                            'symbol': str(rows['symbol']).strip(),
                            'expiryDate': parser.parse(str(rows['expiryDate']).strip())
                        }, {'$push': {'dailyData': dailyData}})
                        updateCount += 1
                else:
                    result = await self.idxFutCollection.insert_one({
                        'symbol': str(rows['symbol']).strip(),
                        'expiryDate': parser.parse(str(rows['expiryDate']).strip()),
                        'dailyData': [dailyData]
                    })
                    entryCount += 1

            except Exception as e:
                print('loadIdxFutDataWithCheck () - ERROR : ', e)

        return entryCount, updateCount, skippedCount
