import datetime
from dateutil import parser

# Date formater string
dateFormatString = "%d-%b-%Y"

# BhavData Fields
dailyDataFields = {
    'date': 'date',
    'openValue': 'openValue',
    'highValue': 'highValue',
    'lowValue': 'lowValue',
    'closingValue': 'closingValue',
    'pointsChange': 'pointsChange',
    'percentChange': 'percentChange',
    'volume': 'volume',
    'turnover': 'turnover',
    'peRatio': 'peRatio',
    'pbRatio': 'pbRatio',
    'divYield': 'divYield'
}

INDICES_COL_IDX = {
    'indexName': 0,
    'date': 1,
    'openValue': 2,
    'highValue': 3,
    'lowValue': 4,
    'closingValue': 5,
    'pointsChange': 6,
    'percentChange': 7,
    'volume': 8,
    'turnover': 9,
    'peRatio': 10,
    'pbRatio': 11,
    'divYield': 12
}

# Archived Index has less fields and different column positioning from "https://www.niftyindices.com/reports/historical-data"
# Combine two csv files manually, add the index name in first column of the sheet and then upload
STOCK_ARCHIVED_COL_IDX = {
    'indexName': 0,
    'date': 1,
    'openValue': 2,
    'highValue': 3,
    'lowValue': 4,
    'closingValue': 5,
    'peRatio': 6,
    'pbRatio': 7,
    'divYield': 8
}


# Function to check if a string contains numeric characters or not
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def convertStringToDate(strDate):
    # Returns date of type <class 'datetime.date'>
    return parser.parse(strDate).date()


def convertStringToDatetime(strDate):
    # Returns date of type <class 'datetime.datetime'>
    return parser.parse(strDate)


def convertDateToString(date):
    return date.strftime(dateFormatString)


def convertDatetimeToDate(d):
    # Converting datetime.datetime to datetime.date type
    return d.date()


def prettyPrintDailyData(dailyData):
    for key in dailyData:
        if key == 'date':
            dateList = [convertDateToString(x) for x in dailyData[key]]
            print(key, ' | ', dateList)
        else:
            print(key, ' | ', dailyData[key])



