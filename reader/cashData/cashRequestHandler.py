import json
from . import cashDbAPIs
from . import redisAPIs

class CashDataRequestHandlers:
    def __init__(self):
        self.cashDbAPIs = cashDbAPIs.CashDbAPIs()

    async def handler_cashSymbolList(self, request):
        '''
        Returns the list of symbols in cash market segment
        /api/{marketType}
        '''
        # FROM MongoDB SERVER
        #return await self.cashDbAPIs.getCashSymbolList()

        # FROM REDIS SERVER
        data = redisAPIs.readDataFromRedis('CASH_SYMBOLS')
        if data:
            return json.loads(redisAPIs.readDataFromRedis('CASH_SYMBOLS'))
        else:
            #return ('ERROR: CASH_SYMBOLS')
            return ([])

    async def handler_cashMarketData(self, request):
        '''
        Returns the details of a stock symbol
        /api/cash/data?symbol=sbin&startdate=5-jul-2019&enddate=15-jul-2019
        '''

        symbol      = str(request.rel_url.query.get('symbol')).upper()
        startDate   = request.rel_url.query.get('startdate')
        endDate     = request.rel_url.query.get('enddate')

        result = await self.cashDbAPIs.getCashData(symbol, startDate, endDate)

        return result
    

