import datetime

from . import indexUtils as utils

''' This class is used to recieve Index daily data when read from DB '''


class DailyDataFromDB:
    def __init__(self, dailyData):
        self.date           = utils.convertDateToString(dailyData['date'])
        self.openValue      = dailyData['openValue']
        self.highValue      = dailyData['highValue']
        self.lowValue       = dailyData['lowValue']
        self.closingValue   = dailyData['closingValue']
        self.pointsChange   = dailyData['pointsChange']
        self.percentChange  = dailyData['percentChange']
        self.volume         = dailyData['volume']
        self.turnover       = dailyData['turnover']
        self.peRatio        = dailyData['peRatio']
        self.pbRatio        = dailyData['pbRatio']
        self.divYield       = dailyData['divYield']

    def getDailyDataInfo(self):
        returnData = {}
        returnData.update({'date': self.date})
        returnData.update({'openValue': self.openValue})
        returnData.update({'highValue': self.highValue})
        returnData.update({'lowValue': self.lowValue})
        returnData.update({'closingValue': self.closingValue})
        returnData.update({'pointsChange': self.pointsChange})
        returnData.update({'percentChange': self.percentChange})
        returnData.update({'volume': self.volume})
        returnData.update({'turnover': self.turnover})
        returnData.update({'peRatio': self.peRatio})
        returnData.update({'pbRatio': self.pbRatio})
        returnData.update({'divYield': self.divYield})
        return returnData

    def printData(self):
        print("date             : ", utils.convertDateToString(self.date))
        print("openValue        : ", self.openValue)
        print("highValue        : ", self.highValue)
        print("lowValue         : ", self.lowValue)
        print("closingValue     : ", self.closingValue)
        print("pointsChange     : ", self.pointsChange)
        print("percentChange    : ", self.percentChange)
        print("volume           : ", self.volume)
        print("turnover         : ", self.turnover)
        print("peRatio          : ", self.peRatio)
        print("pbRatio          : ", self.pbRatio)
        print("divYield         : ", self.divYield)


class IndexDataWrapper:
    def __init__(self, indicesData):
        self.indexName  = indicesData['indexName']
        self.dailyData  = {}
        for dd in indicesData['dailyData']:
            data = DailyDataFromDB(dd)
            '''
            ****************** VERY VERY IMPORTANT ***********************
            In Memory the date has to be in string format (due to JSON serialization issues)
            In DB the date will be stored as datetime.date() object
            '''
            self.dailyData.update({utils.convertDateToString(dd['date']): data})

    def getIndicesInfo(self):
        returnData = {}
        returnData.update({'indexName': self.indexName})
        return returnData

    def printData(self):
        print()
        print('indexName               : ', self.indexName)

        print('----------- BhavData -------------')
        for d in self.dailyData:
            print('>> ', d, '  ::')
            print(self.dailyData[d].printData())
            print('-----------------------------------------')

    def getData(self):  # returns by ascending date order
        '''
        Returns daily data in following format:
        {
            date : [date1-string | date2-string | date3-string | ...], Ascending order ->
            prevClose : [prevClose1 | prevClose2 | prevClose3 | ...],
            .
            .
            .
            delivPer : [delivPer1 | delivPer2 | delivPer3 | .....]
        }
        '''

        returnData = {}

        dtDateList = [utils.convertStringToDate(sDate) for sDate in self.dailyData.keys()]

        # Sort the dtDateList
        sortedDtDateList = sorted(dtDateList)
        sortedStrDateList = [utils.convertDateToString(dtDate) for dtDate in sortedDtDateList]

        # Construct the first row of the returnData {date: [sorted date list]}
        returnData.update(
            {utils.dailyDataFields['date']: sortedStrDateList})  # First row of the table, indexed by 'date'

        for field in utils.dailyDataFields:
            l = []
            if field != 'date':
                for strDate in sortedStrDateList:
                    l.append(self.dailyData[strDate].getDailyDataInfo()[field])
                returnData.update({field: l})

        return returnData

    def getDataForAInterval(self, startDate,
                                              endDate=datetime.date.today()):  # returns by ascending date order
        '''
        Returns daily data in following format:
        {
            date : [date1-string | date2-string | date3-string | ...], Ascending order ->
            prevClose : [prevClose1 | prevClose2 | prevClose3 | ...],
            .
            .
            .
            delivPer : [delivPer1 | delivPer2 | delivPer3 | .....]
        }
        '''

        returnData = {}

        dtDateList = [utils.convertStringToDate(sDate) for sDate in self.dailyData.keys()]

        selectedDtDates = []
        # Select the dates in valid range
        for dtDate in dtDateList:
            if dtDate >= startDate and dtDate <= endDate:
                selectedDtDates.append(dtDate)

        # Sort the dtDateList
        sortedDtDateList = sorted(selectedDtDates)
        sortedStrDateList = [utils.convertDateToString(dtDate) for dtDate in sortedDtDateList]

        # Construct the first row of the returnData {date: [sorted date list]}
        returnData.update(
            {utils.dailyDataFields['date']: sortedStrDateList})  # First row of the table, indexed by 'date'

        for field in utils.dailyDataFields:
            l = []
            if field != 'date':
                for strDate in sortedStrDateList:
                    l.append(self.dailyData[strDate].getDailyDataInfo()[field])
                returnData.update({field: l})

        return returnData






