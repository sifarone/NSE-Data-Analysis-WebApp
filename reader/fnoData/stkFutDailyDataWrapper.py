from . import fnoUtils as utils

class StkFutDailyDataWrapper:
    def __init__(self, dailyData):
        self.date                           = utils.convertDateToString(dailyData['date'])
        self.stkFutOpenPrice                = dailyData['stkFutOpenPrice']
        self.stkFutHighPrice                = dailyData['stkFutHighPrice']
        self.stkFutLowPrice                 = dailyData['stkFutLowPrice']
        self.stkFutClosePrice               = dailyData['stkFutClosePrice']
        self.stkFutSettlePrice              = dailyData['stkFutSettlePrice']
        self.stkFutContracts                = dailyData['stkFutContracts']
        self.stkFutValueInLakhs             = dailyData['stkFutValueInLakhs']
        self.stkFutOpenInterest             = dailyData['stkFutOpenInterest']
        self.stkFutChangeInOpenInterest     = dailyData['stkFutChangeInOpenInterest']

    def getDailyDatainListForm(self):
        returnList = []
        returnList.append(self.date)
        returnList.append(self.stkFutOpenPrice)
        returnList.append(self.stkFutHighPrice)
        returnList.append(self.stkFutLowPrice)
        returnList.append(self.stkFutClosePrice)
        returnList.append(self.stkFutSettlePrice)
        returnList.append(self.stkFutContracts)
        returnList.append(self.stkFutValueInLakhs)
        returnList.append(self.stkFutOpenInterest)
        returnList.append(self.stkFutChangeInOpenInterest)
        return returnList

    def getDailyDataInfo(self):
        returnData = {}
        returnData.update({'date': self.date})
        returnData.update({'stkFutOpenPrice': self.stkFutOpenPrice})
        returnData.update({'stkFutHighPrice': self.stkFutHighPrice})
        returnData.update({'stkFutLowPrice': self.stkFutLowPrice})
        returnData.update({'stkFutClosePrice': self.stkFutClosePrice})
        returnData.update({'stkFutSettlePrice': self.stkFutSettlePrice})
        returnData.update({'stkFutContracts': self.stkFutContracts})
        returnData.update({'stkFutValueInLakhs': self.stkFutValueInLakhs})
        returnData.update({'stkFutOpenInterest': self.stkFutOpenInterest})
        returnData.update({'stkFutChangeInOpenInterest': self.stkFutChangeInOpenInterest})
        return returnData

    def getstkFutDate(self):
        return self.date

    def getstkFutOpenPrice(self):
        return self.stkFutOpenPrice

    def getstkFutHighPrice(self):
        return self.stkFutHighPrice

    def getstkFutLowPrice(self):
        return self.stkFutLowPrice

    def getstkFutClosePrice(self):
        return self.stkFutClosePrice

    def getstkFutSettlePrice(self):
        return self.stkFutSettlePrice

    def getstkFutContracts(self):
        return self.stkFutContracts

    def getstkFutValueInLakhs(self):
        return self.stkFutValueInLakhs

    def getstkFutOpenInterest(self):
        return self.stkFutOpenInterest

    def getstkFutChangeInOpenInterest(self):
        return self.stkFutChangeInOpenInterest

    def printTypesOfDailyDataFields(self):
        print('type(date)                           : ', type(self.date))
        print('type(stkFutOpenPrice)                : ', type(self.stkFutOpenPrice))
        print('type(stkFutHighPrice)                : ', type(self.stkFutHighPrice))
        print('type(stkFutLowPrice)                 : ', type(self.stkFutLowPrice))
        print('type(stkFutClosePrice)               : ', type(self.stkFutClosePrice))
        print('type(stkFutSettlePrice)              : ', type(self.stkFutSettlePrice))
        print('type(stkFutContracts)                : ', type(self.stkFutContracts))
        print('type(stkFutValueInLakhs)             : ', type(self.stkFutValueInLakhs))
        print('type(stkFutOpenInterest)             : ', type(self.stkFutOpenInterest))
        print('type(stkFutChangeInOpenInterest)     : ', type(self.stkFutChangeInOpenInterest))

    def printDailyData(self)   :
        print('date                         : ', self.date)
        print('stkFutOpenPrice              : ', self.stkFutOpenPrice)
        print('stkFutHighPrice              : ', self.stkFutHighPrice)
        print('stkFutLowPrice               : ', self.stkFutLowPrice)
        print('stkFutClosePrice             : ', self.stkFutClosePrice)
        print('stkFutSettlePrice            : ', self.stkFutSettlePrice)
        print('stkFutContracts              : ', self.stkFutContracts)
        print('stkFutValueInLakhs           : ', self.stkFutValueInLakhs)
        print('stkFutOpenInterest           : ', self.stkFutOpenInterest)
        print('stkFutChangeInOpenInterest   : ', self.stkFutChangeInOpenInterest)