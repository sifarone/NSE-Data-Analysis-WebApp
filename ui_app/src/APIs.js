//import axios from 'axios';

import { DATA_SERVER,
        //READ_SERVER_PORT,
        //WRITE_SERVER_PORT
       } from './config';

// const FnOStockSymbolListAPI = 'http://' + DATA_SERVER + ':60000/api/fno';

/*
// --- Docker-Compose APIS
const CashStockSymbolListAPI = 'http://' + DATA_SERVER + ':' + READ_SERVER_PORT + '/api/cash';
const FnOStockSymbolListAPI = 'http://' + DATA_SERVER + ':' + READ_SERVER_PORT + '/api/fno';
const FnOIndexSymbolListAPI = 'http://' + DATA_SERVER + ':' + READ_SERVER_PORT + '/api/index';
const StockOptionInfoAPI = 'http://' + DATA_SERVER + ':' + READ_SERVER_PORT + '/api/fno/stkopt/info';
const StockFutureInfoAPI = 'http://' + DATA_SERVER + ':' + READ_SERVER_PORT + '/api/fno/stkfut/info';
const IndexOptionInfoAPI = 'http://' + DATA_SERVER + ':' + READ_SERVER_PORT + '/api/fno/idxopt/info';
const IndexFutureInfoAPI = 'http://' + DATA_SERVER + ':' + READ_SERVER_PORT + '/api/fno/idxfut/info';

const CashDataAPI = 'http://' + DATA_SERVER + ':' + READ_SERVER_PORT + '/api/cash/data?symbol=';
const ChartDataAPI = 'http://' + DATA_SERVER + ':' + READ_SERVER_PORT + '/api/post/charting';
const AdminInitJobsAPI = 'http://' + DATA_SERVER + ':' + READ_SERVER_PORT + '/api/admin';
//const AdminUploadCSVDataAPI = 'http://' + DATA_SERVER + ':' + WRITE_SERVER_PORT + '/api/write';
const AdminUploadCashCSVFileAPI = 'http://' + DATA_SERVER + ':' + WRITE_SERVER_PORT + '/api/admin/upload/cashcsv';
const AdminUploadFnOCSVFileAPI = 'http://' + DATA_SERVER + ':' + WRITE_SERVER_PORT + '/api/admin/upload/fnocsv';
const AdminUploadIndexCSVFileAPI = 'http://' + DATA_SERVER + ':' + WRITE_SERVER_PORT + '/api/admin/upload/indexcsv';

const AdminWriteServerJobsAPI = 'http://' + DATA_SERVER + ':' + WRITE_SERVER_PORT + '/api/admin';

const LoginAPI = 'http://' + DATA_SERVER + ':' + READ_SERVER_PORT + '/login';
const SigninAPI = 'http://' + DATA_SERVER + ':' + WRITE_SERVER_PORT + '/signin';
*/

// --- Kubernetes APIS
const CashStockSymbolListAPI = 'https://' + DATA_SERVER + '/read/api/cash';
const FnOStockSymbolListAPI = 'https://' + DATA_SERVER + '/read/api/fno';
const FnOIndexSymbolListAPI = 'https://' + DATA_SERVER + '/read/api/index';
const StockOptionInfoAPI = 'https://' + DATA_SERVER + '/read/api/fno/stkopt/info';
const StockFutureInfoAPI = 'https://' + DATA_SERVER + '/read/api/fno/stkfut/info';
const IndexOptionInfoAPI = 'https://' + DATA_SERVER + '/read/api/fno/idxopt/info';
const IndexFutureInfoAPI = 'https://' + DATA_SERVER + '/read/api/fno/idxfut/info';

const CashDataAPI = 'https://' + DATA_SERVER + '/read/api/cash/data?symbol=';
const ChartDataAPI = 'https://' + DATA_SERVER + '/read/api/post/charting';
const AdminInitJobsAPI = 'https://' + DATA_SERVER + '/read/api/admin';
const AdminUploadCashCSVFileAPI = 'https://' + DATA_SERVER + '/write/api/admin/upload/cashcsv';
const AdminUploadFnOCSVFileAPI = 'https://' + DATA_SERVER + '/write/api/admin/upload/fnocsv';
const AdminUploadIndexCSVFileAPI = 'https://' + DATA_SERVER + '/write/api/admin/upload/indexcsv';

const AdminWriteServerJobsAPI = 'https://' + DATA_SERVER + '/write/api/admin';

const LoginAPI = 'https://' + DATA_SERVER + '/read/login';
const SigninAPI = 'https://' + DATA_SERVER + '/write/signin';

export {
    CashStockSymbolListAPI,
    FnOStockSymbolListAPI,
    FnOIndexSymbolListAPI,
    StockOptionInfoAPI,
    StockFutureInfoAPI,
    IndexOptionInfoAPI,
    IndexFutureInfoAPI,
    CashDataAPI,
    ChartDataAPI,
    AdminInitJobsAPI,
    AdminWriteServerJobsAPI,

    //AdminUploadCSVDataAPI,
    AdminUploadCashCSVFileAPI,
    AdminUploadFnOCSVFileAPI,
    AdminUploadIndexCSVFileAPI,

    LoginAPI,
    SigninAPI
} 

/* TBD

const LoginAPI = axios.create({
    baseURL: 'http://' + DATA_SERVER + ':60000/login',
    method: 'post'
})

// get: CASH DATA API
const CashDataAPI = axios.create({
    baseURL: 'http://' + DATA_SERVER + ':60000/api/cash',
    method: 'get',
    params: {
        symbol : ''
    }
})

// post: CHART DATA API
const ChartDataAPI = axios.create({
    baseURL: 'http://' + DATA_SERVER + ':60000/api/post/charting',
    method: 'post'
})

// post: ADMIN INIT_JOBS API
const AdminInitJobsAPI = axios.create({
    baseURL: 'http://' + DATA_SERVER + ':60000/api/admin',
    method: 'post'
})

// post: ADMIN UPLOAD_CASH_CSV_DATA_TO_DB API
const AdminUploadCSVDataAPI = axios.create({
    baseURL: 'http://' + DATA_SERVER + ':50000/api/write',
    method: 'post'
})
*/


