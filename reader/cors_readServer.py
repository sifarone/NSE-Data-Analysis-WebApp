from aiohttp import web
import aiohttp_cors
import os

import config
import responses
import cashData.cashRequestHandler as cashHandlers
import fnoData.fnoRequestHandler as fnoHandlers
import indexData.indexRequestHandler as indexHandlers
import chartsRequestHandler as chartsHandlers
import adminRequestHandler as adminHandlers
import users.userRequestHandler as userHandlers

cashReqHandlers     = cashHandlers.CashDataRequestHandlers()
fnoReqHandlers      = fnoHandlers.FnoDataRequestHandlers()
indexReqHandlers    = indexHandlers.IndexDataRequestHandlers()
chartsReqHandlers   = chartsHandlers.ChartsRequestHandler()
adminReqHandlers    = adminHandlers.AdminRequestHandler()
userReqHandlers     = userHandlers.UserRequestHandler()


async def handleSymbolListRequest(request):

    marketType = request.match_info['marketType'].lower()

    if marketType == 'cash':
        # Return the list of cash symbols
        result = await cashReqHandlers.handler_cashSymbolList(request)
        return web.json_response(result)

    elif marketType == 'fnostock':
        # Return the list of fno stock symbols
        result = await fnoReqHandlers.handler_fnoStkSymbolList(request)
        return web.json_response(result)

    elif marketType == 'fnoindex':
        # Return the list of fno index symbols
        result = await fnoReqHandlers.handler_fnoIdxSymbolList(request)
        return web.json_response(result)

    elif marketType == 'index':
        # Return the list of indices:
        result = await indexReqHandlers.handler_indexSymbolList(request)
        return web.json_response(result)

    else:
        # Return an error message
        return responses.errorMessage('Wrong Choice')

async def handleCashMarketDataRequest(request):
    result = await cashReqHandlers.handler_cashMarketData(request)
    #print('handleCashMarketDataRequest: ', result)
    return web.json_response(result)

#-----------------------------------------------------------------------------------

async def handleStkOptDataRequest(request):
    result = await fnoReqHandlers.handler_stkOptData(request)
    return web.json_response(result)

async def handleStkOptInfoRequest(request):
    result = await fnoReqHandlers.handler_stkOptInfo(request)
    return web.json_response(result)

#-----------------------------------------------------------------------------------

async def handleStkFutDataRequest(request):
    result = await fnoReqHandlers.handler_stkFutData(request)
    return web.json_response(result)

async def handleStkFutInfoRequest(request):
    result = await fnoReqHandlers.handler_stkFutInfo(request)
    return web.json_response(result)

#-----------------------------------------------------------------------------------

async def handleIdxOptDataRequest(request):
    result = await fnoReqHandlers.handler_idxOptData(request)
    return web.json_response(result)

async def handleIdxOptInfoRequest(request):
    result = await fnoReqHandlers.handler_idxOptInfo(request)
    return web.json_response(result)

#-----------------------------------------------------------------------------------

async def handleIdxFutDataRequest(request):
    result = await fnoReqHandlers.handler_idxFutData(request)
    return web.json_response(result)

async def handleIdxFutInfoRequest(request):
    result = await fnoReqHandlers.handler_idxFutInfo(request)
    return web.json_response(result)

#-----------------------------------------------------------------------------------

async def handleIndexMarketDataRequest(request):
    result = await indexReqHandlers.handler_indexMarketData(request)
    return web.json_response(result)

#-----------------------------------------------------------------------------------

# CHARTS & ANALYTICS
async def handleChartDataRequest(request):
    print('Chart Data Request recieved ------>  ')
    result = await chartsReqHandlers.handler_charts(request)
    #print('handleChartDataRequest ---> : ', result)
    return web.json_response(result)

#-----------------------------------------------------------------------------------

