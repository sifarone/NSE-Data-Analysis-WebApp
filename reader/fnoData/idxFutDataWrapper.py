import datetime
import copy

from . import fnoUtils as utils
from . import dailyDataUtils
from . import idxFutDailyDataWrapper

'''
1. This class is a wrapper over the Index Futures data (each document) fetched from Database.
2. It Adds few utility functions over this data to be used in the application
3. It indexes the and sorts daily data also according to daily date
'''


class IdxFutDataWrapper:  # Identifier key = (symbol, expiryDate, strikePrice, optionType)
    def __init__(self, idxFutureData):
        self.symbol     = idxFutureData['symbol']
        self.expiryDate = idxFutureData['expiryDate']
        self.dailyData  = {}  # Here instead of List (as in DB), construct a dictionary with date as key for each daily data structure
        for dd in idxFutureData['dailyData']:
            data = idxFutDailyDataWrapper.IdxFutDailyDataWrapper(dd)

            '''
            ****************** VERY VERY IMPORTANT ***********************
            In Memory the date has to be in string format (due to JSON serialization issues)
            In DB the date will be stored as datetime.date() object
            '''
            # Convert datetime.date() to string before using it as key
            self.dailyData.update({utils.convertDateToString(dd['date']): data})  # Here data also has trhe date in it.

        self.instrumentType = utils.instruments['indexFutures']

    def getSymbol(self):
        return self.symbol

    def getExpiyDate(self):
        return self.expiryDate

    def getUniqueIdKeysAsDict(self):
        key = {
            'symbol': self.symbol,
            'expiryDate': self.expiryDate
        }
        return key

    def getDailyDataRaw(self):
        return copy.deepcopy(self.dailyData)

    def getDailyData(self):  # In Ascending date order
        return dailyDataUtils.getDailyData(self.instrumentType, self.dailyData)

    def getDailyDataForATimeInterval(self, startDate, endDate=datetime.date.today()):  # returns by ascending date order
        return dailyDataUtils.getTabularDailyDataFromADate(self.instrumentType, self.dailyData, startDate, endDate)






