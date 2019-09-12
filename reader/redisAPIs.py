import redis
import config

redis_server = redis.Redis(config.REDIS_HOST, config.REDIS_PORT)

def writeDataToRedis(key, data):
    redis_server.set(key, data)

def checkIfDataInRedis(key):
    return redis_server.exists(key)

def readDataFromRedis(key):
    return redis_server.get(key)

def deleteDataFromRedis(key):
    return redis_server.delete(key)

def persistRedis(name):
    redis_server.persist(name)


