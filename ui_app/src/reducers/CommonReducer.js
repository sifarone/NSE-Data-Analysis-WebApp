
const initialState = {
    currentSection: 'login'
}

export const commonReducer = (state=initialState, action) => {

    switch (action.type) {
        case 'CURRENT_SECTION':
            console.log('reducer called : action ', action)
            return {
                ...state,
                ...action.payload
            }

        default:
            return state
    }
}