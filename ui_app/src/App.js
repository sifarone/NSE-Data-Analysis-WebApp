import React from 'react';
import { connect } from 'react-redux';
import {Switch, Route, Link} from 'react-router-dom';


import LoginPage from './components/LoginPage';
import AdminMain from './components/admin/AdminMain';

//import LoginPage from './components/LoginPage';
//import SigninPage from './components/SigninPage';
//import HomePage from './components/HomePage';
import ChartAppMain from './components/chartApp/ChartAppMain';


class App extends React.Component {
  render () {

    /*
    if (this.props.isLoggedIn === false) {
      return (
        <div>
          <LoginPage />
        </div>
      )
    } // end of if */
    

    return (
      <div>
        <Switch>
          <Route exact path='/' component={ChartAppMain}/>
          <Route path='/admin' component={this.props.isLoggedIn ? AdminMain : LoginPage}/>
        </Switch>       
      </div>
    )
  } // end of render()
}

const mapStateToProps = (state) => {
  return ({
    isLoggedIn : state.userInfo.isLoggedIn,
    isAdmin : state.userInfo.isAdmin
  });  
}

export default connect(mapStateToProps)(App);
