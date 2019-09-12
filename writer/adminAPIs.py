import os
import config

import cashData.writeAPIs as cashDataWriteAPIs
import fnoData.writeAPIs as fnoDataWriteAPIs
import indexData.writeAPIs as indexDataWriteAPIs

async def doAction(action, request):
    body = await request.json()

    if action == 'DELETE_DIR':
        dirType = body.get('dirType')

        if dirType == 'CASH_DATA_DIR':
            try:
                deleteDir = config.CASH_CSV_UPLOAD_PATH + '*'
                deleteCmd = 'rm -rf ' + deleteDir
                print('Delete command : ', deleteCmd)
                os.system(deleteCmd)
                return 'Completed'

            except Exception as e:
                return ('ERROR: Cannot clear Cash data directory on server')

        elif dirType == 'CASH_ARCHIVED_DATA_DIR':
            try:
                deleteDir = config.CASH_ARCHIVED_CSV_UPLOAD_PATH + '*'
                deleteCmd = 'rm -rf ' + deleteDir
                print('Delete command : ', deleteCmd)
                os.system(deleteCmd)
                return 'Completed'

            except Exception as e:
                return ('ERROR: Cannot clear Cash archived data directory on server')

        elif dirType == 'FNO_DATA_DIR':
            try:
                deleteDir = config.FNO_CSV_UPLOAD_PATH + '*'
                deleteCmd = 'rm -rf ' + deleteDir
                print('Delete command : ', deleteCmd)
                os.system(deleteCmd)
                return 'Completed'

            except Exception as e:
                return ('ERROR: Cannot clear FnO data directory on server')

        elif dirType == 'INDEX_DATA_DIR':
            try:
                deleteDir = config.INDEX_CSV_UPLOAD_PATH + '*'
                deleteCmd = 'rm -rf ' + deleteDir
                print('Delete command : ', deleteCmd)
                os.system(deleteCmd)
                return 'Completed'

            except Exception as e:
                return ('ERROR: Cannot clear Index data directory on server')

        elif dirType == 'INDEX_ARCHIVED_DATA_DIR':
            try:
                deleteDir = config.INDEX_ARCHIVED_CSV_UPLOAD_PATH + '*'
                deleteCmd = 'rm -rf ' + deleteDir
                print('Delete command : ', deleteCmd)
                os.system(deleteCmd)
                return 'Completed'

            except Exception as e:
                return ('ERROR: Cannot clear Index archived data directory on server')

        else:
            return ('ERROR : Invalid directory')

    elif action == 'LOAD_DATA':
        dataType = body.get('dataType')

        if dataType == 'CASH_DATA':
            print('Received: Load Cash Data request')
            result = await cashDataWriteAPIs.loadCashDataToDB(request)
            return result

        elif dataType == 'FNO_DATA':
            print('Received: Load FnO Data request')
            result = await fnoDataWriteAPIs.loadFnoDataToDB(request)
            return result

        elif dataType == 'INDEX_DATA':
            print('Received: Load Index Data request')
            result = await indexDataWriteAPIs.loadIndexDataToDB(request)
            return result

        else:
            return ('ERROR : Invalid upload data')

    elif action == 'DELETE_DATA':
        dataType = body.get('dataType')

        if dataType == 'CASH_DATA':
            pass

        elif dataType == 'STOCK_FNO_DATA':
            print('Received: Delete Stock FnO Data request')
            result = await fnoDataWriteAPIs.deleteStockFnoData(body)
            return result

        elif dataType == 'INDEX_FNO_DATA':
            print('Received: Delete Index FnO Data request')
            result = await fnoDataWriteAPIs.deleteIndexFnoData(body)
            return result

        elif dataType == 'INDEX_DATA':
            pass

        else:
            return ('ERROR : Invalid upload data')

    else:
        return ('ERROR : Invalid Action')


async def handleAdminRequest(request):
    returnData = {}
    try:
        body = await request.json()
        if body:
            params = {}
            params.update({
                'actions': body.get('actions')
            })

            print('action :>> ', params['actions'])

            for action in params['actions']:
                actionResult = await doAction(action, request)
                returnData.update({action: actionResult})
        else:
            returnData.update({'ERROR': 'Request Invalid'})
    except Exception as e:
        returnData.update({'ERROR': str(e)})
    return returnData