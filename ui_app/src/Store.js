import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import reducers from './reducers/ReducerMain'; // reducer is combineReducer

export default createStore(
    reducers,
    applyMiddleware(thunk)
);