# ADMIN FUNCTIONS
async def handleAdminRequest(request):
    print('DEBUG: recieved a Admin request')
    result = await adminReqHandlers.handler_adminRequest(request)
    return web.json_response(result)

#-----------------------------------------------------------------------------------

# User Login
async def handleUserLogin(request):
    result = await userReqHandlers.handler_userLogin(request)
    return web.json_response(result)

##################################################################################

# For Debugging purposes
async def handlePostTestRequest(request):
    body = await request.json()

    '''
    name = body['name']
    age = body['age']
    data = body['data']
    '''

    name  = body.get('name')
    age   = body.get('age')
    data  = body.get('data')

    print(name, age, data)
    return web.json_response("Post Data reveived")

#################################################################################

# For Debugging purposes
async def handleTestRequest(request):
    return web.json_response("Hello form Read Server!!")

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

marketType_resource = cors.add(app.router.add_resource("/read/api/{marketType}"))
cors.add(marketType_resource.add_route("GET", handleSymbolListRequest))

cashData_resource = cors.add(app.router.add_resource("/read/api/cash/data"))
cors.add(cashData_resource.add_route("GET", handleCashMarketDataRequest))

stkOptData_resource = cors.add(app.router.add_resource("/read/api/fno/stkopt/data"))
cors.add(stkOptData_resource.add_route("GET", handleStkOptDataRequest))

stkOptInfo_resource = cors.add(app.router.add_resource("/read/api/fno/stkopt/info"))
cors.add(stkOptInfo_resource.add_route("GET", handleStkOptInfoRequest))

stkFutData_resource = cors.add(app.router.add_resource("/read/api/fno/stkfut/data"))
cors.add(stkFutData_resource.add_route("GET", handleStkFutDataRequest))

stkFutInfo_resource = cors.add(app.router.add_resource("/read/api/fno/stkfut/info"))
cors.add(stkFutInfo_resource.add_route("GET", handleStkFutInfoRequest))

idxOptData_resource = cors.add(app.router.add_resource("/read/api/fno/idxopt/data"))
cors.add(idxOptData_resource.add_route("GET", handleIdxOptDataRequest))

idxOptInfo_resource = cors.add(app.router.add_resource("/read/api/fno/idxopt/info"))
cors.add(idxOptInfo_resource.add_route("GET", handleIdxOptInfoRequest))

idxFutData_resource = cors.add(app.router.add_resource("/read/api/fno/idxfut/data"))
cors.add(idxFutData_resource.add_route("GET", handleIdxFutDataRequest))

idxFutInfo_resource = cors.add(app.router.add_resource("/read/api/fno/idxfut/info"))
cors.add(idxFutInfo_resource.add_route("GET", handleIdxFutInfoRequest))

indexData_resource = cors.add(app.router.add_resource("/read/api/index/data"))
cors.add(indexData_resource.add_route("GET", handleIndexMarketDataRequest))

charting_resource = cors.add(app.router.add_resource("/read/api/post/charting"))
cors.add(charting_resource.add_route("POST", handleChartDataRequest))

admin_resource = cors.add(app.router.add_resource("/read/api/admin"))
cors.add(admin_resource.add_route("POST", handleAdminRequest))

login_resource = cors.add(app.router.add_resource("/read/login"))
cors.add(login_resource.add_route("POST", handleUserLogin))

# For Debugging -----------
test_resource = cors.add(app.router.add_resource("/read/test"))
cors.add(test_resource.add_route("GET", handleTestRequest))

#########################################################################
if __name__ == '__main__':
    #web.run_app(app, host=config.HOST, port=config.PORT)
    print('HOST : ', os.environ['READ_SERVER_HOST'])
    print('PORT : ', int(os.environ['READ_SERVER_PORT']))

    #web.run_app(app, host=os.environ['HOST'], port=config.PORT)
    web.run_app(app, host=os.environ['READ_SERVER_HOST'], port=int(os.environ['READ_SERVER_PORT']))