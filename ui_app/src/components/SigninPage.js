import React from 'react';
//import { Redirect} from 'react-router';
import { connect } from 'react-redux';

import InputField from './common/InputField';
import PasswordField from './common/PasswordField';
import { userSigninAction } from '../actions/UserActions';

class SigninPage extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            userName        : '',
            password        : ''
        }
    }   

    handleUserNameInput = (event) => {
        this.setState({userName: event.target.value})
    }

    handlePasswordInput = (event) => {
        this.setState({password: event.target.value})
    }

    processSigninStatus = (userSigninStatus) => {
        console.log('processSigninStatus : userSigninStatus: ', userSigninStatus)
        if (userSigninStatus === 'pass') {
            console.log('processSigninStatus redirect : userSigninStatus: ', userSigninStatus)
            return (
                <h2>SignIn Success</h2>
            )
        }
        else if (userSigninStatus === 'fail') {
            return (
                <div>
                    <h3>User SignIn Failed!!</h3>
                    <InputField name="User Name" value={this.state.userName} handleChange={this.handleUserNameInput}/>
                    <PasswordField value={this.state.password} handleChange={this.handlePasswordInput}/>
                    <button onClick={() => this.props.userSignIn(this.state.userName, this.state.password)}>Login</button>
                </div>
                
            )
        }
        else {
            return (
                <div>
                    <h1>Sign In:</h1>
                    <InputField name="User Name" value={this.state.userName} handleChange={this.handleUserNameInput}/>
                    <PasswordField value={this.state.password} handleChange={this.handlePasswordInput}/>
                    <button onClick={() => this.props.userSignIn(this.state.userName, this.state.password)}>Sign In</button>
                </div>
            )  
        }
    }

    render() {
        console.log('SignIn Page: userSigninStatus > ', this.props.userSigninStatus);
        return (
            <div style={{margin:"0 auto", width: "200px"}}>
               {this.processSigninStatus(this.props.userSigninStatus)}
            </div>
        )
    }
}

const mapStateToProps = (state) => {
    return {
        userSigninStatus: state.userInfo.userSigninStatus
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        userSignIn: (username, password) => dispatch(userSigninAction(username, password))
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(SigninPage);
