
from . import fnoUtils as utils


def getDailyData(instrumentType, dailyData):
    '''
        Returns all Daily Data In Ascending date order after doing the following conversion:

        Current in memory dailyData format:
        {
            date1-string : {
                        date: date1,
                        open: open1,
                        high: high1,
                        .
                        .
                        changeInOpenInterest : changeInOpenInterest1
                    },

            date2-string : {
                        date: date2,
                        open: open2,
                        high: high2,
                        .
                        .
                        changeInOpenInterest : changeInOpenInterest2
                    },
                    .
                    .
                    .
        }

        Return dailyData Fromat:
        {
            date : [date1-string | date2-string | date3-string | ...], Ascending order ->
            open : [open1 | open2 | open3 | ...],
            .
            .
            .
            chnageInOpenInterest : [chnageInOpenInterest1 | chnageInOpenInterest2 | chnageInOpenInterest3 | .....]
        }
    '''

    #data = {}
    returnData = {}
    dailyDataFields = {}

    if instrumentType == utils.instruments['stockOptions']:
        dailyDataFields = utils.stkOptDailyDataFields
    elif instrumentType == utils.instruments['stockFutures']:
        dailyDataFields = utils.stkFutDailyDataFields
    elif instrumentType == utils.instruments['indexOptions']:
        dailyDataFields = utils.idxOptDailyDataFields
    elif instrumentType == utils.instruments['indexFutures']:
        dailyDataFields = utils.idxFutDailyDataFields


    dtDateList = [utils.convertStringToDate(sDate) for sDate in dailyData.keys()]

    # Sort the dtDates List
    sortedDtDateList = sorted(dtDateList)
    sortedStrDateList = [utils.convertDateToString(dtDate) for dtDate in sortedDtDateList]

    # Construct the first row of the returnData {date: [sorted date list]}
    returnData.update({dailyDataFields['date']: sortedStrDateList})
    # Construct sorted date wise list of other daily data except date as it has already been constructed above
    for field in dailyDataFields:  # Loop through the names(keys) of all fields
        l = []
        # Leave out date field as we have already constructed its sorted list above
        for strDate in sortedStrDateList:  # Loop over the sorted date list
            l.append(dailyData[strDate].getDailyDataInfo()[field])
        returnData.update({field: l})
    return returnData

def getDailyDataForAInterval(instrumentType, dailyData, startDate, endDate):
    '''
        startDate:  datetime.date() object
        endDate:    datetime.date() object

        Returns all Daily Data In Ascending date order after doing the following conversion:

        Current in memory dailyData format:
        {
            date1-string : {
                        date: date1,
                        open: open1,
                        high: high1,
                        .
                        .
                        changeInOpenInterest : changeInOpenInterest1
                    },

            date2-string : {
                        date: date2,
                        open: open2,
                        high: high2,
                        .
                        .
                        changeInOpenInterest : changeInOpenInterest2
                    },
                    .
                    .
                    .
        }

        Return dailyData Fromat:
        {
            date : [date1-string | date2-string | date3-string | ...], Ascending order ->
            open : [open1 | open2 | open3 | ...],
            .
            .
            .
            chnageInOpenInterest : [chnageInOpenInterest1 | chnageInOpenInterest2 | chnageInOpenInterest3 | .....]
        }
    '''


    returnData = {}
    dailyDataFields = {}

    if instrumentType == utils.instruments['stockOptions']:
        dailyDataFields = utils.stkOptDailyDataFields
    elif instrumentType == utils.instruments['stockFutures']:
        dailyDataFields = utils.stkFutDailyDataFields
    elif instrumentType == utils.instruments['indexOptions']:
        dailyDataFields = utils.idxOptDailyDataFields
    elif instrumentType == utils.instruments['indexFutures']:
        dailyDataFields = utils.idxFutDailyDataFields

    dtDateList = [utils.convertStringToDate(sDate) for sDate in dailyData.keys()]

    selectedDtDates = []
    # Select the dates in valid range
    for dtDate in dtDateList:
        if dtDate >= startDate and dtDate <= endDate:
            selectedDtDates.append(dtDate)

    # Sort the slected dtDates List
    sortedDtDateList = sorted(selectedDtDates)
    sortedStrDateList = [utils.convertDateToString(dtDate) for dtDate in sortedDtDateList]

    # Construct the first row of the returnData {date: [sorted date list]}
    returnData.update({dailyDataFields['date']: sortedStrDateList})
    # Construct sorted date wise list of other daily data except date as it has already been constructed above
    for field in dailyDataFields:  # Loop through the names(keys) of all fields
        l = []
        # Leave out date field as we have already constructed its sorted list above
        for strDate in sortedStrDateList:  # Loop over the sorted date list
            l.append(dailyData[strDate].getDailyDataInfo()[field])
        returnData.update({field: l})
    return returnData




