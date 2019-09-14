from aiohttp import web
import os

import config
import responses
import cashData.writeAPIs as cashDataWriteAPIs
import fnoData.writeAPIs as fnoDataWriteAPIs
import indexData.writeAPIs as indexDataWriteAPIs
import users.writeAPIs as userWriteAPIs

# Initialize a route table
routes = web.RouteTableDef()

@routes.post('/api/write/cash/data')
async def handleCashMarketDataRequest(request):
    print('Recieved: Load Cash Data request')
    result = await cashDataWriteAPIs.loadCashDataToDB(request)
    return web.json_response(result)

@routes.post('/api/write/fno/data')
async def handleFnOMarketDataRequest(request):
    print('Recieved: Load FnO Data request')
    result = await fnoDataWriteAPIs.loadFnoDataToDB(request)
    return web.json_response(result)

@routes.post('/api/write/index/data')
async def handleIndexMarketDataRequest(request):
    print('Recieved: Load Index Data request')
    result = await indexDataWriteAPIs.loadIndexDataToDB(request)
    return web.json_response(result)

# USER LOGIN
@routes.post('/signin')
async def handleUserSignInRequest(request):
    print('Recieved: User SignIn request')
    result = await userWriteAPIs.saveUserInfo(request)
    return web.json_response(result)


# Create a Application instance
app = web.Application()

# Add all the routes to the web app
app.add_routes(routes)

if __name__ == '__main__':
    #web.run_app(app, host=config.HOST, port=config.PORT)
    web.run_app(app, host=os.environ['HOST'], port=50000)

