import React from 'react';
import { Redirect} from 'react-router';
import { connect } from 'react-redux';

import InputField from './common/InputField';
import PasswordField from './common/PasswordField';
import { userLoginAction } from '../actions/UserActions';

class LoginPage extends React.Component {
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

    processloginStatus = (isLoggedIn) => {
        //console.log('processloginStatus : isLoggedIn: ', isLoggedIn)
        if (isLoggedIn === true) {
            //console.log('processloginStatus redirect : isLoggedIn: ', isLoggedIn)
            return (
                <Redirect to="/home" />
            )
        }
        else if (isLoggedIn === false) {
            return (
                <div>
                    <h3>User Authentication Failed!!</h3>
                    <InputField name="User Name" value={this.state.userName} handleChange={this.handleUserNameInput}/>
                    <PasswordField value={this.state.password} handleChange={this.handlePasswordInput}/>
                    <button onClick={() => this.props.userLogin(this.state.userName, this.state.password)}>Login</button>
                </div>
                
            )
        }
        else {
            return (
                <div>
                    <InputField name="User Name" value={this.state.userName} handleChange={this.handleUserNameInput}/>
                    <PasswordField value={this.state.password} handleChange={this.handlePasswordInput}/>
                    <button onClick={() => this.props.userLogin(this.state.userName, this.state.password)}>Login</button>
                </div>
            )  
        }
    }

    render() {
        //console.log('LoginPage: userStattus > ', this.props.isLoggedIn);
        return (
            <div style={{margin:"0 auto", width: "200px"}}>
               {this.processloginStatus(this.props.isLoggedIn)}
            </div>
        )
    }
}

const mapStateToProps = (state) => {
    return {
        isLoggedIn: state.userInfo.userStatus
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        userLogin: (username, password) => dispatch(userLoginAction(username, password))
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(LoginPage);
