from dateutil import parser

# Number of coulumns in FnO CSV file
NO_OF_COULMNS = 15

# Date formater string
dateFormatString = "%d-%b-%Y"

# Types of Instruments in the FnO csv file
instruments = {
    "indexFutures": "FUTIDX",
    "indexOptions": "OPTIDX",
    "stockFutures": "FUTSTK",
    "stockOptions": "OPTSTK"
}

# Coulmn name indexes in FnO csv
'''
['INSTRUMENT', 'SYMBOL', 'EXPIRY_DT', 'STRIKE_PR', 'OPTION_TYP', 'OPEN',
 'HIGH', 'LOW', 'CLOSE', 'SETTLE_PR', 'CONTRACTS', 'VAL_INLAKH', 'OPEN_INT', 'CHG_IN_OI', 'TIMESTAMP']
 '''
FNO_COL_IDX = {
    "instrument": 0,
    "symbol": 1,
    "expiryDate": 2,
    "strikePrice": 3,
    "optionType": 4,
    "open": 5,
    "high": 6,
    "low": 7,
    "close": 8,
    "settlePrice": 9,
    "contracts": 10,
    "valueInLakhs": 11,
    "openInterest": 12,
    "changeInOpenInterest": 13,
    "timeStamp": 14
}

# BhavData Fields
stkOptDailyDataFields = {
    'date': 'date',
    'stkOptOpenPrice': 'stkOptOpenPrice',
    'stkOptHighPrice': 'stkOptHighPrice',
    'stkOptLowPrice': 'stkOptLowPrice',
    'stkOptClosePrice': 'stkOptClosePrice',
    'stkOptSettlePrice': 'stkOptSettlePrice',
    'stkOptContracts': 'stkOptContracts',
    'stkOptValueInLakhs': 'stkOptValueInLakhs',
    'stkOptOpenInterest': 'stkOptOpenInterest',
    'stkOptChangeInOpenInterest': 'stkOptChangeInOpenInterest'
}

stkFutDailyDataFields = {
    'date': 'date',
    'stkFutOpenPrice': 'stkFutOpenPrice',
    'stkFutHighPrice': 'stkFutHighPrice',
    'stkFutLowPrice': 'stkFutLowPrice',
    'stkFutClosePrice': 'stkFutClosePrice',
    'stkFutSettlePrice': 'stkFutSettlePrice',
    'stkFutContracts': 'stkFutContracts',
    'stkFutValueInLakhs': 'stkFutValueInLakhs',
    'stkFutOpenInterest': 'stkFutOpenInterest',
    'stkFutChangeInOpenInterest': 'stkFutChangeInOpenInterest'
}

idxOptDailyDataFields = {
    'date': 'date',
    'idxOptOpenPrice': 'idxOptOpenPrice',
    'idxOptHighPrice': 'idxOptHighPrice',
    'idxOptLowPrice': 'idxOptLowPrice',
    'idxOptClosePrice': 'idxOptClosePrice',
    'idxOptSettlePrice': 'idxOptSettlePrice',
    'idxOptContracts': 'idxOptContracts',
    'idxOptValueInLakhs': 'idxOptValueInLakhs',
    'idxOptOpenInterest': 'idxOptOpenInterest',
    'idxOptChangeInOpenInterest': 'idxOptChangeInOpenInterest'
}

idxFutDailyDataFields = {
    'date': 'date',
    'idxFutOpenPrice': 'idxFutOpenPrice',
    'idxFutHighPrice': 'idxFutHighPrice',
    'idxFutLowPrice': 'idxFutLowPrice',
    'idxFutClosePrice': 'idxFutClosePrice',
    'idxFutSettlePrice': 'idxFutSettlePrice',
    'idxFutContracts': 'idxFutContracts',
    'idxFutValueInLakhs': 'idxFutValueInLakhs',
    'idxFutOpenInterest': 'idxFutOpenInterest',
    'idxFutChangeInOpenInterest': 'idxFutChangeInOpenInterest'
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


# Get value from a single pandas dataframe cell
def getValueFromDFCell(cell):
    return cell.values[0]


def getColString(key, columnList):
    return columnList[FNO_COL_IDX[key]]


'''
# strptime = "string parse time"
# strftime = "string format time"

# Converting datetime.datetime to datetime.date
            d =  parser.parse(bd.strftime(utils.dateFormatString)).date()
'''


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
