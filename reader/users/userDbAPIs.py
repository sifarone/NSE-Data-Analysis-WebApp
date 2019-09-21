import datetime
import motor.motor_asyncio
from passlib.hash import sha256_crypt

from . import config
from . import responses

class UserDbAPIs:
    def __init__(self):
        print('MONGODB_HOST : ', config.DB_HOST)
        print('MONGODB_PORT : ', config.DB_PORT)

        self.dbClient = motor.motor_asyncio.AsyncIOMotorClient(config.DB_HOST, config.DB_PORT)
        self.db = self.dbClient[config.DATABASE]
        self.collection = self.db[config.COLLECTION]

    async def getUserData(self, userName, password):
        try:
            # Async DB Lookup
            document = await self.collection.find_one({'username': userName})
            authStatus = False
            if document:
                print('User found in database')
                dbPassword = document['password']
                authStatus = sha256_crypt.verify(password, dbPassword)
                print('User Authentication status : ', authStatus)

            if authStatus:
                print('documnet : ', document['usertype'])
                return ({'status': document['usertype']})
                #return ({'status': 'pass'})
            else:
                return ({'status': 'fail'})

        except Exception as e:
            # Return an error message
            print(e)
            return responses.errorMessage('Server Login error!!')