import json
import datetime
from dateutil import parser

def myConverter(date):
    if isinstance(date, datetime.datetime) or isinstance(date, datetime.date):
        return date.__str__()

def toJSON(data):
    return json.dumps(data , default=myConverter)

def toJSON2(data):
    return json.dumps(json.JSONDecoder().decode(data))

def fromJSON(data):
    return json.loads(data)


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