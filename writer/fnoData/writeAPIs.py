import asyncio
from . import fileUtils
from . import loadFnoDataFromCsv
from . import deleteFnoDataFromDB
from . import responses

async def loadDataFromCsv(checks):
    '''
    /api/write/fno/data?source=csv&checks=yes
    '''
    writeStatus = []
    fileList = fileUtils.getFilesNames()
    if fileList:
        for f in fileList:
            print()
            print('Reading File : ', f)
            # Load Individual files in DB one by one
            dataToLoad = loadFnoDataFromCsv.LoadFnoDataFromCsvToDB(f)

            print('     Loading FnO Data  from : ', f)
            if checks == 'yes':
                result = await asyncio.gather(dataToLoad.loadStkOptDataWithCheck(),
                                              dataToLoad.loadStkFutDataWithCheck(),
                                              dataToLoad.loadIdxOptDataWithCheck(),
                                              dataToLoad.loadIdxFutDataWithCheck())

                writeStatus.append(str(f) + ' :: ' + str(result[0]) + ' | ' + str(result[1]) + ' | ' + str(result[2]) + ' | ' + str(result[3]))


                '''
                e, u, s = await dataToLoad.loadStkOptDataWithCheck()
                print('Stock Option' ':: entry -> ', e, ' | update -> ', u, ' | skipped -> ', s)
                msg = 'Stock Option' + ' :: entry -> ' + str(e) + ' | update -> ' + str(u) + ' | skipped -> ' + str(s)
                writeStatus.append(msg)

                e, u, s = await dataToLoad.loadStkFutDataWithCheck()
                print('Stock Future' ':: entry -> ', e, ' | update -> ', u, ' | skipped -> ', s)
                msg = 'Stock Future' + ' :: entry -> ' + str(e) + ' | update -> ' + str(u) + ' | skipped -> ' + str(s)
                writeStatus.append(msg)

                e, u, s = await dataToLoad.loadIdxOptDataWithCheck()
                print('Index Option' ':: entry -> ', e, ' | update -> ', u, ' | skipped -> ', s)
                msg = 'Index Option' + ' :: entry -> ' + str(e) + ' | update -> ' + str(u) + ' | skipped -> ' + str(s)
                writeStatus.append(msg)

                e, u, s = await dataToLoad.loadIdxFutDataWithCheck()
                print('Index Future' ':: entry -> ', e, ' | update -> ', u, ' | skipped -> ', s)
                msg = 'Index Future' + ' :: entry -> ' + str(e) + ' | update -> ' + str(u) + ' | skipped -> ' + str(s)
                writeStatus.append(msg)
                '''
            else:
                result = await asyncio.gather(dataToLoad.loadStkOptDataWithoutCheck(),
                                              dataToLoad.loadStkFutDataWithoutCheck(),
                                              dataToLoad.loadIdxOptDataWithoutCheck(),
                                              dataToLoad.loadIdxFutDataWithoutCheck())

                writeStatus.append(str(f) + ' :: ' + str(result[0]) + ' | ' + str(result[1]) + ' | ' + str(result[2]) + ' | ' + str(result[3]))


                '''
                e, u, s = await dataToLoad.loadStkOptDataWithoutCheck()
                print('Stock Option' ':: entry -> ', e, ' | update -> ', u, ' | skipped -> ', s)
                msg = 'Stock Option' + ' :: entry -> ' + str(e) + ' | update -> ' + str(u) + ' | skipped -> ' + str(s)
                writeStatus.append(msg)

                e, u, s = await dataToLoad.loadStkFutDataWithoutCheck()
                print('Stock Future' ':: entry -> ', e, ' | update -> ', u, ' | skipped -> ', s)
                msg = 'Stock Future' + ' :: entry -> ' + str(e) + ' | update -> ' + str(u) + ' | skipped -> ' + str(s)
                writeStatus.append(msg)

                e, u, s = await dataToLoad.loadIdxOptDataWithoutCheck()
                print('Index Option' ':: entry -> ', e, ' | update -> ', u, ' | skipped -> ', s)
                msg = 'Index Option' + ' :: entry -> ' + str(e) + ' | update -> ' + str(u) + ' | skipped -> ' + str(s)
                writeStatus.append(msg)

                e, u, s = await dataToLoad.loadIdxFutDataWithoutCheck()
                print('Index Future' ':: entry -> ', e, ' | update -> ', u, ' | skipped -> ', s)
                msg = 'Index Future' + ' :: entry -> ' + str(e) + ' | update -> ' + str(u) + ' | skipped -> ' + str(s)
                writeStatus.append(msg)
                '''
    else:
        msg = 'NO Stock BhavData files to read. !!!'
        writeStatus.append(msg)
        print(msg)

    print(writeStatus)
    return writeStatus

async def loadFnoDataToDB(request):
    try:
        body = await request.json()
        if body:
            params = {}
            params.update({
                'source': body.get('source'),
                'checks': body.get('checks')
            })

            if params['source'] == 'csv':
                if not params['checks']:
                    params['checks'] = 'yes'
                status = await loadDataFromCsv(params['checks'])
                return status
            elif params['source'] == 'nsetools':
                pass
            else:
                return responses.errorMessage('Invalid Load params')

        else:
            return responses.errorMessage('Load Request Invalid')

    except Exception as e:
        return responses.errorMessage({'ERROR': str(e)})

async def deleteStockFnoData(body):
    try:
       expiryDate = body.get('expiryDate')
       dataToDelete = deleteFnoDataFromDB.DeleteFnoDataFromDB()
       stkOptstatus = await dataToDelete.deleteStkOptDataByExpDate(expiryDate)
       stkFutstatus = await dataToDelete.deleteStkFutDataByExpDate(expiryDate)

       return ('Status : ' + stkOptstatus + ' | ' + stkFutstatus)

    except Exception as e:
        return ('ERROR : %s' % str(e))

async def deleteIndexFnoData(body):
    try:
       expiryDate = body.get('expiryDate')
       dataToDelete = deleteFnoDataFromDB.DeleteFnoDataFromDB()
       idxOptstatus = await dataToDelete.deleteIdxOptDataByExpDate(expiryDate)
       idxFutstatus = await dataToDelete.deleteIdxFutDataByExpDate(expiryDate)

       return ('Status : ' + idxOptstatus + ' | ' + idxFutstatus)

    except Exception as e:
        return ('ERROR : %s' % str(e))
