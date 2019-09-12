import motor.motor_asyncio
from dateutil import parser

from . import config
from . import fnoUtils as utils

class DeleteFnoDataFromDB:
    def __init__(self):
        self.dbClient = motor.motor_asyncio.AsyncIOMotorClient(config.DB_HOST, config.DB_PORT)
        self.db = self.dbClient[config.DATABASE]
        self.stkOptCollection = self.db[config.STKOPT_COLLECTION]
        self.stkFutCollection = self.db[config.STKFUT_COLLECTION]
        self.idxOptCollection = self.db[config.IDXOPT_COLLECTION]
        self.idxFutCollection = self.db[config.IDXFUT_COLLECTION]

    # DATA DELETION --------------------------------------------------------------------
    async def deleteStkOptDataByExpDate(self, expiryDate):
        try:
            print('deleteStkOptDataByExpDate: ', utils.convertStringToDatetime(expiryDate))
            expDate = utils.convertStringToDatetime(expiryDate)
            n1 = await self.stkOptCollection.count_documents({})
            print('deleteStkOptDataByExpDate: documents before deletion : ', n1)
            result = await self.stkOptCollection.delete_many({'expiryDate': expDate})
            n2 = await self.stkOptCollection.count_documents({})
            print('deleteStkOptDataByExpDate: documents after deletion : ', n2)
            return ('StkOpt Records Deleted : ' + str(n1-n2))

        except Exception as e:
            print('deleteStkOptDataByExpDate () : Fatal Error : ', e)
            return ('ERROR : error while deletion.')

    async def deleteStkFutDataByExpDate(self, expiryDate):
        try:
            print('deleteStkFutDataByExpDate: ', utils.convertStringToDatetime(expiryDate))
            expDate = utils.convertStringToDatetime(expiryDate)
            n1 = await self.stkFutCollection.count_documents({})
            print('deleteStkFutDataByExpDate: documents before deletion : ', n1)
            result = await self.stkFutCollection.delete_many({'expiryDate': expDate})
            n2 = await self.stkFutCollection.count_documents({})
            print('deleteStkFutDataByExpDate: documents after deletion : ', n2)
            return ('StkFut Records Deleted : ' + str(n1-n2))

        except Exception as e:
            print('deleteStkFutDataByExpDate () : Fatal Error : ', e)
            return ('ERROR : error while deletion.')

    async def deleteIdxOptDataByExpDate(self, expiryDate):
        try:
            print('deleteIdxOptDataByExpDate: ', utils.convertStringToDatetime(expiryDate))
            expDate = utils.convertStringToDatetime(expiryDate)
            n1 = await self.idxOptCollection.count_documents({})
            print('deleteIdxOptDataByExpDate: documents before deletion : ', n1)
            result = await self.idxOptCollection.delete_many({'expiryDate': expDate})
            n2 = await self.idxOptCollection.count_documents({})
            print('deleteIdxOptDataByExpDate: documents after deletion : ', n2)
            return ('IdxOpt Records Deleted : ' + str(n1-n2))

        except Exception as e:
            print('deleteStkOptDataByExpDate () : Fatal Error : ', e)
            return ('ERROR : error while deletion.')

    async def deleteIdxFutDataByExpDate(self, expiryDate):
        try:
            print('deleteIdxFutDataByExpDate: ', utils.convertStringToDatetime(expiryDate))
            expDate = utils.convertStringToDatetime(expiryDate)
            n1 = await self.idxFutCollection.count_documents({})
            print('deleteIdxFutDataByExpDate: documents before deletion : ', n1)
            result = await self.idxFutCollection.delete_many({'expiryDate': expDate})
            n2 = await self.idxFutCollection.count_documents({})
            print('deleteIdxFutDataByExpDate: documents after deletion : ', n2)
            return ('IdxFut Records Deleted : ' + str(n1-n2))

        except Exception as e:
            print('deleteIdxFutDataByExpDate () : Fatal Error : ', e)
            return ('ERROR : error while deletion.')