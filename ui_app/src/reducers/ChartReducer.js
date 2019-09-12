
const initialState = { 
    cashStockSymbolList : [],   
    fnoStockSymbolList  : [],
    fnoIndexSymbolList  : [],
    stockOptionInfo     : {},
    stockFutureInfo     : {},
    indexOptionInfo     : {},
    indexFutureInfo     : {},
    cashData            : {},
    cashFnOData         : {},
    stk_pe_oivsdoi      : {},
    stk_ce_oivsdoi      : {},
    stk_ce_cashOptFut   : {},
    stk_pe_cashOptFut   : {},
    idx_pe_oivsdoi      : {},
    idx_ce_oivsdoi      : {},
    stk_optionChain     : {},
    idx_optionChain     : {},
    combinedStkFnoInputParams: {
        symbol          : '',
        stkOptExpDate   : '',
        strikePrice     : 0,
        stkFutExpDate   : '',
        date            : ''
    },
    combinedIdxFnoInputParams : {
        symbol          : '',
        idxOptExpDate   : '',
        strikePrice     : 0,
        idxFutExpDate   : '',
        date            : ''
    },
    stkOptioChainParams : {
        symbol          : '',
        stkOptExpDate   : '',
        date            : ''
    },
    idxOptioChainParams : {
        symbol          : '',
        idxOptExpDate   : '',
        date            : ''
    }
}

export const chartReducer = (state=initialState, action) => {

    switch (action.type) {
        case 'CHART_INITIAL_DATA':
            return {
                ...state,
                ...action.payload
            }

        case 'CHART_CASH_DATA':
            console.log('CHART_CASH_DATA =====> state: ', state);
            return {
                ...state,
                ...action.payload
            }

        case 'CHART_CASH_FNO_DATA':
            console.log('CHART_CASH_FNO_DATA =====> state: ', state);
            return {
                ...state,
                ...action.payload
            }

        // Stock Fno
        case 'CHART_STK_COMBINED_FNO_DATA':
            console.log('CHART_STK_COMBINED_FNO_DATA =====> state: ', state);
            return {
                ...state,
                ...action.payload
            }

        case 'CHART_STK_CASHFUTOPT_CE_DATA':
            console.log('CHART_STK_CASHFUTOPT_CE_DATA =====> state: ', state);
            return {
                ...state,
                ...action.payload
            }

        case 'CHART_STK_CASHFUTOPT_PE_DATA':
            console.log('CHART_STK_CASHFUTOPT_PE_DATA =====> state: ', state);
            return {
                ...state,
                ...action.payload
            }

        case 'CHART_STK_OIVSDELTAOI_CE_DATA':
            console.log('CHART_STK_OIVSDELTAOI_CE_DATA =====> state: ', state);
            return {
                ...state,
                ...action.payload
            }

        case 'CHART_STK_OIVSDELTAOI_PE_DATA':
            console.log('CHART_STK_OIVSDELTAOI_PE_DATA =====> state: ', state);
            return {
                ...state,
                ...action.payload
            }

        // Index FNO
        case 'CHART_IDX_COMBINED_FNO_DATA':
            console.log('CHART_IDX_COMBINED_FNO_DATA =====> state: ', state);
            return {
                ...state,
                ...action.payload
            }

        case 'CHART_IDX_OIVSDELTAOI_CE_DATA':
            console.log('CHART_IDX_OIVSDELTAOI_CE_DATA =====> state: ', state);
            return {
                ...state,
                ...action.payload
            }

        case 'CHART_IDX_OIVSDELTAOI_PE_DATA':
            console.log('CHART_IDX_OIVSDELTAOI_PE_DATA =====> state: ', state);
            return {
                ...state,
                ...action.payload
            }

        case 'CHART_STK_OPTIONCHAIN_DATA':
            console.log('CHART_STK_OPTIONCHAIN_DATA =====> state: ', state);
            return {
                ...state,
                ...action.payload
            }

        case 'CHART_IDX_OPTIONCHAIN_DATA':
            console.log('CHART_IDX_OPTIONCHAIN_DATA =====> state: ', state);
            return {
                ...state,
                ...action.payload
            }

        default:
            return state;
    }
}