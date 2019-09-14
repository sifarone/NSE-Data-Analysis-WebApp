import { 
    CashDataAPI,
    CashStockSymbolListAPI,
    IndexSymbolListAPI,
    FnOStockSymbolListAPI,
    FnOIndexSymbolListAPI,
    StockOptionInfoAPI,
    StockFutureInfoAPI,
    IndexOptionInfoAPI,
    IndexFutureInfoAPI,
    ChartDataAPI 
} from '../APIs';

export const initialDataChartAction = () => {
    return async function(dispatch, getState) {

        const cashStockSymbolListJson =  await fetch(CashStockSymbolListAPI, {
            method: 'GET'
        })
        const indexSymbolListJson =  await fetch(IndexSymbolListAPI, {
            method: 'GET'
        })
        const fnoStockSymbolListJson =  await fetch(FnOStockSymbolListAPI, {
            method: 'GET'
        })
        const fnoIndexSymbolListJson =  await fetch(FnOIndexSymbolListAPI, {
            method: 'GET'
        })
        const stkOptInfoJson =  await fetch(StockOptionInfoAPI, {
            method: 'GET'
        })
        const stkFutInfoJson =  await fetch(StockFutureInfoAPI, {
            method: 'GET'
        })
        const idxOptInfoJson =  await fetch(IndexOptionInfoAPI, {
            method: 'GET'
        })
        const idxFutInfoJson =  await fetch(IndexFutureInfoAPI, {
            method: 'GET'
        })

        console.log('cashStockSymbolListJson: ', cashStockSymbolListJson.status)
        console.log('indexSymbolListJson: ', indexSymbolListJson.status)
        console.log('fnoStockSymbolListJson: ', fnoStockSymbolListJson.status)
        console.log('fnoIndexSymbolListJson: ', fnoIndexSymbolListJson.status)
        console.log('stkOptInfoJson: ', stkOptInfoJson.status)
        console.log('stkFutInfoJson: ', stkFutInfoJson.status)
        console.log('idxOptInfoJson: ', idxOptInfoJson.status)
        console.log('idxFutInfoJson: ', idxFutInfoJson.status)

        let cashStockSymbolList = []
        let indexSymbolList = []
        let fnoStockSymbolList = []
        let fnoIndexSymbolList = []
        let stkOptInfo = {}
        let stkFutInfo = {}
        let idxOptInfo = {}
        let idxFutInfo = {}

        if (cashStockSymbolListJson === 500
            || indexSymbolListJson === 500
            || fnoStockSymbolListJson.status === 500
            || fnoIndexSymbolListJson.status === 500
            || stkOptInfoJson.status === 500 
            || stkFutInfoJson.status === 500
            || idxOptInfoJson.status === 500
            || idxFutInfoJson.status === 500) {
            console.log('Init data not ready --  Run Admin Job')
        }
        else {
            cashStockSymbolList = await cashStockSymbolListJson.json()
            indexSymbolList     = await indexSymbolListJson.json()
            fnoStockSymbolList  = await fnoStockSymbolListJson.json()
            fnoIndexSymbolList  = await fnoIndexSymbolListJson.json()
            stkOptInfo          = await stkOptInfoJson.json()
            stkFutInfo          = await stkFutInfoJson.json()
            idxOptInfo          = await idxOptInfoJson.json()
            idxFutInfo          = await idxFutInfoJson.json()
        }

        console.log('cashStockSymbolList: ', cashStockSymbolList)
        console.log('indexSymbolList: ', indexSymbolList)
        console.log('fnoStockSymbolList: ', fnoStockSymbolList)
        console.log('stkOptInfo: ', stkOptInfo)
        console.log('stkFutInfo: ', stkFutInfo)
        console.log('fnoIndexSymbolList: ', fnoIndexSymbolList)
        console.log('idxOptInfo: ', idxOptInfo)
        console.log('idxFutInfo: ', idxFutInfo)

        dispatch({
            type: 'CHART_INITIAL_DATA',
            payload: {
                cashStockSymbolList : cashStockSymbolList,
                indexSymbolList     : indexSymbolList,
                fnoStockSymbolList  : fnoStockSymbolList,
                fnoIndexSymbolList  : fnoIndexSymbolList,
                stockOptionInfo     : stkOptInfo,
                stockFutureInfo     : stkFutInfo,
                indexOptionInfo     : idxOptInfo,
                indexFutureInfo     : idxFutInfo
            }
        })        
    }
}

