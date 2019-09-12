import os

DB_HOST     = os.environ['MONGODB_HOST']
DB_PORT     = int(os.environ['MONGODB_PORT'])
DATABASE    = 'MasterStockData_DB'
COLLECTION  = 'IndicesData_C'
TEMP_COLLECTION = 'Temp_C'

# File Directory path
INDEXDATA_DIRECTORY = "./data/indexData/currentData/"

# Archived File Directory path
ARCHIVED_INDEXDATA_DIRECTORY = "./data/indexData/archivedData/"
