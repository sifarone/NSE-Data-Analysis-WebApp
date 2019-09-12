import asyncio

import chartsUtils as utils

import cashData.cashDbAPIs as cashDbAPIs
import fnoData.stkOptDbAPIs as stkOptDbAPIs
import fnoData.stkFutDbAPIs as stkFutDbAPIs
import fnoData.idxOptDbAPIs as idxOptDbAPIs
import fnoData.idxFutDbAPIs as idxFutDbAPIs
import indexData.indexDbAPIs as indexDbAPIs

async def getData(params, source): #3
    if source == 'cash':
       data = await cashDbAPIs.CashDbAPIs().getCashData(params['symbol'], params['startDate'], params['date'])
       return data
    elif source == 'stkOpt':
        data = await stkOptDbAPIs.StkOptDbAPIs().getStkOptData(params['symbol'], params['stkOptExpiryDate'])
        return data
    elif source == 'stkFut':
        pass
    elif source == 'idxOpt':
        pass
    elif source == 'idxFut':
        pass
    elif source == 'index':
        pass
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
    elif source == 'put_idxOptOIvsDeltaOI':
        # convert dates from string to date types
        expDate = utils.convertStringToDatetime(params['idxOptExpiryDate'])
        dd = utils.convertStringToDatetime(params['date'])
        data = await idxOptDbAPIs.IdxOptDbAPIs().getStrikePricePutCallDetailsForADate(params['symbol'], expDate, dd)
        print('=== ', data)
        return data['PE']
    elif source == 'call_idxOptOIvsDeltaOI':
        # convert dates from string to datetime types
        expDate = utils.convertStringToDatetime(params['idxOptExpiryDate'])
        dd = utils.convertStringToDatetime(params['date'])
        data = await idxOptDbAPIs.IdxOptDbAPIs().getStrikePricePutCallDetailsForADate(params['symbol'], expDate, dd)
        return data['CE']
    elif source == 'analytics':
        pass
    else:
        print('Something is not write with charts!!')

async def gatherData(params, source):
    dataSources = {}
    if source == 'cash':
       data = await cashDbAPIs.CashDbAPIs().getCashData(params['symbol'], params['startDate'], params['date'])
       return data
    elif source == 'stkOpt':
        data = await stkOptDbAPIs.StkOptDbAPIs().getStkOptData(params['symbol'], params['stkOptExpiryDate'])
        return data
    elif source == 'stkFut':
        pass
    elif source == 'idxOpt':
        pass
    elif source == 'idxFut':
        pass
    elif source == 'index':
        pass
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
    elif source == 'put_idxOptOIvsDeltaOI':
        # convert dates from string to date types
        expDate = utils.convertStringToDatetime(params['idxOptExpiryDate'])
        dd = utils.convertStringToDatetime(params['date'])
        data = await idxOptDbAPIs.IdxOptDbAPIs().getStrikePricePutCallDetailsForADate(params['symbol'], expDate, dd)
        print('=== ', data)
        return data['PE']
    elif source == 'call_idxOptOIvsDeltaOI':
        # convert dates from string to datetime types
        expDate = utils.convertStringToDatetime(params['idxOptExpiryDate'])
        dd = utils.convertStringToDatetime(params['date'])
        data = await idxOptDbAPIs.IdxOptDbAPIs().getStrikePricePutCallDetailsForADate(params['symbol'], expDate, dd)
        return data['CE']
    elif source == 'analytics':
        pass
    else:
        print('Something is not write with charts!!')


async def getDataFromSources(params, chart): #2
    sourceList  = chart['sourceList']
    aggregatedData = {}
    for source in sourceList:
        #data = await getData(params, source)
        dataSources = await gatherData(params, source)
        fields = chart[source]
        for field in fields:
            print('+++ ', data)
            aggregatedData.update({field:data[field]})
    print('***** ',aggregatedData)
    return aggregatedData


async def getChartsData(request): #1
    returnData = {}
    body = await request.json()
    if body:
        params = {}
        params.update({
            'symbol'                : body.get('symbol'),
            'startDate'             : body.get('startDate'),
            'stkOptExpiryDate'      : body.get('stkOptExpiryDate'),
            'idxOptExpiryDate'      : body.get('idxOptExpiryDate'),
            'strikePrice'           : body.get('strikePrice'),
            #'optionType'    : body.get('optionType'),
            'date'                  : body.get('date')
        })

        charts  = body.get('charts')
        for chart in charts:
            chartData = await getDataFromSources(params, body.get(chart))
            returnData.update({chart : chartData})
    else:
        returnData.update({'ERROR' : ''})

    return returnData

