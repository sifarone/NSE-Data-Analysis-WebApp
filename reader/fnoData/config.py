import os

DB_HOST     = os.environ['MONGODB_HOST']
DB_PORT     = int(os.environ['MONGODB_PORT'])

REDIS_HOST  = os.environ['REDIS_HOST']
REDIS_PORT  = int(os.environ['REDIS_PORT'])

DATABASE    = 'MasterStockData_DB'

STKOPT_COLLECTION = 'StockOptionsData_C'
STKFUT_COLLECTION = 'StockFuturesData_C'
IDXOPT_COLLECTION = 'IndexOptionsData_C'
IDXFUT_COLLECTION = 'IndexFuturesData_C'
