import asyncio

import chartsUtils as utils

import cashData.cashDbAPIs as cashDbAPIs
import fnoData.stkOptDbAPIs as stkOptDbAPIs
import fnoData.stkFutDbAPIs as stkFutDbAPIs
import fnoData.idxOptDbAPIs as idxOptDbAPIs
import fnoData.idxFutDbAPIs as idxFutDbAPIs
import indexData.indexDbAPIs as indexDbAPIs

# This function fetches the data from the source based on the type of chart requested
async def getData(params, source): #3
    if source == 'cash':
       data = await cashDbAPIs.CashDbAPIs().getCashData(params['symbol'], params['startDate'], params['date'])
       return data

    elif source == 'call_stkOptByDate':

        expDate = utils.convertStringToDatetime(params['stkOptExpiryDate'])
        dd = utils.convertStringToDatetime(params['date'])
        data = await stkOptDbAPIs.StkOptDbAPIs().getStkOptDataForADate(params['symbol'], expDate, 'CE', dd)
        return data

    elif source == 'put_stkOptByDate':
        expDate = utils.convertStringToDatetime(params['stkOptExpiryDate'])
        dd = utils.convertStringToDatetime(params['date'])
        data = await stkOptDbAPIs.StkOptDbAPIs().getStkOptDataForADate(params['symbol'], expDate, 'PE', dd)
        return data

    elif source == 'put_stkOptOIvsDeltaOI':
        # convert dates from string to date types
        expDate = utils.convertStringToDatetime(params['stkOptExpiryDate'])
        dd = utils.convertStringToDatetime(params['date'])
        data = await stkOptDbAPIs.StkOptDbAPIs().getStrikePricePutCallDetailsForADate(params['symbol'], expDate, dd)
        return data['PE']

    elif source == 'call_stkOptOIvsDeltaOI':
        # convert dates from string to datetime types
        expDate = utils.convertStringToDatetime(params['stkOptExpiryDate'])
        dd = utils.convertStringToDatetime(params['date'])
        data = await stkOptDbAPIs.StkOptDbAPIs().getStrikePricePutCallDetailsForADate(params['symbol'], expDate, dd)
        return data['CE']

    elif source == 'stkFutByExpiryDate':
        expDate = utils.convertStringToDatetime(params['stkFutExpiryDate'])
        data = await stkFutDbAPIs.StkFutDbAPIs().getStkFutDataForAExpiryMonth(params['symbol'], expDate)
        return data

    elif source == 'idxOpt':
        pass

    elif source == 'put_idxOptOIvsDeltaOI':
        # convert dates from string to date types
        expDate = utils.convertStringToDatetime(params['idxOptExpiryDate'])
        dd = utils.convertStringToDatetime(params['date'])
        data = await idxOptDbAPIs.IdxOptDbAPIs().getStrikePricePutCallDetailsForADate(params['symbol'], expDate, dd)
        return data['PE']

    elif source == 'call_idxOptOIvsDeltaOI':
        # convert dates from string to datetime types
        expDate = utils.convertStringToDatetime(params['idxOptExpiryDate'])
        dd = utils.convertStringToDatetime(params['date'])
        data = await idxOptDbAPIs.IdxOptDbAPIs().getStrikePricePutCallDetailsForADate(params['symbol'], expDate, dd)
        return data['CE']

    elif source == 'idxFutByExpiryDate':
        expDate = utils.convertStringToDatetime(params['idxFutExpiryDate'])
        #print('1 --> ExpiryDate : ', expDate)
        data = await idxFutDbAPIs.IdxFutDbAPIs().getIdxFutDataForAExpiryMonth(params['symbol'], expDate)
        return data

    elif source == 'index':
        pass

    elif source == 'cashStkFutStkOptCE':
        #print('In cashStkFutStkOptCE params[strikePrice] : ', params['strikePrice'])
        dateDict = await stkOptDbAPIs.StkOptDbAPIs().getFirstDateForAStrikePriceInAllExpiryMonth(params['symbol'], params['strikePrice'])
        #print('1==>> dateDict : ', dateDict)
        stDate = dateDict[params['stkOptExpiryDate']] # assuming opt and fut have same dates
        #print('1==>> stDate : ', type(stDate))

        cashData = await cashDbAPIs.CashDbAPIs().getCashData(params['symbol'], stDate)
        #print('1==>> cashData : ', cashData)
        del cashData['date']


        expDate = utils.convertStringToDatetime(params['stkFutExpiryDate'])
        futData = await stkFutDbAPIs.StkFutDbAPIs().getStkFutDataForAExpiryMonth(params['symbol'], expDate)
        #print('1==>> futData : ', futData)
        del futData['date']
        #print('1==>> futData : ', futData)

        optData = await stkOptDbAPIs.StkOptDbAPIs().getStkOptStrikePriceData(params['symbol'], expDate, params['strikePrice'])
        #del optData['CE']['date']
        #print('1==>> optData[CE] : ', optData['CE'])

        combinedDataSource = {**cashData, **futData, **optData['CE']}

        #print('1combinedDataSource : ', combinedDataSource)

        return combinedDataSource

    elif source == 'cashStkFutStkOptPE':
        #print('In cashStkFutStkOptPE')
        dateDict = await stkOptDbAPIs.StkOptDbAPIs().getFirstDateForAStrikePriceInAllExpiryMonth(params['symbol'],
                                                                                                 params['strikePrice'])
        #print('==>> dateDict : ', dateDict)
        stDate = dateDict[params['stkOptExpiryDate']]  # assuming opt and fut have same dates
        #print('==>> stDate : ', type(stDate))

        cashData = await cashDbAPIs.CashDbAPIs().getCashData(params['symbol'], stDate)
        del cashData['date']
        #print('==>> cashData : ', cashData)

        expDate = utils.convertStringToDatetime(params['stkFutExpiryDate'])
        futData = await stkFutDbAPIs.StkFutDbAPIs().getStkFutDataForAExpiryMonth(params['symbol'], expDate)
        del futData['date']
        #print('==>> futData : ', futData)

        optData = await stkOptDbAPIs.StkOptDbAPIs().getStkOptStrikePriceData(params['symbol'], expDate,
                                                                             params['strikePrice'])
        #del optData['PE']['date']
        #print('==>> optData[CE] : ', optData['CE'])

        combinedDataSource = {**cashData, **futData, **optData['PE']}

        #print('combinedDataSource : ', combinedDataSource)

        return combinedDataSource

    elif source == 'stock_optionChain':
        returnData = {}
        expDate = utils.convertStringToDatetime(params['stkOptExpiryDate'])
        dt = utils.convertStringToDatetime(params['date'])
        symbol, info, callOptChainData = await stkOptDbAPIs.StkOptDbAPIs().getStkOptDataForADate(params['symbol'], expDate, 'CE', dt)
        symbol, info, putOptChainData = await stkOptDbAPIs.StkOptDbAPIs().getStkOptDataForADate(params['symbol'], expDate, 'PE', dt)
        returnData.update({
            'CE' : callOptChainData,
            'PE' : putOptChainData
        })
        return returnData

    elif source == 'index_optionChain':
        returnData = {}
        expDate = utils.convertStringToDatetime(params['idxOptExpiryDate'])
        dt = utils.convertStringToDatetime(params['date'])
        symbol, info, callOptChainData = await idxOptDbAPIs.IdxOptDbAPIs().getIdxOptDataForADate(params['symbol'], expDate, 'CE', dt)
        symbol, info, putOptChainData = await idxOptDbAPIs.IdxOptDbAPIs().getIdxOptDataForADate(params['symbol'], expDate, 'PE', dt)
        returnData.update({
            'CE' : callOptChainData,
            'PE' : putOptChainData
        })
        return returnData

    elif source == 'analytics':
        pass

    else:
        print('Something is not write with charts!!')

