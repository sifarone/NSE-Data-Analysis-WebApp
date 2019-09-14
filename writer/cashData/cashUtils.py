import datetime
from dateutil import parser

# Date formater string
dateFormatString = "%d-%b-%Y"

# BhavData Fields
dailyBhavDataFields = {
    # 'symbol'        : 'symbol',
    'date'              : 'date',
    'prevClose'         : 'prevClose',
    'openPrice'         : 'openPrice',
    'highPrice'         : 'highPrice',
    'lowPrice'          : 'lowPrice',
    'lastPrice'         : 'lastPrice',
    'closePrice'        : 'closePrice',
    'avgPrice'          : 'avgPrice',
    'ttlTrdQtnty'       : 'ttlTrdQtnty',
    'turnoverLacs'      : 'turnoverLacs',
    'noOfTrades'        : 'noOfTrades',
    'delivQty'          : 'delivQty',
    'delivPer'          : 'delivPer'
}

STOCK_COL_IDX = {
    "symbol"            : 0,
    'date'              : 2,  # Skip the 'Series' column
    'prevClose'         : 3,
    'openPrice'         : 4,
    'highPrice'         : 5,
    'lowPrice'          : 6,
    'lastPrice'         : 7,
    'closePrice'        : 8,
    'avgPrice'          : 9,
    'ttlTrdQtnty'       : 10,
    'turnoverLacs'      : 11,
    'noOfTrades'        : 12,
    'delivQty'          : 13,
    'delivPer'          : 14
}

# Archived bhavcopy has less fields and different column positioning
STOCK_ARCHIVED_COL_IDX = {
    'symbol'            : 0,
    'openPrice'         : 2,
    'highPrice'         : 3,
    'lowPrice'          : 4,
    'closePrice'        : 5,
    'lastPrice'         : 6,
    'prevClose'         : 7,
    'date'              : 10
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


def prettyPrintBhavData(bhavData):
    for key in bhavData:
        if key == 'date':
            dateList = [convertDateToString(x) for x in bhavData[key]]
            print(key, ' | ', dateList)
        else:
            print(key, ' | ', bhavData[key])



