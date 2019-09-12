from dateutil import parser

# Date formater string
dateFormatString = "%d-%b-%Y"


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