import datetime
import copy

from . import fnoUtils as utils
from . import dailyDataUtils
from . import stkOptDailyDataWrapper

'''
1. This class is a wrapper over the stock option data (each document) fetched from Database.
2. It Adds few utility functions over this data to be used in the application
3. It indexes the and sorts daily data also according to daily date

Description:
Here convert the flat daily data from DB, to a key-value pair where 
the key of a data is the 'date' field from that data and the value is the complete data itself.
i.e. dailyData is now of the following form in memory
{
    date1-string: {data1},
    date2-string: {data2},
    .
    .
    .
}
'''
class StkOptDataWrapper:  # Identifier key = (symbol, expiryDate, strikePrice, optionType)
    def __init__(self, stkOptionData):
        self.symbol = stkOptionData['symbol']
        self.expiryDate = stkOptionData['expiryDate']
        self.strikePrice = stkOptionData['strikePrice']
        self.optionType = stkOptionData['optionType']
        self.dailyData = {}  # Here instead of List (as in DB), construct a dictionary with date as key for each daily data structure
        for dd in stkOptionData['dailyData']:
            data = stkOptDailyDataWrapper.StkOptDailyDataWrapper(dd)

            '''
            ****************** VERY VERY IMPORTANT ***********************
            In Memory the date has to be in string format (due to JSON serialization issues)
            In DB the date will be stored as datetime.date() object
            '''
            self.dailyData.update({utils.convertDateToString(dd['date']): data})  # Here data also has trhe date in it.

        self.instrumentType = utils.instruments['stockOptions']

    def getSymbol(self):
        return self.symbol

    def getExpiyDate(self):
        return self.expiryDate

    def getStrikePrice(self):
        return self.strikePrice

    def getOptionType(self):
        return self.optionType

    def getUniqueIdKeysAsDict(self):
        key = {
            'symbol': self.symbol,
            'expiryDate': self.expiryDate,
            'strikePrice': self.strikePrice,
            'optionType': self.optionType
        }
        return key

    def getDailyDataRaw(self):
        return copy.deepcopy(self.dailyData)

    def getDailyData(self):
        return dailyDataUtils.getDailyData(self.instrumentType, self.dailyData)

    def getDailyDataForATimeInterval(self, startDate, endDate=datetime.date.today()):
        return dailyDataUtils.getDailyDataForAInterval(self.instrumentType, self.dailyData, startDate, endDate)






