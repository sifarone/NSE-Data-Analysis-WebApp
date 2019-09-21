import React from 'react';
import { connect } from 'react-redux';

import { userSigninAction } from '../../actions/UserActions';

class AddUser extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            userName : '',
            passWord : '',
            isAdmin: false

        }
    }

    handleOnUserNameChange = (e) => {
        this.setState({
            userName: e.target.value
        })
    }

    handleOnPasswordChange = (e) => {
        this.setState({
            passWord: e.target.value
        })
    }

    handleOnIsAdminCheck = (e) => {
        this.setState({
            isAdmin: e.target.checked
        })
        //console.log('isAdmin : ', this.state.isAdmin)
    }

    createUser = () => {
        console.log('CreateUser : userName : ', this.state.userName)
        console.log('CreateUser : Password : ', this.state.passWord)
        console.log('CreateUser : IsAdmin : ', (this.state.isAdmin ? 'ADMIN' : 'USER'))
        this.props.userSignIn(this.state.userName, this.state.passWord, (this.state.isAdmin ? 'ADMIN' : 'USER'))
    }

    render () {
        return (
            <div>
            <table>
                    <tbody>
                        <tr>
                            <td>
                                <label>
                                    UserName
                                    <input type="text" autoComplete="off" value={this.state.userName} 
                                        onChange={(e) => this.handleOnUserNameChange(e)}></input>
                                </label>
                            </td>

                            <td>
                                <label>
                                    Password
                                    <input type="password" autoComplete="off" value={this.state.passWord} 
                                        onChange={(e) => this.handleOnPasswordChange(e)}></input>
                                </label>
                            </td>

                            <td>
                                <input type="checkbox" checked={this.state.isAdmin} 
                                    onChange={(e) => this.handleOnIsAdminCheck(e)} /> isAdmin<br />
                            </td>

                            <td>
                                <button onClick={this.createUser}>Create User</button>
                            </td>

                            <td>
                                {this.state.userSigninStatus}
                            </td>
                        </tr>                        
                        
                    </tbody>
                </table>       
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
        userSignIn: (username, password, usertype) => dispatch(userSigninAction(username, password, usertype))
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(AddUser);