export const cashDataChartAction = (symbol) => {
    return async function(dispatch, getState) {
        //console.log('CHART_CASH_DATA =====> state: ', getState());
    
        const response =  await fetch(CashDataAPI + symbol, {
            method: 'GET'
        })
    
        const jsonData = await response.json()
        console.log('CHART_CASH_DATA =====> status: ', jsonData);
    
        dispatch({
            type: 'CHART_CASH_DATA',
            payload: {
                cashData : jsonData
            }
        })
    }
}

export const indexDataChartAction = (symbol) => {
    return async function(dispatch, getState) {
        //console.log('CHART_CASH_DATA =====> state: ', getState());
    
        /*    
        const response =  await fetch(CashDataAPI + symbol, {
            method: 'GET'
        })
    
        const jsonData = await response.json()
        console.log('CHART_INDEX_DATA =====> status: ', jsonData);
    
        dispatch({
            type: 'CHART_INDEX_DATA',
            payload: {
                indexData : jsonData
            }
        })
        */

        //-------------------------------------------------

        const query_data = {
            symbol                  : symbol,
            startDate	    		: "01-Jan-2019",
            stkOptExpiryDate 	    : "18-Jul-2019",
            idxOptExpiryDate	    : "18-Jul-2019",
            stkFutExpiryDate	    : "18-Jul-2019",
            strikePrice   		    : 100,
            date					: "18-Jul-2019",
            charts  			    : ["indexData"],           
            indexData     : {
              sourceList			: ["index"],
              index                 : ["date", "openValue", "highValue", "lowValue", "closingValue", "lowValue", "pointsChange",
                                         "percentChange", "volume", "turnover", "peRatio", "pbRatio", "divYield"]
            }
          }
    
        const response =  await fetch(ChartDataAPI, {
            method: 'POST',
            body: JSON.stringify(query_data)
        })
    
        const jsonData = await response.json()
        console.log('CHART_INDEX_DATA =====> jsonData: ', jsonData);
    
        if (Object.keys(jsonData).includes('ERROR')) {
            console.log('CHART_INDEX_DATA =====> got error: ', jsonData.ERROR);
            dispatch({
                type: 'CHART_INDEX_DATA',
                payload: {
                    ...getState() 
                }
            })
        }
        else {
            dispatch({
                type: 'CHART_INDEX_DATA',
                payload: {
                    indexData: jsonData.indexData,
                        indexInputParams : {
                            symbol          : symbol
                        }
                }
            })
        }

    }
}

export const cashDataFnOChartAction = (symbol) => { // Used in FNO view
    return async function(dispatch, getState) {
        //console.log('CHART_CASH_DATA =====> state: ', getState());
    
        const response =  await fetch(CashDataAPI + symbol, {
            method: 'GET'
        })
    
        const jsonData = await response.json()
        console.log('CHART_CASH_FNO_DATA =====> status: ', jsonData);
    
        dispatch({
            type: 'CHART_CASH_FNO_DATA',
            payload: {
                cashFnOData : jsonData
            }
        })
    }
}

