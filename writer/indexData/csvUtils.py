import pandas as pd
from . import indexUtils as utils

class ReadConsolidatedIndicesCSV:
    def __init__(self, fileName):
        self.df = pd.read_csv(fileName)
        self.columns = self.df.columns

    def getCSVColumnList(self):
        return self.columns

    def getConsolidatedIndicesFlatData(self):
        '''
        Returns a list of following dictionary corresponding to each row in the csv file
        [
            {
                indexName       : ,
                date            : ,
                openValue       : ,
                highValue       : ,
                lowValue        : ,
                closingValue    : ,
                pointsChange    : ,
                percentChange   : ,
                volume          : ,
                turnover        : ,
                peRatio         : ,
                pbRatio         : ,
                divYield        :
            },
            {},
            {},
            .
            .
            .
        ]
        '''
        # Nested function
        def getDictFromRows(r):
            rowDict = {
                'indexName'                 : r[self.columns[utils.INDICES_COL_IDX['indexName']]],
                'date'                      : r[self.columns[utils.INDICES_COL_IDX['date']]],
                'openValue'                 : r[self.columns[utils.INDICES_COL_IDX['openValue']]],
                'highValue'                 : r[self.columns[utils.INDICES_COL_IDX['highValue']]],
                'lowValue'                  : r[self.columns[utils.INDICES_COL_IDX['lowValue']]],
                'closingValue'              : r[self.columns[utils.INDICES_COL_IDX['closingValue']]],
                'pointsChange'              : r[self.columns[utils.INDICES_COL_IDX['pointsChange']]],
                'percentChange'             : r[self.columns[utils.INDICES_COL_IDX['percentChange']]],
                'volume'                    : r[self.columns[utils.INDICES_COL_IDX['volume']]],
                'turnover'                  : r[self.columns[utils.INDICES_COL_IDX['turnover']]],
                'peRatio'                   : r[self.columns[utils.INDICES_COL_IDX['peRatio']]],
                'pbRatio'                   : r[self.columns[utils.INDICES_COL_IDX['pbRatio']]],
                'divYield'                  : r[self.columns[utils.INDICES_COL_IDX['divYield']]]
            }
            return rowDict

        returnList = []
        for index, row in self.df.iterrows():
            rowDict = getDictFromRows(row)
            returnList.append(rowDict)

        return returnList

class ReadArchivedIndexCSV:
    def __init__(self, fileName):
        self.df = pd.read_csv(fileName)
        self.columns = self.df.columns

    def getCSVColumnList(self):
        return self.columns

    def getArchivedIndicesFlatData(self):
        '''
        Returns a list of following dictionary corresponding to each row in the csv file
        [
            {
                indexName       : ,
                date            : ,
                openValue       : ,
                highValue       : ,
                lowValue        : ,
                closingValue    : ,
                peRatio         : ,
                pbRatio         : ,
                divYield        :
            },
            {},
            {},
            .
            .
            .
        ]
        '''
        # Nested function
        def getDictFromRows(r):
            rowDict = {
                'indexName'                     : r[self.columns[utils.STOCK_ARCHIVED_COL_IDX['indexName']]],
                'date'                          : r[self.columns[utils.STOCK_ARCHIVED_COL_IDX['date']]],
                'openValue'                     : r[self.columns[utils.STOCK_ARCHIVED_COL_IDX['openValue']]],
                'highValue'                     : r[self.columns[utils.STOCK_ARCHIVED_COL_IDX['highValue']]],
                'lowValue'                      : r[self.columns[utils.STOCK_ARCHIVED_COL_IDX['lowValue']]],
                'closingValue'                  : r[self.columns[utils.STOCK_ARCHIVED_COL_IDX['closingValue']]],
                'peRatio'                       : r[self.columns[utils.STOCK_ARCHIVED_COL_IDX['peRatio']]],
                'pbRatio'                       : r[self.columns[utils.STOCK_ARCHIVED_COL_IDX['pbRatio']]],
                'divYield'                      : r[self.columns[utils.STOCK_ARCHIVED_COL_IDX['divYield']]]
            }
            return rowDict

        returnList = []
        for index, row in self.df.iterrows():
            rowDict = getDictFromRows(row)
            returnList.append(rowDict)

        return returnList