from aiohttp import web
import os

import config
import responses
import cashData.cashRequestHandler as cashHandlers
import fnoData.fnoRequestHandler as fnoHandlers
import indexData.indexRequestHandler as indexHandlers
import chartsRequestHandler as chartsHandlers
import adminRequestHandler as adminHandlers
import users.userRequestHandler as userHandlers



cashReqHandlers    = cashHandlers.CashDataRequestHandlers()
fnoReqHandlers     = fnoHandlers.FnoDataRequestHandlers()
indexReqHandlers   = indexHandlers.IndexDataRequestHandlers()
chartsReqHandlers  = chartsHandlers.ChartsRequestHandler()
adminReqHandlers   = adminHandlers.AdminRequestHandler()
userReqHandlers    = userHandlers.UserRequestHandler()


# Initialize a route table
routes = web.RouteTableDef()

@routes.get('/api/{marketType}')
async def handleSymbolListRequest(request):

    marketType = request.match_info['marketType'].lower()

    if marketType == 'cash':
        # Return the list of cash symbols
        result = await cashReqHandlers.handler_cashSymbolList(request)
        return web.json_response(result)

    elif marketType == 'fno':
        # Return the list of fno symbols
        result = await fnoReqHandlers.handler_fnoSymbolList(request)
        return web.json_response(result)

    elif marketType == 'index':
        # Return the list of indices:
        result = await indexReqHandlers.handler_indexSymbolList(request)
        return web.json_response(result)

    else:
        # Return an error message
        return responses.errorMessage('Wrong Choice')

@routes.get('/api/cash/data')
async def handleCashMarketDataRequest(request):
    result = await cashReqHandlers.handler_cashMarketData(request)
    #print('handleCashMarketDataRequest: ', result)
    return web.json_response(result)

#-----------------------------------------------------------------------------------

@routes.get('/api/fno/stkopt/data')
async def handleStkOptDataRequest(request):
    result = await fnoReqHandlers.handler_stkOptData(request)
    return web.json_response(result)

@routes.get('/api/fno/stkopt/info')
async def handleStkOptInfoRequest(request):
    result = await fnoReqHandlers.handler_stkOptInfo(request)
    return web.json_response(result)

#-----------------------------------------------------------------------------------

@routes.get('/api/fno/stkfut/data')
async def handleStkFutDataRequest(request):
    result = await fnoReqHandlers.handler_stkFutData(request)
    return web.json_response(result)

@routes.get('/api/fno/stkfut/info')
async def handleStkFutInfoRequest(request):
    result = await fnoReqHandlers.handler_stkFutInfo(request)
    return web.json_response(result)

#-----------------------------------------------------------------------------------

@routes.get('/api/fno/idxopt/data')
async def handleIdxOptDataRequest(request):
    result = await fnoReqHandlers.handler_idxOptData(request)
    return web.json_response(result)

@routes.get('/api/fno/idxopt/info')
async def handleIdxOptInfoRequest(request):
    result = await fnoReqHandlers.handler_idxOptInfo(request)
    return web.json_response(result)

#-----------------------------------------------------------------------------------

@routes.get('/api/fno/idxfut/data')
async def handleIdxFutDataRequest(request):
    result = await fnoReqHandlers.handler_idxFutData(request)
    return web.json_response(result)

@routes.get('/api/fno/idxfut/info')
async def handleIdxFutInfoRequest(request):
    result = await fnoReqHandlers.handler_idxFutInfo(request)
    return web.json_response(result)

#-----------------------------------------------------------------------------------

@routes.get('/api/index/data')
async def handleIndexMarketDataRequest(request):
    result = await indexReqHandlers.handler_indexMarketData(request)
    return web.json_response(result)

#-----------------------------------------------------------------------------------

# CHARTS & ANALYTICS
@routes.post('/api/post/charting')
async def handleChartDataRequest(request):
    result = await chartsReqHandlers.handler_charts(request)
    #print('handleChartDataRequest ---> : ', result)
    return web.json_response(result)

#-----------------------------------------------------------------------------------

# ADMIN FUNCTIONS
@routes.post('/api/admin')
async def handleAdminRequest(request):
    result = await adminReqHandlers.handler_adminRequest(request)
    return web.json_response(result)

#-----------------------------------------------------------------------------------

# User Login
@routes.post('/login')
async def handleUserLogin(request):
    result = await userReqHandlers.handler_userLogin(request)
    return web.json_response(result)

#########################################################################
@routes.post('/api/post/test')
async def handlePostTestRequest(request):
    body = await request.json()

    '''
    name = body['name']
    age = body['age']
    data = body['data']
    '''

    name    = body.get('name')
    age     = body.get('age')
    data    = body.get('data')

    print(name, age, data)
    return web.json_response("Post Data reveived")

#########################################################################

# Create a Application instance
app = web.Application()

# Add all the routes to the web app
app.add_routes(routes)

if __name__ == '__main__':
    #web.run_app(app, host=config.HOST, port=config.PORT)
    web.run_app(app, host=os.environ['HOST'], port=config.PORT)