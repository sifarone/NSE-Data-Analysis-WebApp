import { LoginAPI } from '../APIs';
import { SigninAPI } from '../APIs';

// User Login action
export const userLoginAction = (username, password) => {
    return async function(dispatch, getState) {
        console.log('=====> userLoginAction: triggered > ', username, password);

        const post_body = {
            username: username,
            password: password
        }

        const response =  await fetch(LoginAPI, {
            method: 'POST',
            body: JSON.stringify(post_body)
        })

        const jsonData = await response.json()
        //console.log('=====> status: ', jsonData);

        let isLoggedIn = false;

        if (jsonData.status === 'pass') {
            isLoggedIn = true;
        }
        else {
            isLoggedIn = false;
        }

        dispatch(
            {
                type: 'USER_LOGIN',
                payload: {
                    isLoggedIn: isLoggedIn,
                    isAdmin: true
                }
            }
        ) 
    }
}

// User Logout action
export const userLogoutAction = () => {
    //console.log('=====> userLogoutAction: triggered');
    return {
        type: 'USER_LOGOUT',
        payload: {
            isLoggedIn: false,
            isAdmin: false
        }
    }
}

// User Signin action
export const userSigninAction = (username, password) => {
    return async function(dispatch, getState) {

        const post_body = {
            username: username,
            password: password
        }

        const response =  await fetch(SigninAPI, {
            method: 'POST',
            body: JSON.stringify(post_body)
        })

        const jsonData = await response.json()
        //console.log('=====> status: ', jsonData);

        let signinStatus = 'fail';

        if (jsonData.status === 'pass') {
            signinStatus = 'pass';
        }
        else {
            signinStatus = 'fail';
        }

        dispatch(
            {
                type: 'USER_SIGNIN',
                payload: {
                    userSigninStatus: signinStatus
                }
            }
        ) 
    }
}