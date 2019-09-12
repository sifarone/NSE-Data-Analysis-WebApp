import json

import redisAPIs

import cashData.cashDbAPIs as cashDbAPIs
import fnoData.stkOptDbAPIs as stkOptDbAPIs
import fnoData.stkFutDbAPIs as stkFutDbAPIs
import fnoData.idxOptDbAPIs as idxOptDbAPIs
import fnoData.idxFutDbAPIs as idxFutDbAPIs
import indexData.indexDbAPIs as indexDbAPIs

async def doAction(action, params):
    # TBD : use asyncio.gather()

    if action == 'CASH_SYMBOLS': #INFO_CASH
        cashSymbols = await cashDbAPIs.CashDbAPIs().getCashSymbolList()
        #print('cashSymbols : ', cashSymbols)
        redisAPIs.deleteDataFromRedis('CASH_SYMBOLS')
        redisAPIs.writeDataToRedis("CASH_SYMBOLS", json.dumps(cashSymbols))
        return 'Completed'

    elif action == 'FNOSTK_SYMBOLS':
        fnoStkSymbols = await stkOptDbAPIs.StkOptDbAPIs().getFnOSymbolList()
        #print('fnoStkSymbols : ', fnoStkSymbols)
        redisAPIs.deleteDataFromRedis('FNOSTK_SYMBOLS')
        redisAPIs.writeDataToRedis("FNOSTK_SYMBOLS", json.dumps(fnoStkSymbols))
        return 'Completed'

    elif action == 'FNOIDX_SYMBOLS':
        fnoIdxSymbols = await idxOptDbAPIs.IdxOptDbAPIs().getIdxOptSymbolList()
        #print('fnoIdxSymbols : ', fnoIdxSymbols)
        redisAPIs.deleteDataFromRedis('FNOIDX_SYMBOLS')
        redisAPIs.writeDataToRedis("FNOIDX_SYMBOLS", json.dumps(fnoIdxSymbols))
        return 'Completed'

    elif action == 'INDEX_SYMBOLS':
        idxSymbols = await indexDbAPIs.IndexDbAPIs().getIndexSymbolList()
        #print('idxSymbols : ', idxSymbols)
        redisAPIs.deleteDataFromRedis('INDEX_SYMBOLS')
        redisAPIs.writeDataToRedis("INDEX_SYMBOLS", json.dumps(idxSymbols))
        return 'Completed'

    elif action == 'INFO_STKOPT':
        infoStkOpt = await stkOptDbAPIs.StkOptDbAPIs().getInfoForAllStkOptSymbols()
        #print('infoStkOpt : ', infoStkOpt)
        redisAPIs.deleteDataFromRedis('INFO_STKOPT')
        redisAPIs.writeDataToRedis("INFO_STKOPT", json.dumps(infoStkOpt))
        return 'Completed'

    elif action == 'INFO_STKFUT':
        infoStkFut = await stkFutDbAPIs.StkFutDbAPIs().getInfoForAllStkFutSymbols()
        #print('infoStkFut : ', infoStkFut)
        redisAPIs.deleteDataFromRedis('INFO_STKFUT')
        redisAPIs.writeDataToRedis("INFO_STKFUT", json.dumps(infoStkFut))
        return 'Completed'

    elif action == 'INFO_IDXOPT':
        infoIdxOpt = await idxOptDbAPIs.IdxOptDbAPIs().getInfoForAllIdxOptSymbols()
        #print('infoIdxOpt : ', infoIdxOpt)
        redisAPIs.deleteDataFromRedis('INFO_IDXOPT')
        redisAPIs.writeDataToRedis("INFO_IDXOPT", json.dumps(infoIdxOpt))
        return 'Completed'

    elif action == 'INFO_IDXFUT':
        infoIdxFut = await idxFutDbAPIs.IdxFutDbAPIs().getInfoForAllIdxFutSymbols()
        #print('infoIdxFut : ', infoIdxFut)
        redisAPIs.deleteDataFromRedis('INFO_IDXFUT')
        redisAPIs.writeDataToRedis("INFO_IDXFUT", json.dumps(infoIdxFut))
        return 'Completed'


    else:
        return 'Invalid Action'

async def handleAdminRequest(request):
    returnData = {}
    try:
        body = await request.json()
        if body:
            params = {}
            params.update({
                'actions': body.get('actions')
            })

            print('action list :--> ', str(body.get('actions')).upper())
            print('action :>> ', params['actions'])

            for action in params['actions']:
                print(action, ' -> Running')
                actionResult = await doAction(action, params)
                print(action, ' : ', actionResult)
                returnData.update({action: actionResult})
        else:
            returnData.update({'ERROR': 'Request Invalid'})
    except Exception as e:
        returnData.update({'ERROR': str(e)})

    print(returnData)
    return returnData

'''
async def initInfoData():
    returnData = {}
    actions = [
                "CASH_SYMBOLS",
                "FNOSTK_SYMBOLS",
                "FNOIDX_SYMBOLS",
                "INFO_STKOPT",
                "INFO_STKFUT",
                "INFO_IDXOPT",
                "INFO_IDXFUT"
                ]
    for action in actions:
        print('initInfoData() : action : ', action)
        actionResult = await doAction(action, '')
        returnData.update({action: actionResult})

    return returnData
'''