
import adminAPIs

class AdminRequestHandler:
    def __init__(self):
        pass

    async def handler_adminRequest(self, request):
        return await adminAPIs.handleAdminRequest(request)