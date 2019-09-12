import motor.motor_asyncio
from passlib.hash import sha256_crypt

from . import config

async def saveUserInfo(request):
    print('MONGODB_HOST : ', config.DB_HOST)
    print('MONGODB_PORT : ', config.DB_PORT)

    dbClient = motor.motor_asyncio.AsyncIOMotorClient(config.DB_HOST, config.DB_PORT)
    db = dbClient[config.DATABASE]
    userCollection = db[config.COLLECTION]

    #extract post data
    body = await request.json()
    if body:
        userParams = {}
        userParams.update({'username': body.get('username')})
        userParams.update({'password': body.get('password')})
        print(userParams)

        try:
            document = await userCollection.find_one({
                'username' : userParams['username']
            })

            if document:
                return ({'status': 'User already present'})
            else:
                passwordHash = sha256_crypt.hash(userParams['password'])
                result = await userCollection.insert_one({
                    'username'  : userParams['username'],
                    'password'  : passwordHash
                })
                return ({'status': 'pass'})

        except Exception as e:
            print('saveUserInfo () - ERROR: ', e)
    else:
        print('saveUserInfo() ERROR: Request Invalid')

