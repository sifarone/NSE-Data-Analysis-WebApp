
import chartsDataAPIs

class ChartsRequestHandler:
    def __init__(self):
        pass

    async def handler_charts(self, request):
        return await chartsDataAPIs.getChartsData(request)