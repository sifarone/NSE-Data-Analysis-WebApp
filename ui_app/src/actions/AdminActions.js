import { AdminInitJobsAPI,
        AdminWriteServerJobsAPI,
        //AdminUploadCSVDataAPI,
        AdminUploadCashCSVFileAPI,
        AdminUploadFnOCSVFileAPI,
        AdminUploadIndexCSVFileAPI } from '../APIs';

export const adminInitJobAction = () => {
    return async function(dispatch, getState) {

        const post_body = {
            actions : [
                            "CASH_SYMBOLS",
                            "FNOSTK_SYMBOLS",
                            "FNOIDX_SYMBOLS",
                            "INFO_STKOPT",
                            "INFO_STKFUT",
                            "INFO_IDXOPT",
                            "INFO_IDXFUT"
                        ]
        }
    
        const response =  await fetch(AdminInitJobsAPI, {
            method: 'POST',
            body: JSON.stringify(post_body)
        })
    
        const jsonData = await response.json()
        console.log('ADMIN_INIT_JOBS =====> status: ', jsonData);
    
        dispatch({
            type: 'ADMIN_INIT_JOBS',
            payload: {
                adminInitJobStatus : jsonData
            }
        })
    }
}


export const adminLoadCashDataAction = () => {
    return async function(dispatch, getState) {

        const post_body = {
            actions     : ['LOAD_DATA'],
            dataType    : 'CASH_DATA',
            source      : "csv",
            checks      : "yes" 
        }
    
        const response =  await fetch(AdminWriteServerJobsAPI, {
            method: 'POST',
            body: JSON.stringify(post_body)
        })
    
        const jsonData = await response.json()
        console.log('ADMIN_LOAD_CASH_DATA =====> status: ', jsonData);
    
        dispatch({
            type: 'ADMIN_LOAD_CASH_DATA',
            payload: {
                adminLoadCashDataStatus : jsonData
            }
        })
    }
}

export const adminLoadFnODataAction = () => {
    return async function(dispatch, getState) {

        const post_body = {
            actions     : ['LOAD_DATA'],
            dataType    : 'FNO_DATA',
            source      : "csv"
        }
    
        const response =  await fetch(AdminWriteServerJobsAPI, {
            method: 'POST',
            body: JSON.stringify(post_body)
        })

        const jsonData = await response.json()
        console.log('ADMIN_LOAD_FNO_DATA =====> status: ', jsonData);
    
        dispatch({
            type: 'ADMIN_LOAD_FNO_DATA',
            payload: {
                adminLoadFnODataStatus : jsonData
            }
        })
    }
}

export const adminUploadCashCsvFileAction = (formData) => {
    return async function(dispatch, getState) {  
    
        const response =  await fetch(AdminUploadCashCSVFileAPI , {
            method: 'POST',
            body: formData
        })
        const jsonData = await response.json()

        console.log('ADMIN_UPLOAD_CASH_CSV_FILE =====> status: ', jsonData);
    
        dispatch({
            type: 'ADMIN_UPLOAD_CASH_CSV_FILE',
            payload: {
                adminUploadCashCsvFileStatus : jsonData
            }
        })
    }
}

export const adminUploadFnOCsvFileAction = (formData) => {
    return async function(dispatch, getState) {        
    
        const response =  await fetch(AdminUploadFnOCSVFileAPI, {
            method: 'POST',
            body: formData
        })
        const jsonData = await response.json()

        console.log('ADMIN_UPLOAD_FNO_CSV_FILE =====> status: ', jsonData);
    
        dispatch({
            type: 'ADMIN_UPLOAD_FNO_CSV_FILE',
            payload: {
                adminUploadFnOCsvFileStatus : jsonData
            }
        })
    }
}

export const adminUploadIndexCsvFileAction = (formData) => {
    return async function(dispatch, getState) {        
    
        const response =  await fetch(AdminUploadIndexCSVFileAPI, {
            method: 'POST',
            body: formData
        })
        const jsonData = await response.json()

        console.log('ADMIN_UPLOAD_INDEX_CSV_FILE =====> status: ', jsonData);
    
        dispatch({
            type: 'ADMIN_UPLOAD_INDEX_CSV_FILE',
            payload: {
                adminUploadIndexCsvFileStatus : jsonData
            }
        })
    }
}

export const adminDeleteCashDirAction = () => {
    return async function(dispatch, getState) {

        const post_body = {
            actions     : ['DELETE_DIR'],
            dirType     : 'CASH_DATA_DIR'
        }
    
        const response =  await fetch(AdminWriteServerJobsAPI, {
            method: 'POST',
            body: JSON.stringify(post_body)
        })

        const jsonData = await response.json()
        console.log('ADMIN_DELETE_CASH_DIR =====> status: ', jsonData['DELETE_DIR']);
    
        dispatch({
            type: 'ADMIN_DELETE_CASH_DIR',
            payload: {
                adminDeleteCashDirStatus : jsonData['DELETE_DIR']
            }
        })
    }
}

export const adminDeleteCashArchivedDirAction = () => {
    return async function(dispatch, getState) {

        const post_body = {
            actions     : ['DELETE_DIR'],
            dirType     : 'CASH_ARCHIVED_DATA_DIR'
        }
    
        const response =  await fetch(AdminWriteServerJobsAPI, {
            method: 'POST',
            body: JSON.stringify(post_body)
        })

        const jsonData = await response.json()
        console.log('ADMIN_DELETE_CASH_ARCHIVED_DIR =====> status: ', jsonData['DELETE_DIR']);
    
        dispatch({
            type: 'ADMIN_DELETE_CASH_ARCHIVED_DIR',
            payload: {
                adminDeleteCashArchivedDirStatus : jsonData['DELETE_DIR']
            }
        })
    }
}

