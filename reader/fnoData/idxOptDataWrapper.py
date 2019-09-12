import datetime
import copy

from . import fnoUtils as utils
from . import dailyDataUtils
from . import idxOptDailyDataWrapper

'''
1. This class is a wrapper over the stock option data (each document) fetched from Database.
2. It Adds few utility functions over this data to be used in the application
3. It indexes the and sorts daily data also according to daily date
'''


class IdxOptDataWrapper:
    def __init__(self, idxOptionData):
        self.symbol         = idxOptionData['symbol']
        self.expiryDate     = idxOptionData['expiryDate']
        self.strikePrice    = idxOptionData['strikePrice']
        self.optionType     = idxOptionData['optionType']
        self.dailyData      = {}  # Here instead of List (as in DB), construct a dictionary with date as key for each daily data structure
        for dd in idxOptionData['dailyData']:
            data = idxOptDailyDataWrapper.IdxOptDailyDataWrapper(dd)

            # Convert the date key (in datetime.date() type to string type before using it as key
            '''
            ****************** VERY VERY IMPORTANT ***********************
            In Memory the date has to be in string format (due to JSON serialization issues)
            In DB the date will be stored as datetime.date() object
            '''
            self.dailyData.update({utils.convertDateToString(dd['date']): data})  # Here data also has the date in it.

        self.instrumentType = utils.instruments['indexOptions']

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

    def getDailyData(self):  # In Ascending date order
        return dailyDataUtils.getDailyData(self.instrumentType, self.dailyData)

    def getDailyDataForATimeInterval(self, startDate, endDate=datetime.date.today()):  # returns by ascending date order
        return dailyDataUtils.getDailyDataForAInterval(self.instrumentType, self.dailyData, startDate, endDate)





