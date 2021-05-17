import { createStore, applyMiddleware } from 'redux';
import { composWithDevTools } from 'redux-devtools-extension';
import thunk from 'redux-thunk';
import rootReducer from './reducers';

const initialState = {};

const middleware = [thunk];

const store = createStore(
    rootReducer,
    initialState,
    composWithDevTools(applyMiddleware(...middleware))
);

export default store;