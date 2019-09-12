import os

DB_HOST     = os.environ['MONGODB_HOST']
DB_PORT     = int(os.environ['MONGODB_PORT'])
DATABASE    = 'MasterStockData_DB'

STKOPT_COLLECTION = 'StockOptionsData_C'
STKFUT_COLLECTION = 'StockFuturesData_C'
IDXOPT_COLLECTION = 'IndexOptionsData_C'
IDXFUT_COLLECTION = 'IndexFuturesData_C'

#COLLECTION = 'Temp_C'

# File Directory path
DAILYDATA_DIRECTORY = "./data/fnoData/"