export const combinedStkFnODataChartAction = (symbol, stkOptExpDate, strikePrice, stkFutExpDate, date) => {
    return async function(dispatch, getState) {
        //console.log('CHART_STK_COMBINED_FNO_DATA =====> state: ', getState());
        console.log('CHART_STK_COMBINED_FNO_DATA =====> type strikePrice: ', typeof strikePrice);

        const query_data = {
            symbol                  : symbol,
            startDate	    		: "01-Jul-2019",
            stkOptExpiryDate 	    : stkOptExpDate,
            idxOptExpiryDate	    : "18-Jul-2019",
            stkFutExpiryDate	    : stkFutExpDate,
            strikePrice   		    : strikePrice,
            date					: date,
            charts  			    : ["stk_pe_oivsdoi", "stk_ce_oivsdoi", "stk_ce_cashOptFut", "stk_pe_cashOptFut"],
            stk_pe_oivsdoi		: {
              sourceList			      : ["put_stkOptOIvsDeltaOI"],
              put_stkOptOIvsDeltaOI	: ["date", "strikePrice", "stkOptOpenInterest", "stkOptChangeInOpenInterest"]
            },
            stk_ce_oivsdoi			: {
              sourceList				      : ["call_stkOptOIvsDeltaOI"],
              call_stkOptOIvsDeltaOI	: ["date", "strikePrice", "stkOptOpenInterest", "stkOptChangeInOpenInterest"]
            },
            stk_ce_cashOptFut     : {
              sourceList			      : ["cashStkFutStkOptCE"],
              cashStkFutStkOptCE    : ["date", "closePrice", "stkFutClosePrice", "stkOptClosePrice"]
            },
            stk_pe_cashOptFut     : {
              sourceList			      : ["cashStkFutStkOptPE"],
              cashStkFutStkOptPE    : ["date", "closePrice", "stkFutClosePrice", "stkOptClosePrice"]
            }
          }
    
        const response =  await fetch(ChartDataAPI, {
            method: 'POST',
            body: JSON.stringify(query_data)
        })
    
        const jsonData = await response.json()
        console.log('CHART_STK_COMBINED_FNO_DATA =====> jsonData: ', jsonData);

        if (Object.keys(jsonData).includes('ERROR')) {
            console.log('CHART_STK_COMBINED_FNO_DATA =====> got error: ', jsonData.ERROR);
            dispatch({
                type: 'CHART_STK_COMBINED_FNO_DATA',
                payload: {
                    ...getState() 
                }
            })
        }
        else {
            dispatch({
                type: 'CHART_STK_COMBINED_FNO_DATA',
                payload: {
                    
                    stk_pe_oivsdoi : jsonData.stk_pe_oivsdoi,
                    stk_ce_oivsdoi : jsonData.stk_ce_oivsdoi,
                    stk_ce_cashOptFut : jsonData.stk_ce_cashOptFut,
                    stk_pe_cashOptFut : jsonData.stk_pe_cashOptFut, 
                    combinedStkFnoInputParams : {
                        symbol          : symbol,
                        stkOptExpDate   : stkOptExpDate,
                        strikePrice     : strikePrice,
                        stkFutExpDate   : stkFutExpDate,
                        date            : date
                    }
                }
            })
        }
    }
}

export const stkCashFutCallOptChartAction = (symbol, stkOptExpDate, strikePrice, stkFutExpDate, date) => {
    return async function(dispatch, getState) {

        const query_data = {
            symbol                  : symbol,
            startDate	    		: "01-Jul-2019",
            stkOptExpiryDate 	    : stkOptExpDate,
            idxOptExpiryDate	    : "18-Jul-2019",
            stkFutExpiryDate	    : stkFutExpDate,
            strikePrice   		    : strikePrice,
            date					: date,
            charts  			    : ["stk_ce_cashOptFut"],            
            stk_ce_cashOptFut     : {
              sourceList			      : ["cashStkFutStkOptCE"],
              cashStkFutStkOptCE    : ["date", "closePrice", "stkFutClosePrice", "stkOptClosePrice"]
            }
          }
    
        const response =  await fetch(ChartDataAPI, {
            method: 'POST',
            body: JSON.stringify(query_data)
        })
    
        const jsonData = await response.json()
        console.log('CHART_STK_CASHFUTOPT_CE_DATA =====> jsonData: ', jsonData);

        if (Object.keys(jsonData).includes('ERROR')) {
            console.log('CHART_STK_CASHFUTOPT_CE_DATA =====> got error: ', jsonData.ERROR);
            dispatch({
                type: 'CHART_STK_CASHFUTOPT_CE_DATA',
                payload: {
                    ...getState() 
                }
            })
        }
        else {
            dispatch({
                type: 'CHART_STK_CASHFUTOPT_CE_DATA',
                payload: {
                        stk_ce_cashOptFut: jsonData.stk_ce_cashOptFut,
                        combinedStkFnoInputParams : {
                            symbol          : symbol,
                            stkOptExpDate   : stkOptExpDate,
                            strikePrice     : strikePrice,
                            stkFutExpDate   : stkFutExpDate,
                            date            : date
                        }
                }
            })
        }
    }
}

