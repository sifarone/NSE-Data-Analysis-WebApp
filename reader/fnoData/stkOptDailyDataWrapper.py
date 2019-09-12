from . import fnoUtils as utils

class StkOptDailyDataWrapper:
    def __init__(self, dailyData):
        self.date                           = utils.convertDateToString(dailyData['date'])
        self.stkOptOpenPrice                = dailyData['stkOptOpenPrice']
        self.stkOptHighPrice                = dailyData['stkOptHighPrice']
        self.stkOptLowPrice                 = dailyData['stkOptLowPrice']
        self.stkOptClosePrice               = dailyData['stkOptClosePrice']
        self.stkOptSettlePrice              = dailyData['stkOptSettlePrice']
        self.stkOptContracts                = dailyData['stkOptContracts']
        self.stkOptValueInLakhs             = dailyData['stkOptValueInLakhs']
        self.stkOptOpenInterest             = dailyData['stkOptOpenInterest']
        self.stkOptChangeInOpenInterest     = dailyData['stkOptChangeInOpenInterest']

    def getDailyDatainListForm(self):
        returnList = []
        returnList.append(self.date)
        returnList.append(self.stkOptOpenPrice)
        returnList.append(self.stkOptHighPrice)
        returnList.append(self.stkOptLowPrice)
        returnList.append(self.stkOptClosePrice)
        returnList.append(self.stkOptSettlePrice)
        returnList.append(self.stkOptContracts)
        returnList.append(self.stkOptValueInLakhs)
        returnList.append(self.stkOptOpenInterest)
        returnList.append(self.stkOptChangeInOpenInterest)
        return returnList

    def getDailyDataInfo(self):
        returnData = {}
        returnData.update({'date': self.date})
        returnData.update({'stkOptOpenPrice': self.stkOptOpenPrice})
        returnData.update({'stkOptHighPrice': self.stkOptHighPrice})
        returnData.update({'stkOptLowPrice': self.stkOptLowPrice})
        returnData.update({'stkOptClosePrice': self.stkOptClosePrice})
        returnData.update({'stkOptSettlePrice': self.stkOptSettlePrice})
        returnData.update({'stkOptContracts': self.stkOptContracts})
        returnData.update({'stkOptValueInLakhs': self.stkOptValueInLakhs})
        returnData.update({'stkOptOpenInterest': self.stkOptOpenInterest})
        returnData.update({'stkOptChangeInOpenInterest': self.stkOptChangeInOpenInterest})
        return returnData

    def getStkOptDate(self):
        return self.date

    def getStkOptOpenPrice(self):
        return self.stkOptOpenPrice

    def getStkOptHighPrice(self):
        return self.stkOptHighPrice

    def getStkOptLowPrice(self):
        return self.stkOptLowPrice

    def getStkOptClosePrice(self):
        return self.stkOptClosePrice

    def getStkOptSettlePrice(self):
        return self.stkOptSettlePrice

    def getStkOptContracts(self):
        return self.stkOptContracts

    def getStkOptValueInLakhs(self):
        return self.stkOptValueInLakhs

    def getStkOptOpenInterest(self):
        return self.stkOptOpenInterest

    def getStkOptChangeInOpenInterest(self):
        return self.stkOptChangeInOpenInterest

    def printTypesOfDailyDataFields(self):
        print('type(date)                           : ', type(self.date))
        print('type(stkOptOpenPrice)                : ', type(self.stkOptOpenPrice))
        print('type(stkOptHighPrice)                : ', type(self.stkOptHighPrice))
        print('type(stkOptLowPrice)                 : ', type(self.stkOptLowPrice))
        print('type(stkOptClosePrice)               : ', type(self.stkOptClosePrice))
        print('type(stkOptSettlePrice)              : ', type(self.stkOptSettlePrice))
        print('type(stkOptContracts)                : ', type(self.stkOptContracts))
        print('type(stkOptValueInLakhs)             : ', type(self.stkOptValueInLakhs))
        print('type(stkOptOpenInterest)             : ', type(self.stkOptOpenInterest))
        print('type(stkOptChangeInOpenInterest)     : ', type(self.stkOptChangeInOpenInterest))

    def printDailyData(self)   :
        print('date                         : ', self.date)
        print('stkOptOpenPrice              : ', self.stkOptOpenPrice)
        print('stkOptHighPrice              : ', self.stkOptHighPrice)
        print('stkOptLowPrice               : ', self.stkOptLowPrice)
        print('stkOptClosePrice             : ', self.stkOptClosePrice)
        print('stkOptSettlePrice            : ', self.stkOptSettlePrice)
        print('stkOptContracts              : ', self.stkOptContracts)
        print('stkOptValueInLakhs           : ', self.stkOptValueInLakhs)
        print('stkOptOpenInterest           : ', self.stkOptOpenInterest)
        print('stkOptChangeInOpenInterest   : ', self.stkOptChangeInOpenInterest)