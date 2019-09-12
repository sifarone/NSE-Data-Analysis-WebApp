import datetime
from dateutil import parser

from . import cashUtils as utils

''' This class is used to recieve stock bhav data when read from DB '''

class BhavDataFromDB:
    def __init__(self, bhavData):
        self.date            = utils.convertDateToString(bhavData['date'])
        self.prevClose       = bhavData['prevClose']
        self.openPrice       = bhavData['openPrice']    
        self.highPrice       = bhavData['highPrice']   
        self.lowPrice        = bhavData['lowPrice']     
        self.lastPrice       = bhavData['lastPrice']    
        self.closePrice      = bhavData['closePrice']   
        self.avgPrice        = bhavData['avgPrice']     
        self.ttlTrdQtnty     = bhavData['ttlTrdQtnty']  
        self.turnoverLacs    = bhavData['turnoverLacs']
        self.noOfTrades      = bhavData['noOfTrades']   
        self.delivQty        = bhavData['delivQty']     
        self.delivPer        = bhavData['delivPer'] 

    def getBhavDataInfo(self):
        returnData = {}
        returnData.update({'date': self.date})
        returnData.update({'prevClose': self.prevClose})
        returnData.update({'openPrice': self.openPrice})
        returnData.update({'highPrice': self.highPrice})
        returnData.update({'lowPrice': self.lowPrice})
        returnData.update({'lastPrice': self.lastPrice})
        returnData.update({'closePrice': self.closePrice})
        returnData.update({'avgPrice': self.avgPrice})
        returnData.update({'ttlTrdQtnty': self.ttlTrdQtnty})
        returnData.update({'turnoverLacs': self.turnoverLacs})
        returnData.update({'noOfTrades': self.noOfTrades})
        returnData.update({'delivQty': self.delivQty})
        returnData.update({'delivPer': self.delivPer})
        return returnData


    def printData(self):
        print("     date         : ", utils.convertDateToString(self.date))
        print("     prevClose    : ", self.prevClose)
        print("     openPrice    : ", self.openPrice)
        print("     highPrice    : ", self.highPrice)
        print("     lowPrice     : ", self.lowPrice)
        print("     lastPrice    : ", self.lastPrice)
        print("     closePrice   : ", self.closePrice)
        print("     avgPrice     : ", self.avgPrice)
        print("     ttlTrdQtnty  : ", self.ttlTrdQtnty)
        print("     turnoverLacs : ", self.turnoverLacs)
        print("     noOfTrades   : ", self.noOfTrades)
        print("     delivQty     : ", self.delivQty)
        print("     delivPer     : ", self.delivPer)

class CashDataWrapper:
    def __init__(self, cashData):          
        self.symbol                 = cashData['symbol']
        self.bhavData               = {}
        for bd in cashData['bhavData']:
            data = BhavDataFromDB(bd)
            '''
            ****************** VERY VERY IMPORTANT ***********************
            In Memory the date has to be in string format (due to JSON serialization issues)
            In DB the date will be stored as datetime.date() object
            '''
            self.bhavData.update({utils.convertDateToString(bd['date']) : data})

    def printData(self):
        print()
        print('symbol               : ',self.symbol)
        
        print('----------- BhavData -------------')
        for d in self.bhavData:
            print('>> ',d,'  ::')
            print(self.bhavData[d].printData())
            print('-----------------------------------------')


    def getData(self): # returns by ascending date order
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

        dtDateList = [ utils.convertStringToDate(sDate) for sDate in self.bhavData.keys()]

        # Sort the dtDateList
        sortedDtDateList = sorted(dtDateList)
        sortedStrDateList = [utils.convertDateToString(dtDate) for dtDate in sortedDtDateList]

        # Construct the first row of the returnData {date: [sorted date list]}
        returnData.update({utils.dailyBhavDataFields['date']: sortedStrDateList})  # First row of the table, indexed by 'date'

        for field in utils.dailyBhavDataFields:
            l = []
            if field != 'date':
                for strDate in sortedStrDateList:
                    l.append(self.bhavData[strDate].getBhavDataInfo()[field])
                returnData.update({field: l})

        return returnData

    def getDataForAInterval(self, startDate, endDate=datetime.date.today()): # returns by ascending date order
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

        dtDateList = [utils.convertStringToDate(sDate) for sDate in self.bhavData.keys()]

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
            {utils.dailyBhavDataFields['date']: sortedStrDateList})  # First row of the table, indexed by 'date'

        for field in utils.dailyBhavDataFields:
            l = []
            if field != 'date':
                for strDate in sortedStrDateList:
                    l.append(self.bhavData[strDate].getBhavDataInfo()[field])
                returnData.update({field: l})

        return returnData






   
