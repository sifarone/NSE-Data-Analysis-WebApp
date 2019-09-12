import pandas as pd
from . import cashUtils as utils


class ReadStockBhavDataCSV:
    def __init__(self, fileName):
        self.df = pd.read_csv(fileName)
        self.columns = self.df.columns

    def getCSVColumnList(self):
        return self.columns

    def getStockFlatData(self):
        '''
        Returns a list of following dictionary corresponding to each row in the csv file
        [
            {
                symbol          : ,
                date            : ,
                prevClose       : ,
                openPrice       : ,
                highPrice       : ,
                lowPrice        : ,
                lastPrice       : ,
                closePrice      : ,
                avgPrice        : ,
                ttlTrdQtnty     : ,
                turnoverLacs    : ,
                noOfTrades      : ,
                delivQty        : ,
                delivPer        :
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
                'symbol'        : r[self.columns[utils.STOCK_COL_IDX['symbol']]],
                'date'          : r[self.columns[utils.STOCK_COL_IDX['date']]],
                'prevClose'     : r[self.columns[utils.STOCK_COL_IDX['prevClose']]],
                'openPrice'     : r[self.columns[utils.STOCK_COL_IDX['openPrice']]],
                'highPrice'     : r[self.columns[utils.STOCK_COL_IDX['highPrice']]],
                'lowPrice'      : r[self.columns[utils.STOCK_COL_IDX['lowPrice']]],
                'lastPrice'     : r[self.columns[utils.STOCK_COL_IDX['lastPrice']]],
                'closePrice'    : r[self.columns[utils.STOCK_COL_IDX['closePrice']]],
                'avgPrice'      : r[self.columns[utils.STOCK_COL_IDX['avgPrice']]],
                'ttlTrdQtnty'   : r[self.columns[utils.STOCK_COL_IDX['ttlTrdQtnty']]],
                'turnoverLacs'  : r[self.columns[utils.STOCK_COL_IDX['turnoverLacs']]],
                'noOfTrades'    : r[self.columns[utils.STOCK_COL_IDX['noOfTrades']]],
                'delivQty'      : r[self.columns[utils.STOCK_COL_IDX['delivQty']]],
                'delivPer'      : r[self.columns[utils.STOCK_COL_IDX['delivPer']]]
            }
            return rowDict

        returnList = []
        for index, row in self.df.iterrows():
            rowDict = getDictFromRows(row)
            returnList.append(rowDict)

        return returnList


class ReadArchivedStockBhavDataCSV:
    def __init__(self, fileName):
        self.df = pd.read_csv(fileName)
        self.columns = self.df.columns

    def getCSVColumnList(self):
        return self.columns

    def getStockFlatData(self):
        '''
        Returns a list of following dictionary corresponding to each row in the csv file
        [
            {
                symbol          : ,
                openPrice       : ,
                highPrice       : ,
                lowPrice        : ,
                closePrice      : ,
                lastPrice       : ,
                prevClose       : ,
                date            :
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
                'symbol'        : r[self.columns[utils.STOCK_ARCHIVED_COL_IDX['symbol']]],
                'date'          : r[self.columns[utils.STOCK_ARCHIVED_COL_IDX['date']]],
                'prevClose'     : r[self.columns[utils.STOCK_ARCHIVED_COL_IDX['prevClose']]],
                'openPrice'     : r[self.columns[utils.STOCK_ARCHIVED_COL_IDX['openPrice']]],
                'highPrice'     : r[self.columns[utils.STOCK_ARCHIVED_COL_IDX['highPrice']]],
                'lowPrice'      : r[self.columns[utils.STOCK_ARCHIVED_COL_IDX['lowPrice']]],
                'lastPrice'     : r[self.columns[utils.STOCK_ARCHIVED_COL_IDX['lastPrice']]],
                'closePrice'    : r[self.columns[utils.STOCK_ARCHIVED_COL_IDX['closePrice']]]
            }
            return rowDict

        returnList = []
        for index, row in self.df.iterrows():
            rowDict = getDictFromRows(row)
            returnList.append(rowDict)

        return returnList