export const adminDeleteFnODirAction = () => {
    return async function(dispatch, getState) {

        const post_body = {
            actions     : ['DELETE_DIR'],
            dirType     : 'FNO_DATA_DIR'
        }
    
        const response =  await fetch(AdminWriteServerJobsAPI, {
            method: 'POST',
            body: JSON.stringify(post_body)
        })

        const jsonData = await response.json()
        console.log('ADMIN_DELETE_FNO_DIR =====> status: ', jsonData['DELETE_DIR']);
    
        dispatch({
            type: 'ADMIN_DELETE_FNO_DIR',
            payload: {
                adminDeleteFnODirStatus : jsonData['DELETE_DIR']
            }
        })
    }
}

export const adminDeleteIndexDirAction = () => {
    return async function(dispatch, getState) {

        const post_body = {
            actions     : ['DELETE_DIR'],
            dirType     : 'INDEX_DATA_DIR'
        }
    
        const response =  await fetch(AdminWriteServerJobsAPI, {
            method: 'POST',
            body: JSON.stringify(post_body)
        })

        const jsonData = await response.json()
        console.log('ADMIN_DELETE_INDEX_DIR =====> status: ', jsonData['DELETE_DIR']);
    
        dispatch({
            type: 'ADMIN_DELETE_INDEX_DIR',
            payload: {
                adminDeleteIndexDirStatus : jsonData['DELETE_DIR']
            }
        })
    }
}

export const adminDeleteIndexArchivedDirAction = () => {
    return async function(dispatch, getState) {

        const post_body = {
            actions     : ['DELETE_DIR'],
            dirType     : 'INDEX_ARCHIVED_DATA_DIR'
        }
    
        const response =  await fetch(AdminWriteServerJobsAPI, {
            method: 'POST',
            body: JSON.stringify(post_body)
        })

        const jsonData = await response.json()
        console.log('ADMIN_DELETE_INDEX_ARCHIVED_DIR =====> status: ', jsonData['DELETE_DIR']);
    
        dispatch({
            type: 'ADMIN_DELETE_INDEX_ARCHIVED_DIR',
            payload: {
                adminDeleteIndexArchivedDirStatus : jsonData['DELETE_DIR']
            }
        })
    }
}

export const adminDeleteCashDataAction = () => {
    return async function(dispatch, getState) {

        const post_body = {
            actions     : ['DELETE_DATA'],
            dataType    : 'CASH_DATA'
        }
    
        const response =  await fetch(AdminWriteServerJobsAPI, {
            method: 'POST',
            body: JSON.stringify(post_body)
        })

        const jsonData = await response.json()
        console.log('ADMIN_DELETE_CASH_DATA =====> status: ', jsonData['DELETE_DATA']);
    
        dispatch({
            type: 'ADMIN_DELETE_CASH_DATA',
            payload: {
                adminDeleteCashDataStatus : jsonData['DELETE_DATA']
            }
        })
    }
}

export const adminDeleteStockFnODataAction = (expDate) => {
    return async function(dispatch, getState) {
        console.log('adminDeleteStockFnODataAction : expiryDate > ', expDate)

        const post_body = {
            actions     : ['DELETE_DATA'],
            dataType    : 'STOCK_FNO_DATA',
            expiryDate  : expDate
        }
    
        const response =  await fetch(AdminWriteServerJobsAPI, {
            method: 'POST',
            body: JSON.stringify(post_body)
        })

        const jsonData = await response.json()
        console.log('ADMIN_DELETE_STOCK_FNO_DATA =====> status: ', jsonData['DELETE_DATA']);
    
        dispatch({
            type: 'ADMIN_DELETE_STOCK_FNO_DATA',
            payload: {
                adminDeleteStockFnODataStatus : jsonData['DELETE_DATA']
            }
        })
    }
}

export const adminDeleteIndexFnODataAction = (expDate) => {
    return async function(dispatch, getState) {
        console.log('adminDeleteIndexFnODataAction : expiryDate > ', expDate)

        const post_body = {
            actions     : ['DELETE_DATA'],
            dataType    : 'INDEX_FNO_DATA',
            expiryDate  : expDate
        }
    
        const response =  await fetch(AdminWriteServerJobsAPI, {
            method: 'POST',
            body: JSON.stringify(post_body)
        })

        const jsonData = await response.json()
        console.log('ADMIN_DELETE_INDEX_FNO_DATA =====> status: ', jsonData['DELETE_DATA']);
    
        dispatch({
            type: 'ADMIN_DELETE_INDEX_FNO_DATA',
            payload: {
                adminDeleteIndexFnODataStatus : jsonData['DELETE_DATA']
            }
        })
    }
}

export const adminDeleteIndexDataAction = () => {
    return async function(dispatch, getState) {

        const post_body = {
            actions     : ['DELETE_DATA'],
            dataType    : 'INDEX_DATA'
        }
    
        const response =  await fetch(AdminWriteServerJobsAPI, {
            method: 'POST',
            body: JSON.stringify(post_body)
        })

        const jsonData = await response.json()
        console.log('ADMIN_DELETE_INDEX_DATA =====> status: ', jsonData['DELETE_DATA']);
    
        dispatch({
            type: 'ADMIN_DELETE_INDEX_DATA',
            payload: {
                adminDeleteIndexDataStatus : jsonData['DELETE_DATA']
            }
        })
    }
}
