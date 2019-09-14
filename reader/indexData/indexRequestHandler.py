import json
from . import indexDbAPIs
from . import redisAPIs

class IndexDataRequestHandlers:
    def __init__(self):
        self.indexDbAPIs = indexDbAPIs.IndexDbAPIs()

    async def handler_indexSymbolList(self, request):
        '''
        Returns the list of symbols in cash market segment
        /api/{marketType}
        '''
        # FROM MongoDB SERVER
        #return await self.indexDbAPIs.getIndexSymbolList()

        # FROM REDIS SERVER
        data = redisAPIs.readDataFromRedis('INDEX_SYMBOLS')
        if data:
            return json.loads(redisAPIs.readDataFromRedis('INDEX_SYMBOLS'))
        else:
            #return json.loads({'ERROR' : 'Redis data needs to be built'})
            #return ('ERROR: FNOIDX_SYMBOLS')
            return ([])

    async def handler_indexMarketData(self, request):
        '''
        Returns the details of a stock symbol
        /api/cash/data?symbol=Nifty 50&startdate=5-jul-2019&enddate=15-jul-2019
        '''

        symbol      = request.rel_url.query.get('symbol') # Symbol is Case sensititve in this case
        startDate   = request.rel_url.query.get('startdate')
        endDate     = request.rel_url.query.get('enddate')

        result = await self.indexDbAPIs.getIndexMarketData(symbol, startDate, endDate)

        return result