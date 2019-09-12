import os

DB_HOST     = os.environ['MONGODB_HOST']
DB_PORT     = int(os.environ['MONGODB_PORT'])
DATABASE    = 'MasterStockData_DB'
COLLECTION  = 'StockBhavData_C'
TEMP_COLLECTION = 'Temp_C'

# File Directory path
BHAVDATA_DIRECTORY = "./data/cashData/bhavdata/"

# Archived File Directory path
ARCHIVED_BHAVDATA_DIRECTORY = "./data/cashData/archivedBhavdata/"
