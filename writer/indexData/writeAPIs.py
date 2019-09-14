
from . import fileUtils
from . import loadIndexDataFromCsv
from . import responses

async def loadDataFromCsv(checks):
    writeStatus = []
    fileList = fileUtils.getFilesNames()
    if fileList:
        for f in fileList:
            print()
            # Load Individual files in DB one by one
            dataToLoad = loadIndexDataFromCsv.LoadIndexDataFromCsv(f)
            print('     Loading Index dailyData :')
            if checks == 'yes':
                e, u, s = await dataToLoad.loadDataWithCheck()
            else:
                e, u, s = await dataToLoad.loadDataWithoutCheck()
            print('         >> DailyData :: entry -> ', e, ' | update -> ', u, ' | skipped -> ', s)
            msg = str(f) + ' :: entry -> ' + str(e) + ' | update -> ' + str(u) + ' | skipped -> ' + str(s)
            writeStatus.append(msg)
    else:
        msg = 'NO Index Data files to read. !!!'
        writeStatus.append(msg)
        print(msg)

    return writeStatus

async def loadArchivedDataFromCsv(checks):
    writeStatus = []
    fileList = fileUtils.getArchivedFilesNames()
    if fileList:
        for f in fileList:
            print()
            # Load Individual files in DB one by one
            dataToLoad = loadIndexDataFromCsv.LoadArchivedIndexDataFromCsv(f)
            print('     Loading Archived Index dailyData :')
            if checks == 'yes':
                e, u, s = await dataToLoad.loadDataWithCheck()
            else:
                e, u, s = await dataToLoad.loadDataWithoutCheck()
            print('         >> DailyData :: entry -> ', e, ' | update -> ', u, ' | skipped -> ',s)
            msg = str(f)  + ' :: entry -> ' + str(e) +  ' | update -> '+ str(u) + ' | skipped -> ' + str(s)
            writeStatus.append(msg)
    else:
        msg = 'NO Archived Index Data files to read. !!!'
        writeStatus.append(msg)
        print(msg)

    return writeStatus

async def loadIndexDataToDB(request):
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

            elif params['source'] == 'archivedCsv':
                if not params['checks']:
                    params['checks'] = 'yes'
                status = await loadArchivedDataFromCsv(params['checks'])
                return status

            elif params['source'] == 'nsetools':
                pass
            else:
                return responses.errorMessage('Invalid Load params')

        else:
            return responses.errorMessage('Load Request Invalid')

    except Exception as e:
        return responses.errorMessage({'ERROR': str(e)})


    '''
    source = request.rel_url.query.get('source')
    if source == 'csv':
        checks = request.rel_url.query.get('checks')
        if not checks:
            checks = 'yes'
        status = await loadDataFromCsv(checks)
        return status
    elif source == 'nsetools':
        pass
    else:
        return responses.errorMessage('Load Request Invalid')
    '''