export const stkCashFutPutOptChartAction = (symbol, stkOptExpDate, strikePrice, stkFutExpDate, date) => {
    return async function(dispatch, getState) {
        //console.log('CHART_STK_CASHFUTOPT_PE_DATA =====> state: ', getState());

        const query_data = {
            symbol                  : symbol,
            startDate	    		: "01-Jul-2019",
            stkOptExpiryDate 	    : stkOptExpDate,
            idxOptExpiryDate	    : "18-Jul-2019",
            stkFutExpiryDate	    : stkFutExpDate,
            strikePrice   		    : strikePrice,
            date					: date,
            charts  			    : ["stk_pe_cashOptFut"],           
            stk_pe_cashOptFut     : {
              sourceList			      : ["cashStkFutStkOptPE"],
              cashStkFutStkOptPE    : ["date", "closePrice", "stkFutClosePrice", "stkOptClosePrice"]
            }
          }
    
        const response =  await fetch(ChartDataAPI, {
            method: 'POST',
            body: JSON.stringify(query_data)
        })
    
        const jsonData = await response.json()
        console.log('CHART_STK_CASHFUTOPT_PE_DATA =====> jsonData: ', jsonData);
    
        if (Object.keys(jsonData).includes('ERROR')) {
            console.log('CHART_STK_CASHFUTOPT_PE_DATA =====> got error: ', jsonData.ERROR);
            dispatch({
                type: 'CHART_STK_CASHFUTOPT_PE_DATA',
                payload: {
                    ...getState() 
                }
            })
        }
        else {
            dispatch({
                type: 'CHART_STK_CASHFUTOPT_PE_DATA',
                payload: {
                        stk_pe_cashOptFut: jsonData.stk_pe_cashOptFut,
                        combinedStkFnoInputParams : {
                            symbol          : symbol,
                            stkOptExpDate   : stkOptExpDate,
                            strikePrice     : strikePrice,
                            stkFutExpDate   : stkFutExpDate,
                            date            : date
                        }
                }
            })
        }
        
    }
}

export const stkCallOptOIvsDeltaOIChartAction = (symbol, stkOptExpDate, strikePrice, stkFutExpDate, date) => {
    return async function(dispatch, getState) {
        //console.log('CHART_STK_OIVSDELTAOI_CE_DATA =====> state: ', getState());

        const query_data = {
            symbol                  : symbol,
            startDate	    		: "01-Jul-2019",
            stkOptExpiryDate 	    : stkOptExpDate,
            idxOptExpiryDate	    : "18-Jul-2019",
            stkFutExpiryDate	    : stkFutExpDate,
            strikePrice   		    : strikePrice,
            date					: date,
            charts  			    : ["stk_ce_oivsdoi"],
            stk_ce_oivsdoi			: {
              sourceList				      : ["call_stkOptOIvsDeltaOI"],
              call_stkOptOIvsDeltaOI	: ["date", "strikePrice", "stkOptOpenInterest", "stkOptChangeInOpenInterest"]
            }
          }
    
        const response =  await fetch(ChartDataAPI, {
            method: 'POST',
            body: JSON.stringify(query_data)
        })
    
        const jsonData = await response.json()
        console.log('CHART_STK_OIVSDELTAOI_CE_DATA =====> jsonData: ', jsonData);
    
        if (Object.keys(jsonData).includes('ERROR')) {
            console.log('CHART_STK_OIVSDELTAOI_CE_DATA =====> got error: ', jsonData.ERROR);
            dispatch({
                type: 'CHART_STK_OIVSDELTAOI_CE_DATA',
                payload: {
                    ...getState() 
                }
            })
        }
        else {
            dispatch({
                type: 'CHART_STK_OIVSDELTAOI_CE_DATA',
                payload: {
                    stk_ce_oivsdoi : jsonData.stk_ce_oivsdoi,
                    combinedStkFnoInputParams : {
                        symbol          : symbol,
                        stkOptExpDate   : stkOptExpDate,
                        strikePrice     : strikePrice,
                        stkFutExpDate   : stkFutExpDate,
                        date            : date
                    }
                }
            })
        }
        
    }
}

