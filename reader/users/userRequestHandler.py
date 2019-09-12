from . import userDbAPIs

class UserRequestHandler:
    def __init__(self):
        pass

    async def handler_userLogin(self, request):
        try:
            body = await request.json()

            if body:
                userName = body.get('username')
                password = body.get('password')

                return await userDbAPIs.UserDbAPIs().getUserData(userName, password)
            else:
                return ({'status': 'Request Invalid'})

        except Exception as e:
            print('handler_userLogin() ERROR : ', e)
            return ({'status': e})
