import os

DB_HOST     = os.environ['MONGODB_HOST']
DB_PORT     = int(os.environ['MONGODB_PORT'])

REDIS_HOST  = os.environ['REDIS_HOST']
REDIS_PORT  = int(os.environ['REDIS_PORT'])

DATABASE    = 'MasterStockData_DB'
COLLECTION  = 'StockBhavData_C'