export const stkPutOptOIvsDeltaOIChartAction = (symbol, stkOptExpDate, strikePrice, stkFutExpDate, date) => {
    return async function(dispatch, getState) {
        //console.log('CHART_STK_OIVSDELTAOI_PE_DATA =====> state: ', getState());

        const query_data = {
            symbol                  : symbol,
            startDate	    		: "01-Jul-2019",
            stkOptExpiryDate 	    : stkOptExpDate,
            idxOptExpiryDate	    : "18-Jul-2019",
            stkFutExpiryDate	    : stkFutExpDate,
            strikePrice   		    : strikePrice,
            date					: date,
            charts  			    : ["stk_pe_oivsdoi"],
            stk_pe_oivsdoi			: {
              sourceList				      : ["put_stkOptOIvsDeltaOI"],
              put_stkOptOIvsDeltaOI	: ["date", "strikePrice", "stkOptOpenInterest", "stkOptChangeInOpenInterest"]
            }
          }
    
        const response =  await fetch(ChartDataAPI, {
            method: 'POST',
            body: JSON.stringify(query_data)
        })
    
        const jsonData = await response.json()
        console.log('CHART_STK_OIVSDELTAOI_PE_DATA =====> jsonData: ', jsonData);

        if (Object.keys(jsonData).includes('ERROR')) {
            console.log('CHART_STK_OIVSDELTAOI_PE_DATA =====> got error: ', jsonData.ERROR);
            dispatch({
                type: 'CHART_STK_OIVSDELTAOI_PE_DATA',
                payload: {
                    ...getState()
                }
            })
        }
        else {
            dispatch({
                type: 'CHART_STK_OIVSDELTAOI_PE_DATA',
                payload: {
                    stk_pe_oivsdoi : jsonData.stk_pe_oivsdoi,
                    combinedStkFnoInputParams : {
                        symbol          : symbol,
                        stkOptExpDate   : stkOptExpDate,
                        strikePrice     : strikePrice,
                        stkFutExpDate   : stkFutExpDate,
                        date            : date
                    }
                }
            })
        }        
    }
}

// Index FnO Chart Actions ------------------------------------------------------------
export const combinedIdxFnODataChartAction = (symbol, idxOptExpDate, strikePrice, idxFutExpDate, date) => {
    return async function(dispatch, getState) {
        //console.log('CHART_STK_COMBINED_FNO_DATA =====> state: ', getState());
        console.log('CHART_IDX_COMBINED_FNO_DATA =====> type strikePrice: ', typeof strikePrice);

        const query_data = {
            symbol                  : symbol,
            startDate	    		: "01-Jul-2019",
            stkOptExpiryDate 	    : "18-Jul-2019",
            stkFutExpiryDate	    : "18-Jul-2019",
            idxOptExpiryDate	    : idxOptExpDate,
            idxFutExpiryDate        : idxFutExpDate,            
            strikePrice   		    : strikePrice,
            date					: date,
            charts  			    : ["idx_pe_oivsdoi", "idx_ce_oivsdoi"],
            idx_pe_oivsdoi		: {
              sourceList			      : ["put_idxOptOIvsDeltaOI"],
              put_idxOptOIvsDeltaOI	: ["date", "strikePrice", "idxOptOpenInterest", "idxOptChangeInOpenInterest"]
            },
            idx_ce_oivsdoi			: {
              sourceList				      : ["call_idxOptOIvsDeltaOI"],
              call_idxOptOIvsDeltaOI	: ["date", "strikePrice", "idxOptOpenInterest", "idxOptChangeInOpenInterest"]
            }
          }
    
        const response =  await fetch(ChartDataAPI, {
            method: 'POST',
            body: JSON.stringify(query_data)
        })
    
        const jsonData = await response.json()
        console.log('CHART_IDX_COMBINED_FNO_DATA =====> jsonData: ', jsonData);

        if (Object.keys(jsonData).includes('ERROR')) {
            console.log('CHART_IDX_COMBINED_FNO_DATA =====> got error: ', jsonData.ERROR);
            dispatch({
                type: 'CHART_IDX_COMBINED_FNO_DATA',
                payload: {
                    ...getState() 
                }
            })
        }
        else {
            dispatch({
                type: 'CHART_IDX_COMBINED_FNO_DATA',
                payload: {                    
                    idx_pe_oivsdoi : jsonData.idx_pe_oivsdoi,
                    idx_ce_oivsdoi : jsonData.idx_ce_oivsdoi,
                    //idx_ce_cashOptFut : jsonData.stk_ce_cashOptFut,
                    //idx_pe_cashOptFut : jsonData.stk_pe_cashOptFut,
                    combinedIdxFnoInputParams : {
                        symbol          : symbol,
                        idxOptExpDate   : idxOptExpDate,
                        strikePrice     : strikePrice,
                        idxFutExpDate   : idxFutExpDate,
                        date            : date
                    }
                }
            })
        }
    }
}

