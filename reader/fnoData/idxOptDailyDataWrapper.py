from . import fnoUtils as utils

class IdxOptDailyDataWrapper:
    def __init__(self, dailyData):
        self.date                           = utils.convertDateToString(dailyData['date'])
        self.idxOptOpenPrice                = dailyData['idxOptOpenPrice']
        self.idxOptHighPrice                = dailyData['idxOptHighPrice']
        self.idxOptLowPrice                 = dailyData['idxOptLowPrice']
        self.idxOptClosePrice               = dailyData['idxOptClosePrice']
        self.idxOptSettlePrice              = dailyData['idxOptSettlePrice']
        self.idxOptContracts                = dailyData['idxOptContracts']
        self.idxOptValueInLakhs             = dailyData['idxOptValueInLakhs']
        self.idxOptOpenInterest             = dailyData['idxOptOpenInterest']
        self.idxOptChangeInOpenInterest     = dailyData['idxOptChangeInOpenInterest']

    def getDailyDatainListForm(self):
        returnList = []
        returnList.append(self.date)
        returnList.append(self.idxOptOpenPrice)
        returnList.append(self.idxOptHighPrice)
        returnList.append(self.idxOptLowPrice)
        returnList.append(self.idxOptClosePrice)
        returnList.append(self.idxOptSettlePrice)
        returnList.append(self.idxOptContracts)
        returnList.append(self.idxOptValueInLakhs)
        returnList.append(self.idxOptOpenInterest)
        returnList.append(self.idxOptChangeInOpenInterest)
        return returnList

    def getDailyDataInfo(self):
        returnData = {}
        returnData.update({'date': self.date})
        returnData.update({'idxOptOpenPrice': self.idxOptOpenPrice})
        returnData.update({'idxOptHighPrice': self.idxOptHighPrice})
        returnData.update({'idxOptLowPrice': self.idxOptLowPrice})
        returnData.update({'idxOptClosePrice': self.idxOptClosePrice})
        returnData.update({'idxOptSettlePrice': self.idxOptSettlePrice})
        returnData.update({'idxOptContracts': self.idxOptContracts})
        returnData.update({'idxOptValueInLakhs': self.idxOptValueInLakhs})
        returnData.update({'idxOptOpenInterest': self.idxOptOpenInterest})
        returnData.update({'idxOptChangeInOpenInterest': self.idxOptChangeInOpenInterest})
        return returnData

    def getidxOptDate(self):
        return self.date

    def getidxOptOpenPrice(self):
        return self.idxOptOpenPrice

    def getidxOptHighPrice(self):
        return self.idxOptHighPrice

    def getidxOptLowPrice(self):
        return self.idxOptLowPrice

    def getidxOptClosePrice(self):
        return self.idxOptClosePrice

    def getidxOptSettlePrice(self):
        return self.idxOptSettlePrice

    def getidxOptContracts(self):
        return self.idxOptContracts

    def getidxOptValueInLakhs(self):
        return self.idxOptValueInLakhs

    def getidxOptOpenInterest(self):
        return self.idxOptOpenInterest

    def getidxOptChangeInOpenInterest(self):
        return self.idxOptChangeInOpenInterest

    def printTypesOfDailyDataFields(self):
        print('type(date)                           : ', type(self.date))
        print('type(idxOptOpenPrice)                : ', type(self.idxOptOpenPrice))
        print('type(idxOptHighPrice)                : ', type(self.idxOptHighPrice))
        print('type(idxOptLowPrice)                 : ', type(self.idxOptLowPrice))
        print('type(idxOptClosePrice)               : ', type(self.idxOptClosePrice))
        print('type(idxOptSettlePrice)              : ', type(self.idxOptSettlePrice))
        print('type(idxOptContracts)                : ', type(self.idxOptContracts))
        print('type(idxOptValueInLakhs)             : ', type(self.idxOptValueInLakhs))
        print('type(idxOptOpenInterest)             : ', type(self.idxOptOpenInterest))
        print('type(idxOptChangeInOpenInterest)     : ', type(self.idxOptChangeInOpenInterest))

    def printDailyData(self)   :
        print('date                         : ', self.date)
        print('idxOptOpenPrice              : ', self.idxOptOpenPrice)
        print('idxOptHighPrice              : ', self.idxOptHighPrice)
        print('idxOptLowPrice               : ', self.idxOptLowPrice)
        print('idxOptClosePrice             : ', self.idxOptClosePrice)
        print('idxOptSettlePrice            : ', self.idxOptSettlePrice)
        print('idxOptContracts              : ', self.idxOptContracts)
        print('idxOptValueInLakhs           : ', self.idxOptValueInLakhs)
        print('idxOptOpenInterest           : ', self.idxOptOpenInterest)
        print('idxOptChangeInOpenInterest   : ', self.idxOptChangeInOpenInterest)