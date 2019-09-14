from aiohttp import web
import aiohttp_cors
import os

import config
import users.writeAPIs as userWriteAPIs
import adminRequestHandler as adminHandlers

adminReqHandlers = adminHandlers.AdminRequestHandler()


# USER LOGIN
async def handleUserSignInRequest(request):
    print('Recieved: User SignIn request')
    result = await userWriteAPIs.saveUserInfo(request)
    return web.json_response(result)

# ADMIN JOBS
async def handleAdminJobs(request):
    result = await adminReqHandlers.handler_adminRequest(request)
    return web.json_response(result)


# File Upload
async def handlerCashCSVFileUpload(request):
    print('Recieved: Cash CSV File Upload request')
    reader = await request.multipart()
    field = await reader.next()

    print('field: ', field)
    print('Recieved File field.name: ', field.name)

    try:
        size = 0
        with open(os.path.join(config.CASH_CSV_UPLOAD_PATH, field.name), 'wb') as f:
            while True:
                chunk = await field.read_chunk()
                if not chunk:
                    break
                size += len(chunk)
                f.write(chunk)
        return web.json_response('{} size of {} successfully stored'.format(field.name, size))

    except Exception as e:
        return web.json_response('Some error while storing Cash CSV File at server end')

async def handlerArchivedCashCSVFileUpload(request):
    print('Recieved: Archived Cash CSV File Upload request')
    reader = await request.multipart()
    field = await reader.next()

    print('field: ', field)
    print('Recieved File field.name: ', field.name)

    try:
        size = 0
        with open(os.path.join(config.CASH_ARCHIVED_CSV_UPLOAD_PATH, field.name), 'wb') as f:
            while True:
                chunk = await field.read_chunk()
                if not chunk:
                    break
                size += len(chunk)
                f.write(chunk)
        return web.json_response('{} size of {} successfully stored'.format(field.name, size))

    except Exception as e:
        return web.json_response('Some error while storing Archived Cash CSV File at server end')

async def handlerFnOCSVFileUpload(request):
    print('Recieved: FnO CSV File Upload request')
    reader = await request.multipart()
    field = await reader.next()

    print('field: ', field)
    print('Recieved File field.name: ', field.name)

    try :
        size = 0
        with open(os.path.join(config.FNO_CSV_UPLOAD_PATH, field.name), 'wb') as f:
            while True:
                chunk = await field.read_chunk()
                if not chunk:
                    break
                size += len(chunk)
                f.write(chunk)
        return web.json_response('{} size of {} successfully stored'.format(field.name, size))

    except Exception as e:
        return web.json_response('Some error while storing FnO file at server end')

async def handlerIndexCSVFileUpload(request):
    print('Recieved: Index CSV File Upload request')
    reader = await request.multipart()
    field = await reader.next()

    print('field: ', field)
    print('Recieved File field.name: ', field.name)

    try :
        size = 0
        with open(os.path.join(config.INDEX_CSV_UPLOAD_PATH, field.name), 'wb') as f:
            while True:
                chunk = await field.read_chunk()
                if not chunk:
                    break
                size += len(chunk)
                f.write(chunk)
        return web.json_response('{} size of {} successfully stored'.format(field.name, size))

    except Exception as e:
        return web.json_response('Some error while storing Index CSV File at server end')

async def handlerArchivedIndexCSVFileUpload(request):
    print('Recieved: Archived Index CSV File Upload request')
    reader = await request.multipart()
    field = await reader.next()

    print('field: ', field)
    print('Recieved File field.name: ', field.name)

    try :
        size = 0
        with open(os.path.join(config.INDEX_ARCHIVED_CSV_UPLOAD_PATH, field.name), 'wb') as f:
            while True:
                chunk = await field.read_chunk()
                if not chunk:
                    break
                size += len(chunk)
                f.write(chunk)
        return web.json_response('{} size of {} successfully stored'.format(field.name, size))

    except Exception as e:
        return web.json_response('Some error while storing Archived Index CSV File at server end')

#################################################################################

# For Debugging purposes
async def handleTestRequest(request):
    return web.json_response("Hello form Write Server!!")

#################################################################################

# Create a Application instance
app = web.Application()

############################### CORS Handling ###################################

cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
})

signin_resource = cors.add(app.router.add_resource("/write/signin"))
cors.add(signin_resource.add_route("POST", handleUserSignInRequest))

admin_resource = cors.add(app.router.add_resource("/write/api/admin"))
cors.add(admin_resource.add_route("POST", handleAdminJobs))

uploadCashCsv_resource = cors.add(app.router.add_resource("/write/api/admin/upload/cashcsv"))
cors.add(uploadCashCsv_resource.add_route("POST", handlerCashCSVFileUpload))

uploadArchivedCashCsv_resource = cors.add(app.router.add_resource("/write/api/admin/upload/archivedcashcsv"))
cors.add(uploadArchivedCashCsv_resource.add_route("POST", handlerArchivedCashCSVFileUpload))

uploadFnOCsv_resource = cors.add(app.router.add_resource("/write/api/admin/upload/fnocsv"))
cors.add(uploadFnOCsv_resource.add_route("POST", handlerFnOCSVFileUpload))

uploadIndexCsv_resource = cors.add(app.router.add_resource("/write/api/admin/upload/indexcsv"))
cors.add(uploadIndexCsv_resource.add_route("POST", handlerIndexCSVFileUpload))

uploadArchivedIndexCsv_resource = cors.add(app.router.add_resource("/write/api/admin/upload/archivedindexcsv"))
cors.add(uploadArchivedIndexCsv_resource.add_route("POST", handlerArchivedIndexCSVFileUpload))

# For Debugging -----------
test_resource = cors.add(app.router.add_resource("/write/test"))
cors.add(test_resource.add_route("GET", handleTestRequest))

#########################################################################
if __name__ == '__main__':
    # web.run_app(app, host=config.HOST, port=config.PORT)
    print('HOST : ', os.environ['WRITE_SERVER_HOST'])
    print('PORT : ', int(os.environ['WRITE_SERVER_PORT']))

    #web.run_app(app, host=os.environ['HOST'], port=config.PORT)
    web.run_app(app, host=os.environ['WRITE_SERVER_HOST'], port=int(os.environ['WRITE_SERVER_PORT']))

