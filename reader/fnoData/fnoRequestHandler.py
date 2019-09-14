import json
from . import stkOptDbAPIs
from . import stkFutDbAPIs
from . import idxOptDbAPIs
from . import idxFutDbAPIs
from . import fnoUtils as utils
from . import redisAPIs

class FnoDataRequestHandlers:
    def __init__(self):
        self.stkOptDbAPIs = stkOptDbAPIs.StkOptDbAPIs()
        self.stkFutDbAPIs = stkFutDbAPIs.StkFutDbAPIs()
        self.idxOptDbAPIs = idxOptDbAPIs.IdxOptDbAPIs()
        self.idxFutDbAPIs = idxFutDbAPIs.IdxFutDbAPIs()

    async def handler_fnoStkSymbolList(self, request):
        # FROM MongoDB SERVER
        #return await self.stkOptDbAPIs.getFnOSymbolList()

        # FROM REDIS SERVER
        data = redisAPIs.readDataFromRedis('FNOSTK_SYMBOLS')
        if data:
            return json.loads(redisAPIs.readDataFromRedis('FNOSTK_SYMBOLS'))
        else:
            #return json.loads({'ERROR' : 'Redis data needs to be built'})
            #return ('ERROR: FNOSTK_SYMBOLS')
            return ([])

    async def handler_fnoIdxSymbolList(self, request):
        # FROM MongoDB SERVER
        #return await self.stkOptDbAPIs.getFnOSymbolList()

        # FROM REDIS SERVER
        data = redisAPIs.readDataFromRedis('FNOIDX_SYMBOLS')
        if data:
            return json.loads(redisAPIs.readDataFromRedis('FNOIDX_SYMBOLS'))
        else:
            #return json.loads({'ERROR' : 'Redis data needs to be built'})
            #return ('ERROR: FNOSTK_SYMBOLS')
            return ([])

    ###### STOCK OPTION REQUEST HANDLERS ######
    async def handler_stkOptData(self, request):

        symbol      = str(request.rel_url.query.get('symbol')).upper()
        expiryDate  = request.rel_url.query.get('expirydate')
        strikePrice = request.rel_url.query.get('strikeprice')
        optionType  = str(request.rel_url.query.get('optiontype')).upper()
        date        = request.rel_url.query.get('date')

        if date:
            d = utils.convertStringToDate(date)
            expDate = utils.convertStringToDatetime(expiryDate)  # <------------- TBD fix this while writing to DB
            # Return stock Option details for a particular date
            s, info, data = await self.stkOptDbAPIs.getStkOptDataForADate(symbol, expDate, optionType, d)
            return {'symbol': s,
                    'info'  : info,
                    'data'  : data}

        s, info, data = await self.stkOptDbAPIs.getStkOptData(symbol)
        return {'symbol': s,
                'info'  : info,
                'data'  : data}

    # FROM REDIS SERVER
    async def handler_stkOptInfo(self, request):
        #return await self.stkOptDbAPIs.getInfoForAllStkOptSymbols()
        data = redisAPIs.readDataFromRedis('INFO_STKOPT')
        if data:
            return json.loads(redisAPIs.readDataFromRedis('INFO_STKOPT'))
        else:
            #return json.loads({'ERROR' : 'Redis data needs to be built'})
            return ('ERROR: INFO_STKOPT')

    ###### STOCK FUTURE REQUEST HANDLERS ######
    async def handler_stkFutData(self, request):
        symbol      = str(request.rel_url.query.get('symbol')).upper()
        expiryDate  = request.rel_url.query.get('expirydate')
        date        = request.rel_url.query.get('date')

        if date:
            d = utils.convertStringToDate(date)
            expDate = utils.convertStringToDatetime(expiryDate)  # <------------- TBD fix this while writing to DB
            # Return stock future details for a particular date
            pass

        s, info, data = await self.stkFutDbAPIs.getStkFutData(symbol)
        return {'symbol': s,
                'info'  : info,
                'data'  : data}

    # FROM REDIS SERVER
    async def handler_stkFutInfo(self, request):
        # return await self.stkOptDbAPIs.getInfoForAllStkOptSymbols()
        data = redisAPIs.readDataFromRedis('INFO_STKFUT')
        if data:
            return json.loads(redisAPIs.readDataFromRedis('INFO_STKFUT'))
        else:
            #return json.loads({'ERROR' : 'Redis data needs to be built'})
            return ('ERROR: INFO_STKFUT')

    ###### INDEX OPTION REQUEST HANDLERS ######
    async def handler_idxOptData(self, request):
        symbol       = str(request.rel_url.query.get('symbol')).upper()
        expiryDate   = request.rel_url.query.get('expirydate')
        strikePrice  = request.rel_url.query.get('strikeprice')
        optionType   = str(request.rel_url.query.get('optiontype')).upper()
        date         = request.rel_url.query.get('date')

        if date:
            d = utils.convertStringToDate(date)
            expDate = utils.convertStringToDatetime(expiryDate)  # <------------- TBD fix this while writing to DB
            # Return stock Option details for a particular date
            s, info, data = await self.idxOptDbAPIs.getIdxOptDataForADate(symbol, expDate, optionType, d)
            return {'symbol': s,
                    'info'  : info,
                    'data'  : data}

        s, info, data = await self.idxOptDbAPIs.getIdxOptData(symbol)
        return {'symbol': s,
                'info'  : info,
                'data'  : data}

    # FROM REDIS SERVER
    async def handler_idxOptInfo(self, request):
        # return await self.stkOptDbAPIs.getInfoForAllStkOptSymbols()
        data = redisAPIs.readDataFromRedis('INFO_IDXOPT')
        if data:
            return json.loads(redisAPIs.readDataFromRedis('INFO_IDXOPT'))
        else:
            #return json.loads({'ERROR' : 'Redis data needs to be built'})
            return ('ERROR: INFO_IDXOPT')

    ###### INDEX FUTURE REQUEST HANDLERS ######
    async def handler_idxFutData(self, request):
        symbol      = str(request.rel_url.query.get('symbol')).upper()
        expiryDate  = request.rel_url.query.get('expirydate')
        date        = request.rel_url.query.get('date')

        if date:
            d = utils.convertStringToDate(date)
            expDate = utils.convertStringToDatetime(expiryDate)  # <------------- TBD fix this while writing to DB
            # Return stock future details for a particular date
            pass

        s, info, data = await self.idxFutDbAPIs.getIdxFutData(symbol)
        return {'symbol': s,
                'info'  : info,
                'data'  : data}

    # FROM REDIS SERVER
    async def handler_idxFutInfo(self, request):
        # return await self.stkOptDbAPIs.getInfoForAllStkOptSymbols()
        data = redisAPIs.readDataFromRedis('INFO_IDXFUT')
        if data:
            return json.loads(redisAPIs.readDataFromRedis('INFO_IDXFUT'))
        else:
            #return json.loads({'ERROR' : 'Redis data needs to be built'})
            return ('ERROR: INFO_IDXFUT')