export const idxCallOptOIvsDeltaOIChartAction = (symbol, idxOptExpDate, strikePrice, idxFutExpDate, date) => {
    return async function(dispatch, getState) {
        //console.log('CHART_STK_COMBINED_FNO_DATA =====> state: ', getState());
        console.log('CHART_IDX_COMBINED_FNO_DATA =====> type strikePrice: ', typeof strikePrice);

        const query_data = {
            symbol                  : symbol,
            startDate	    		: "01-Jul-2019",
            stkOptExpiryDate 	    : "18-Jul-2019",
            stkFutExpiryDate	    : "18-Jul-2019",
            idxOptExpiryDate	    : idxOptExpDate,
            idxFutExpiryDate        : idxFutExpDate,            
            strikePrice   		    : strikePrice,
            date					: date,
            charts  			    : ["idx_ce_oivsdoi"],
            idx_ce_oivsdoi			: {
              sourceList				      : ["call_idxOptOIvsDeltaOI"],
              call_idxOptOIvsDeltaOI	: ["date", "strikePrice", "idxOptOpenInterest", "idxOptChangeInOpenInterest"]
            }
          }
    
        const response =  await fetch(ChartDataAPI, {
            method: 'POST',
            body: JSON.stringify(query_data)
        })
    
        const jsonData = await response.json()
        console.log('CHART_IDX_OIVSDELTAOI_CE_DATA =====> jsonData: ', jsonData);

        if (Object.keys(jsonData).includes('ERROR')) {
            console.log('CHART_IDX_OIVSDELTAOI_CE_DATA =====> got error: ', jsonData.ERROR);
            dispatch({
                type: 'CHART_IDX_OIVSDELTAOI_CE_DATA',
                payload: {
                    ...getState() 
                }
            })
        }
        else {
            dispatch({
                type: 'CHART_IDX_OIVSDELTAOI_CE_DATA',
                payload: {
                    idx_ce_oivsdoi : jsonData.idx_ce_oivsdoi,
                    combinedIdxFnoInputParams : {
                        symbol          : symbol,
                        idxOptExpDate   : idxOptExpDate,
                        strikePrice     : strikePrice,
                        idxFutExpDate   : idxFutExpDate,
                        date            : date
                    }
                }
            })
        }
    }
}

export const idxPutOptOIvsDeltaOIChartAction = (symbol, idxOptExpDate, strikePrice, idxFutExpDate, date) => {
    return async function(dispatch, getState) {
        //console.log('CHART_STK_COMBINED_FNO_DATA =====> state: ', getState());
        console.log('CHART_IDX_COMBINED_FNO_DATA =====> type strikePrice: ', typeof strikePrice);

        const query_data = {
            symbol                  : symbol,
            startDate	    		: "01-Jul-2019",
            stkOptExpiryDate 	    : "18-Jul-2019",
            stkFutExpiryDate	    : "18-Jul-2019",
            idxOptExpiryDate	    : idxOptExpDate,
            idxFutExpiryDate        : idxFutExpDate,            
            strikePrice   		    : strikePrice,
            date					: date,
            charts  			    : ["idx_pe_oivsdoi"],
            idx_pe_oivsdoi			: {
              sourceList				      : ["put_idxOptOIvsDeltaOI"],
              put_idxOptOIvsDeltaOI	: ["date", "strikePrice", "idxOptOpenInterest", "idxOptChangeInOpenInterest"]
            }
          }
    
        const response =  await fetch(ChartDataAPI, {
            method: 'POST',
            body: JSON.stringify(query_data)
        })
    
        const jsonData = await response.json()
        console.log('CHART_IDX_OIVSDELTAOI_PE_DATA =====> jsonData: ', jsonData);

        if (Object.keys(jsonData).includes('ERROR')) {
            console.log('CHART_IDX_OIVSDELTAOI_PE_DATA =====> got error: ', jsonData.ERROR);
            dispatch({
                type: 'CHART_IDX_OIVSDELTAOI_PE_DATA',
                payload: {
                    ...getState() 
                }
            })
        }
        else {
            dispatch({
                type: 'CHART_IDX_OIVSDELTAOI_PE_DATA',
                payload: {
                    idx_pe_oivsdoi : jsonData.idx_pe_oivsdoi,
                    combinedIdxFnoInputParams : {
                        symbol          : symbol,
                        idxOptExpDate   : idxOptExpDate,
                        strikePrice     : strikePrice,
                        idxFutExpDate   : idxFutExpDate,
                        date            : date
                    }
                }
            })
        }
    }
}

