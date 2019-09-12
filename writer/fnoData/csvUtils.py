import pandas as pd
from . import fnoUtils as utils

# import utils

'''
['INSTRUMENT', 'SYMBOL', 'EXPIRY_DT', 'STRIKE_PR', 'OPTION_TYP', 'OPEN',
 'HIGH', 'LOW', 'CLOSE', 'SETTLE_PR', 'CONTRACTS', 'VAL_INLAKH', 'OPEN_INT', 'CHG_IN_OI', 'TIMESTAMP']
 '''


class ReadFnOCSV:
    def __init__(self, fileName):
        self.df = pd.read_csv(fileName)
        self.columns = list(self.df.columns.values)
        # print(self.columns)
        if len(self.columns) > utils.NO_OF_COULMNS:
            # print('No. of coulms is > 15')
            # Drop the last coulmn with garbage data
            self.df = self.df.drop(columns=[self.columns[len(self.columns) - 1]])
            # Remove the extra column from columns list
            self.columns = self.columns[:-1]
        self.date = list(set(self.df[self.columns[utils.FNO_COL_IDX['timeStamp']]]))[0]

        # INSTRUMENT DATAFRAME
        # dataframe for only index futures
        self.idxFutDf = self.df.loc[
            self.df[self.columns[utils.FNO_COL_IDX['instrument']]] == utils.instruments['indexFutures']]
        # dataframe for only index options
        self.idxOptDf = self.df.loc[
            self.df[self.columns[utils.FNO_COL_IDX['instrument']]] == utils.instruments['indexOptions']]
        # dataframe for only stock futures
        self.stkFutDf = self.df.loc[
            self.df[self.columns[utils.FNO_COL_IDX['instrument']]] == utils.instruments['stockFutures']]
        # dataframe for only stock options
        self.stkOptDf = self.df.loc[
            self.df[self.columns[utils.FNO_COL_IDX['instrument']]] == utils.instruments['stockOptions']]

        # Create the list of Unique symbols for each of the 4 Instrument
        self.stkOptSymbolList = list(set(self.stkOptDf[self.columns[utils.FNO_COL_IDX['symbol']]]))
        self.stkFutSymbolList = list(set(self.stkFutDf[self.columns[utils.FNO_COL_IDX['symbol']]]))
        self.idxOptSymbolList = list(set(self.idxOptDf[self.columns[utils.FNO_COL_IDX['symbol']]]))
        self.idxFutSymbolList = list(set(self.idxFutDf[self.columns[utils.FNO_COL_IDX['symbol']]]))

        # Create the list of Expiry Dates in the csv file for each of the 4 Instruments
        self.stkOptExpDatesList = list(set(self.stkOptDf[self.columns[utils.FNO_COL_IDX['expiryDate']]]))
        self.stkFutExpDatesList = list(set(self.stkFutDf[self.columns[utils.FNO_COL_IDX['expiryDate']]]))
        self.idxOptExpDatesList = list(set(self.idxOptDf[self.columns[utils.FNO_COL_IDX['expiryDate']]]))
        self.idxFutExpDatesList = list(set(self.idxFutDf[self.columns[utils.FNO_COL_IDX['expiryDate']]]))

        # Create lis of type of options ['CE', 'PE'].  This is common for both stock and futures
        self.optionTypeList = list(set(self.stkOptDf[self.columns[utils.FNO_COL_IDX['optionType']]]))

    def getCSVColumnList(self):
        return self.columns

    def getStockOptionsSymbolsList(self):
        return self.stkOptSymbolList

    def getStockFuturesSymbolsList(self):
        return self.stkFutSymbolList

    def getIndexOptionsSymbolList(self):
        return self.idxOptSymbolList

    def getIndexFuturesSymbolList(self):
        return self.idxFutSymbolList

    # FOR STOCK OPTIONS
    def getOptStkNestedData(self):
        stkOptionData = {}
        for stkSymbol in self.stkOptSymbolList:
            # Create a new dataframe from stock option dataframe (self.stkOptDf) w.r.t each stock symbol
            # SYMBOL DATAFRAME
            symbolDf = self.stkOptDf.loc[self.stkOptDf[self.columns[utils.FNO_COL_IDX['symbol']]] == stkSymbol]
            # From this stock specific dataframe create expiry date specific data frame
            expiryDateData = {}
            for expiryDate in self.stkOptExpDatesList:
                # EXPIRY DATE DATAFRAME
                expDateDf = symbolDf.loc[symbolDf[self.columns[utils.FNO_COL_IDX['expiryDate']]] == expiryDate]
                # Create strike price list of this expiry from the above data frame
                # STRIKE PRICE LIST
                strikePriceList = list(set(expDateDf[self.columns[utils.FNO_COL_IDX['strikePrice']]]))
                strikePriceData = {}
                for strikePrice in strikePriceList:
                    optionTypeData = {}
                    for optionType in self.optionTypeList:  # ['CE', 'PE']
                        dailyData = {}
                        # Create a dataframe for this strike price and this option type from ExpiryDate dataframe (expDateDf)
                        # FINAL DATAFRAME w.r.t strikeprice and optiontype
                        optTypeDf = expDateDf.loc[
                            (expDateDf[self.columns[utils.FNO_COL_IDX['strikePrice']]] == strikePrice)
                            & (expDateDf[self.columns[utils.FNO_COL_IDX['optionType']]] == optionType)]

                        # Insert remaining column data (daily) in a dictionary
                        # have to do a .value[0] to extract the value from a dataframe cell because it has other meta data hidden in it
                        dailyData.update({
                            self.columns[utils.FNO_COL_IDX['timeStamp']]:
                                optTypeDf[self.columns[utils.FNO_COL_IDX['timeStamp']]].values[0],
                            self.columns[utils.FNO_COL_IDX['open']]:
                                optTypeDf[self.columns[utils.FNO_COL_IDX['open']]].values[0],
                            self.columns[utils.FNO_COL_IDX['low']]:
                                optTypeDf[self.columns[utils.FNO_COL_IDX['low']]].values[0],
                            self.columns[utils.FNO_COL_IDX['close']]:
                                optTypeDf[self.columns[utils.FNO_COL_IDX['close']]].values[0],
                            self.columns[utils.FNO_COL_IDX['settlePrice']]:
                                optTypeDf[self.columns[utils.FNO_COL_IDX['settlePrice']]].values[0],
                            self.columns[utils.FNO_COL_IDX['contracts']]:
                                optTypeDf[self.columns[utils.FNO_COL_IDX['contracts']]].values[0],
                            self.columns[utils.FNO_COL_IDX['valueInLakhs']]:
                                optTypeDf[self.columns[utils.FNO_COL_IDX['valueInLakhs']]].values[0],
                            self.columns[utils.FNO_COL_IDX['openInterest']]:
                                optTypeDf[self.columns[utils.FNO_COL_IDX['openInterest']]].values[0],
                            self.columns[utils.FNO_COL_IDX['changeInOpenInterest']]:
                                optTypeDf[self.columns[utils.FNO_COL_IDX['changeInOpenInterest']]].values[0]
                        })

                        optionTypeData.update({optionType: dailyData})
                    strikePriceData.update({strikePrice: optionTypeData})
                expiryDateData.update({expiryDate: strikePriceData})
            stkOptionData.update({stkSymbol: expiryDateData})

        return stkOptionData

    def getOptStkFlatData(self):
        '''
        Returns a list of following dictionary corresponding to each row in the csv file
        [
            {
                symbol          : ,
                expiryDate      : ,
                strikePrice     : ,
                optionType      : ,
                open            : ,
                high            : ,
                low             : ,
                close           : ,
                settlePrice     : ,
                contracts       : ,
                valInLakhs      : ,
                oi              : ,
                changeInOi      : '
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
                'symbol': r[self.columns[utils.FNO_COL_IDX['symbol']]],
                'expiryDate': r[self.columns[utils.FNO_COL_IDX['expiryDate']]],
                'strikePrice': r[self.columns[utils.FNO_COL_IDX['strikePrice']]],
                'optionType': r[self.columns[utils.FNO_COL_IDX['optionType']]],
                'open': r[self.columns[utils.FNO_COL_IDX['open']]],
                'high': r[self.columns[utils.FNO_COL_IDX['high']]],
                'low': r[self.columns[utils.FNO_COL_IDX['low']]],
                'close': r[self.columns[utils.FNO_COL_IDX['close']]],
                'settlePrice': r[self.columns[utils.FNO_COL_IDX['settlePrice']]],
                'contracts': r[self.columns[utils.FNO_COL_IDX['contracts']]],
                'valueInLakhs': r[self.columns[utils.FNO_COL_IDX['valueInLakhs']]],
                'openInterest': r[self.columns[utils.FNO_COL_IDX['openInterest']]],
                'changeInOpenInterest': r[self.columns[utils.FNO_COL_IDX['changeInOpenInterest']]],
                'timeStamp': r[self.columns[utils.FNO_COL_IDX['timeStamp']]]
            }
            return rowDict

        returnList = []
        for index, row in self.stkOptDf.iterrows():
            rowDict = getDictFromRows(row)
            # print()
            # print(rowDict)
            returnList.append(rowDict)

        return returnList

    def getFutStkFlatData(self):
        '''
        Returns a list of following dictionary corresponding to each row in the csv file
        [
            {
                symbol          : ,
                expiryDate      : ,
                open            : ,
                high            : ,
                low             : ,
                close           : ,
                settlePrice     : ,
                contracts       : ,
                valInLakhs      : ,
                oi              : ,
                changeInOi      : '
                date            :
            },
            {},
            {},
            .
            .
            .
        ]
        '''

        # For Futures, columns 'STRIKE_PR'and 'OPTION_TYP' are not required, hence drop them in stock futures dataframe (self.stkFutDf)
        futDf = self.stkFutDf.drop(
            [self.columns[utils.FNO_COL_IDX['strikePrice']], self.columns[utils.FNO_COL_IDX['optionType']]], axis=1)

        # Nested function
        def getDictFromRows(r):
            rowDict = {
                'symbol': r[self.columns[utils.FNO_COL_IDX['symbol']]],
                'expiryDate': r[self.columns[utils.FNO_COL_IDX['expiryDate']]],
                # 'strikePrice'               : r[self.columns[utils.FNO_COL_IDX['strikePrice']]],
                # 'optionType'                : r[self.columns[utils.FNO_COL_IDX['optionType']]],
                'open': r[self.columns[utils.FNO_COL_IDX['open']]],
                'high': r[self.columns[utils.FNO_COL_IDX['high']]],
                'low': r[self.columns[utils.FNO_COL_IDX['low']]],
                'close': r[self.columns[utils.FNO_COL_IDX['close']]],
                'settlePrice': r[self.columns[utils.FNO_COL_IDX['settlePrice']]],
                'contracts': r[self.columns[utils.FNO_COL_IDX['contracts']]],
                'valueInLakhs': r[self.columns[utils.FNO_COL_IDX['valueInLakhs']]],
                'openInterest': r[self.columns[utils.FNO_COL_IDX['openInterest']]],
                'changeInOpenInterest': r[self.columns[utils.FNO_COL_IDX['changeInOpenInterest']]],
                'timeStamp': r[self.columns[utils.FNO_COL_IDX['timeStamp']]]
            }
            return rowDict

        returnList = []
        for index, row in futDf.iterrows():
            rowDict = getDictFromRows(row)
            # print()
            # print(rowDict)
            returnList.append(rowDict)

        return returnList

    def getOptIdxFlatData(self):
        '''
        Returns a list of following dictionary corresponding to each row in the csv file
        [
            {
                symbol          : ,
                expiryDate      : ,
                strikePrice     : ,
                optionType      : ,
                open            : ,
                high            : ,
                low             : ,
                close           : ,
                settlePrice     : ,
                contracts       : ,
                valInLakhs      : ,
                oi              : ,
                changeInOi      : '
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
                'symbol': r[self.columns[utils.FNO_COL_IDX['symbol']]],
                'expiryDate': r[self.columns[utils.FNO_COL_IDX['expiryDate']]],
                'strikePrice': r[self.columns[utils.FNO_COL_IDX['strikePrice']]],
                'optionType': r[self.columns[utils.FNO_COL_IDX['optionType']]],
                'open': r[self.columns[utils.FNO_COL_IDX['open']]],
                'high': r[self.columns[utils.FNO_COL_IDX['high']]],
                'low': r[self.columns[utils.FNO_COL_IDX['low']]],
                'close': r[self.columns[utils.FNO_COL_IDX['close']]],
                'settlePrice': r[self.columns[utils.FNO_COL_IDX['settlePrice']]],
                'contracts': r[self.columns[utils.FNO_COL_IDX['contracts']]],
                'valueInLakhs': r[self.columns[utils.FNO_COL_IDX['valueInLakhs']]],
                'openInterest': r[self.columns[utils.FNO_COL_IDX['openInterest']]],
                'changeInOpenInterest': r[self.columns[utils.FNO_COL_IDX['changeInOpenInterest']]],
                'timeStamp': r[self.columns[utils.FNO_COL_IDX['timeStamp']]]
            }
            return rowDict

        returnList = []
        for index, row in self.idxOptDf.iterrows():
            rowDict = getDictFromRows(row)
            # print()
            # print(rowDict)
            returnList.append(rowDict)

        return returnList

    def getFutIdxFlatData(self):
        '''
        Returns a list of following dictionary corresponding to each row in the csv file
        [
            {
                symbol          : ,
                expiryDate      : ,
                open            : ,
                high            : ,
                low             : ,
                close           : ,
                settlePrice     : ,
                contracts       : ,
                valInLakhs      : ,
                oi              : ,
                changeInOi      : '
                date            :
            },
            {},
            {},
            .
            .
            .
        ]
        '''

        # For Futures, columns 'STRIKE_PR'and 'OPTION_TYP' are not required, hence drop them in stock futures dataframe (self.stkFutDf)
        futDf = self.idxFutDf.drop(
            [self.columns[utils.FNO_COL_IDX['strikePrice']], self.columns[utils.FNO_COL_IDX['optionType']]], axis=1)

        # Nested function
        def getDictFromRows(r):
            rowDict = {
                'symbol': r[self.columns[utils.FNO_COL_IDX['symbol']]],
                'expiryDate': r[self.columns[utils.FNO_COL_IDX['expiryDate']]],
                # 'strikePrice'               : r[self.columns[utils.FNO_COL_IDX['strikePrice']]],
                # 'optionType'                : r[self.columns[utils.FNO_COL_IDX['optionType']]],
                'open': r[self.columns[utils.FNO_COL_IDX['open']]],
                'high': r[self.columns[utils.FNO_COL_IDX['high']]],
                'low': r[self.columns[utils.FNO_COL_IDX['low']]],
                'close': r[self.columns[utils.FNO_COL_IDX['close']]],
                'settlePrice': r[self.columns[utils.FNO_COL_IDX['settlePrice']]],
                'contracts': r[self.columns[utils.FNO_COL_IDX['contracts']]],
                'valueInLakhs': r[self.columns[utils.FNO_COL_IDX['valueInLakhs']]],
                'openInterest': r[self.columns[utils.FNO_COL_IDX['openInterest']]],
                'changeInOpenInterest': r[self.columns[utils.FNO_COL_IDX['changeInOpenInterest']]],
                'timeStamp': r[self.columns[utils.FNO_COL_IDX['timeStamp']]]
            }
            return rowDict

        returnList = []
        for index, row in futDf.iterrows():
            rowDict = getDictFromRows(row)
            # print()
            # print(rowDict)
            returnList.append(rowDict)

        return returnList


if __name__ == "__main__":
    r = ReadFnOCSV('./data/fo18JUN2019bhav.csv')
    optData = r.getOptStkFlatData()
    print(optData[0])