
from . import fileUtils
from . import loadCashDataFromCsv
from . import loadCashDataFromNseTools
from . import responses

async def loadDataFromCsv(checks):
    '''
    /api/write/cash/data?source=csv&checks=yes
    '''
    writeStatus = []
    fileList = fileUtils.getFilesNames()
    if fileList:
        for f in fileList:
            print()
            # Load Individual files in DB one by one
            dataToLoad = loadCashDataFromCsv.LoadBhavDataFromCsvToDB(f)
            print('     Loading Stock bhavData :')
            if checks == 'yes':
                e, u, s = await dataToLoad.loadDataWithCheck()
            else:
                e, u, s = await dataToLoad.loadDataWithoutCheck()
            print('         >> BhavData :: entry -> ', e, ' | update -> ', u, ' | skipped -> ',s)
            msg = str(f)  + ' :: entry -> ' + str(e) +  ' | update -> '+ str(u) + ' | skipped -> ' + str(s)
            writeStatus.append(msg)
    else:
        msg = 'NO Stock BhavData files to read. !!!'
        writeStatus.append(msg)
        print(msg)

    return writeStatus

async def loadArchivedDataFromCsv(checks):
    '''
    /api/write/cash/data?source=csv&checks=yes
    '''
    writeStatus = []
    fileList = fileUtils.getArchivedFilesNames()
    if fileList:
        for f in fileList:
            print()
            # Load Individual files in DB one by one
            dataToLoad = loadCashDataFromCsv.LoadArchivedBhavDataFromCsvToDB(f)
            print('     Loading Archived Stock BhavData :')
            if checks == 'yes':
                e, u, s = await dataToLoad.loadDataWithCheck()
            else:
                e, u, s = await dataToLoad.loadDataWithoutCheck()
            print('         >> BhavData :: entry -> ', e, ' | update -> ', u, ' | skipped -> ',s)
            msg = str(f)  + ' :: entry -> ' + str(e) +  ' | update -> '+ str(u) + ' | skipped -> ' + str(s)
            writeStatus.append(msg)
    else:
        msg = 'NO Stock BhavData files to read. !!!'
        writeStatus.append(msg)
        print(msg)

    return writeStatus

async def loadDataFromNseTools():
    '''
    /api/write/cash/data?source=nsetools
    '''
    writeStatus = []
    e, u, s = await loadCashDataFromNseTools.LoadCashDataFromNseTools().loadBhavdataToDB()
    print('BhavData :: entry -> ', e, ' | update -> ', u, ' | skipped -> ', s)
    msg = 'BhavData :: entry -> ' + str(e) + ' | update -> ' + str(u) + ' | skipped -> ' + str(s)
    writeStatus.append(msg)

    return writeStatus

async def loadCashDataToDB(request):
    try:
        body = await request.json()
        if body:
            params = {}
            params.update({
                'source'    : body.get('source'),
                'checks'    : body.get('checks')
            })

            if params['source'] == 'csv':
                if not params['checks']:
                    params['checks'] = 'yes'
                status = await loadDataFromCsv(params['checks'])
                return status

            elif params['source'] == 'archivedCsv':
                if not params['checks']:
                    params['checks'] = 'yes'
                status = await loadArchivedDataFromCsv(params['checks'])
                return status

            elif params['source'] == 'nsetools':
                status = await loadDataFromNseTools()
                return status
            else:
                return responses.errorMessage('Invalid Load params')

        else:
            return responses.errorMessage('Load Request Invalid')

    except Exception as e:
        return responses.errorMessage({'ERROR': str(e)})