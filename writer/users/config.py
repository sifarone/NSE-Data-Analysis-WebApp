import os

DB_HOST     = os.environ['MONGODB_HOST']
DB_PORT     = int(os.environ['MONGODB_PORT'])

DATABASE    = 'MasterStockData_DB'
COLLECTION  = 'UserData_C'
