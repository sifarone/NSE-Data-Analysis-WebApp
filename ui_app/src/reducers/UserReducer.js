
const initialState = {
    isLoggedIn: false,
    isAdmin: false,
    userSigninStatus: 'fail'
}

export const userReducer = (state=initialState, action) => {

    switch (action.type) {
        case 'USER_LOGIN':
            console.log('reducer called : action ', action)
            return {
                ...state,
                ...action.payload
            }

        case 'USER_LOGOUT':
            console.log('reducer called : action ', action)
            return {
                ...state,
                ...action.payload
            }

        case 'USER_SIGNIN':
            console.log('reducer called : action ', action)
            return {
                ...state,
                ...action.payload
            }

        default:
            return state
    }
}