async def getDataFromSources(params, chart): #2
    sourceList  = chart['sourceList']
    aggregatedData = {}
    for source in sourceList:
        data = await getData(params, source)
        fields = chart[source]
        if fields:
            for field in fields:
                #print('+++ ', data)
                aggregatedData.update({field:data[field]})
        else:
            # in case there are no fields requested in the POST request
            aggregatedData = data
    #print('***** aggregatedData :',aggregatedData)
    return aggregatedData


async def getChartsData(request): #1
    returnData = {}
    try:
        body = await request.json()
        if body:
            params = {}
            params.update({
                'symbol'                : str(body.get('symbol')).upper(),
                'startDate'             : body.get('startDate'),
                'stkOptExpiryDate'      : body.get('stkOptExpiryDate'),
                'stkFutExpiryDate'      : body.get('stkFutExpiryDate'),
                'idxOptExpiryDate'      : body.get('idxOptExpiryDate'),
                'idxFutExpiryDate'      : body.get('idxFutExpiryDate'),
                'strikePrice'           : int(body.get('strikePrice')),
                #'optionType'           : body.get('optionType'),
                'date'                  : body.get('date')
            })

            charts  = body.get('charts')
            for chart in charts:
                chartData = await getDataFromSources(params, body.get(chart))
                returnData.update({chart : chartData})
        else:
            returnData.update({'ERROR' : 'Request Invalid'})
    except Exception as e:
        returnData.update({'ERROR': str(e)})
    return returnData