export const stkOptionChainChartAction = (symbol, stkOptExpDate, date) => {
    return async function(dispatch, getState) {

        const query_data = {
            symbol                  : symbol,
            startDate	    		: "01-Jul-2019",
            stkOptExpiryDate 	    : stkOptExpDate,
            idxOptExpiryDate	    : "18-Jul-2019",
            stkFutExpiryDate	    : "18-Jul-2019",
            strikePrice   		    : 100,
            date					: date,
            charts  			    : ["stk_optionChain"],            
            stk_optionChain         : {
              sourceList			      : ["stock_optionChain"],
              stock_optionChain           : ["CE", "PE"]
            }
          }
    
        const response =  await fetch(ChartDataAPI, {
            method: 'POST',
            body: JSON.stringify(query_data)
        })
    
        const jsonData = await response.json()
        console.log('CHART_STK_OPTIONCHAIN_DATA =====> jsonData: ', jsonData);

        if (Object.keys(jsonData).includes('ERROR')) {
            console.log('CHART_STK_OPTIONCHAIN_DATA =====> got error: ', jsonData.ERROR);
            dispatch({
                type: 'CHART_STK_OPTIONCHAIN_DATA',
                payload: {
                    ...getState() 
                }
            })
        }
        else {
            dispatch({
                type: 'CHART_STK_OPTIONCHAIN_DATA',
                payload: {
                        stk_optionChain : jsonData.stk_optionChain,
                        stkOptioChainParams : {
                            symbol          : symbol,
                            stkOptExpDate   : stkOptExpDate,
                            date            : date
                        }
                }
            })
        }
    }
}

export const idxOptionChainChartAction = (symbol, idxOptExpDate, date) => {
    return async function(dispatch, getState) {

        const query_data = {
            symbol                  : symbol,
            startDate	    		: "01-Jul-2019",
            stkOptExpiryDate 	    : "18-Jul-2019",
            stkFutExpiryDate	    : "18-Jul-2019",
            idxOptExpiryDate	    : idxOptExpDate,
            idxFutExpiryDate        : "18-Jul-2019",            
            strikePrice   		    : 11000,
            date					: date,
            charts  			    : ["idx_optionChain"],
            idx_optionChain			: {
              sourceList		        : ["index_optionChain"],
              index_optionChain	        : ["CE", "PE"]
            }
          }
    
        const response =  await fetch(ChartDataAPI, {
            method: 'POST',
            body: JSON.stringify(query_data)
        })
    
        const jsonData = await response.json()
        console.log('CHART_IDX_OPTIONCHAIN_DATA =====> jsonData: ', jsonData);

        if (Object.keys(jsonData).includes('ERROR')) {
            console.log('CHART_IDX_OPTIONCHAIN_DATA =====> got error: ', jsonData.ERROR);
            dispatch({
                type: 'CHART_IDX_OPTIONCHAIN_DATA',
                payload: {
                    ...getState() 
                }
            })
        }
        else {
            dispatch({
                type: 'CHART_IDX_OPTIONCHAIN_DATA',
                payload: {
                    idx_optionChain : jsonData.idx_optionChain,
                    idxOptioChainParams : {
                        symbol          : symbol,
                        idxOptExpDate   : idxOptExpDate,
                        date            : date
                    }
                }
            })
        }
    }
}

