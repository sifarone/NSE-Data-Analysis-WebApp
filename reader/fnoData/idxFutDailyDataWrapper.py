from . import fnoUtils as utils

class IdxFutDailyDataWrapper:
    def __init__(self, dailyData):
        self.date                           = utils.convertDateToString(dailyData['date'])
        self.idxFutOpenPrice                = dailyData['idxFutOpenPrice']
        self.idxFutHighPrice                = dailyData['idxFutHighPrice']
        self.idxFutLowPrice                 = dailyData['idxFutLowPrice']
        self.idxFutClosePrice               = dailyData['idxFutClosePrice']
        self.idxFutSettlePrice              = dailyData['idxFutSettlePrice']
        self.idxFutContracts                = dailyData['idxFutContracts']
        self.idxFutValueInLakhs             = dailyData['idxFutValueInLakhs']
        self.idxFutOpenInterest             = dailyData['idxFutOpenInterest']
        self.idxFutChangeInOpenInterest     = dailyData['idxFutChangeInOpenInterest']

    def getDailyDatainListForm(self):
        returnList = []
        returnList.append(self.date)
        returnList.append(self.idxFutOpenPrice)
        returnList.append(self.idxFutHighPrice)
        returnList.append(self.idxFutLowPrice)
        returnList.append(self.idxFutClosePrice)
        returnList.append(self.idxFutSettlePrice)
        returnList.append(self.idxFutContracts)
        returnList.append(self.idxFutValueInLakhs)
        returnList.append(self.idxFutOpenInterest)
        returnList.append(self.idxFutChangeInOpenInterest)
        return returnList

    def getDailyDataInfo(self):
        returnData = {}
        returnData.update({'date': self.date})
        returnData.update({'idxFutOpenPrice': self.idxFutOpenPrice})
        returnData.update({'idxFutHighPrice': self.idxFutHighPrice})
        returnData.update({'idxFutLowPrice': self.idxFutLowPrice})
        returnData.update({'idxFutClosePrice': self.idxFutClosePrice})
        returnData.update({'idxFutSettlePrice': self.idxFutSettlePrice})
        returnData.update({'idxFutContracts': self.idxFutContracts})
        returnData.update({'idxFutValueInLakhs': self.idxFutValueInLakhs})
        returnData.update({'idxFutOpenInterest': self.idxFutOpenInterest})
        returnData.update({'idxFutChangeInOpenInterest': self.idxFutChangeInOpenInterest})
        return returnData

    def getidxFutDate(self):
        return self.date

    def getidxFutOpenPrice(self):
        return self.idxFutOpenPrice

    def getidxFutHighPrice(self):
        return self.idxFutHighPrice

    def getidxFutLowPrice(self):
        return self.idxFutLowPrice

    def getidxFutClosePrice(self):
        return self.idxFutClosePrice

    def getidxFutSettlePrice(self):
        return self.idxFutSettlePrice

    def getidxFutContracts(self):
        return self.idxFutContracts

    def getidxFutValueInLakhs(self):
        return self.idxFutValueInLakhs

    def getidxFutOpenInterest(self):
        return self.idxFutOpenInterest

    def getidxFutChangeInOpenInterest(self):
        return self.idxFutChangeInOpenInterest

    def printTypesOfDailyDataFields(self):
        print('type(date)                           : ', type(self.date))
        print('type(idxFutOpenPrice)                : ', type(self.idxFutOpenPrice))
        print('type(idxFutHighPrice)                : ', type(self.idxFutHighPrice))
        print('type(idxFutLowPrice)                 : ', type(self.idxFutLowPrice))
        print('type(idxFutClosePrice)               : ', type(self.idxFutClosePrice))
        print('type(idxFutSettlePrice)              : ', type(self.idxFutSettlePrice))
        print('type(idxFutContracts)                : ', type(self.idxFutContracts))
        print('type(idxFutValueInLakhs)             : ', type(self.idxFutValueInLakhs))
        print('type(idxFutOpenInterest)             : ', type(self.idxFutOpenInterest))
        print('type(idxFutChangeInOpenInterest)     : ', type(self.idxFutChangeInOpenInterest))

    def printDailyData(self)   :
        print('date                         : ', self.date)
        print('idxFutOpenPrice              : ', self.idxFutOpenPrice)
        print('idxFutHighPrice              : ', self.idxFutHighPrice)
        print('idxFutLowPrice               : ', self.idxFutLowPrice)
        print('idxFutClosePrice             : ', self.idxFutClosePrice)
        print('idxFutSettlePrice            : ', self.idxFutSettlePrice)
        print('idxFutContracts              : ', self.idxFutContracts)
        print('idxFutValueInLakhs           : ', self.idxFutValueInLakhs)
        print('idxFutOpenInterest           : ', self.idxFutOpenInterest)
        print('idxFutChangeInOpenInterest   : ', self.idxFutChangeInOpenInterest)