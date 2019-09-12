import { combineReducers } from 'redux';

import { userReducer } from './UserReducer';
import { chartReducer } from './ChartReducer';
import { commonReducer } from './CommonReducer';
import { adminReducer } from './AdminReducer';

export default combineReducers({
    userInfo    : userReducer,
    chartData   : chartReducer,
    common      : commonReducer,
    adminJobs   : adminReducer
});