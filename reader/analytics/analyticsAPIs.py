
def calculateEMA(period, data):
    returnData = {}
    emaList = []
    key = 'ema' + str(period)
    if data:
        historicalEma = data[0]
        e = 2/(period + 1)
        for i in range(len(data)):
            ema = (data[i] - historicalEma) * e + historicalEma
            historicalEma = ema
            emaList.append(ema)
        returnData.update({key : emaList})
    else:
        returnData.update({key:[]})

    return returnData

def calculateNBFilter(period=4, fields=[], data ={}):
    pass
