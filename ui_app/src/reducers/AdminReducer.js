const initialState = {    
    adminInitJobStatus                  : {},
    adminLoadCashDataStatus             : {},
    adminLoadFnODataStatus              : {},
    adminUploadCashCsvFileStatus        : '',
    adminUploadFnOCsvFileStatus         : '',
    adminUploadIndexCsvFileStatus       : '',
    adminDeleteCashDirStatus            : '',
    adminDeleteCashArchivedDirStatus    : '',
    adminDeleteFnODirStatus             : '',
    adminDeleteIndexDirStatus           : '',
    adminDeleteIndexArchivedDirStatus   : '',
    adminDeleteCashDataStatus           : '',
    adminDeleteStockFnODataStatus       : '',
    adminDeleteIndexFnODataStatus       : '',
    adminDeleteIndexDataStatus          : ''
}

export const adminReducer = (state=initialState, action) => {

    switch (action.type) {
        case 'ADMIN_INIT_JOBS':
            return {
                ...state,
                ...action.payload
            }

        case 'ADMIN_LOAD_CASH_DATA':
            return {
                ...state,
                ...action.payload
            }

        case 'ADMIN_LOAD_FNO_DATA':
            return {
                ...state,
                ...action.payload
            }

        case 'ADMIN_UPLOAD_CASH_CSV_FILE':
            return {
                ...state,
                ...action.payload
            }

        case 'ADMIN_UPLOAD_FNO_CSV_FILE':
            return {
                ...state,
                ...action.payload
            }

        case 'ADMIN_UPLOAD_INDEX_CSV_FILE':
            return {
                ...state,
                ...action.payload
            }

        case 'ADMIN_DELETE_CASH_DIR':
            return {
                ...state,
                ...action.payload
            }

        case 'ADMIN_DELETE_CASH_ARCHIVED_DIR':
            return {
                ...state,
                ...action.payload
            }

        case 'ADMIN_DELETE_FNO_DIR':
            return {
                ...state,
                ...action.payload
            }

        case 'ADMIN_DELETE_INDEX_DIR':
            return {
                ...state,
                ...action.payload
            }

        case 'ADMIN_DELETE_INDEX_ARCHIVED_DIR':
            return {
                ...state,
                ...action.payload
            }

        case 'ADMIN_DELETE_CASH_DATA':
            return {
                ...state,
                ...action.payload
            }

        case 'ADMIN_DELETE_STOCK_FNO_DATA':
            return {
                ...state,
                ...action.payload
            }

        case 'ADMIN_DELETE_INDEX_FNO_DATA':
            return {
                ...state,
                ...action.payload
            }

        case 'ADMIN_DELETE_INDEX_DATA':
            return {
                ...state,
                ...action.payload
            }

        default:
            return state;
    }
}