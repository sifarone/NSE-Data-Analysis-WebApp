import React from 'react';
import { Redirect} from 'react-router';
import { connect } from 'react-redux';

class HomePage extends React.Component {
    render() {

        if (this.props.isLoggedIn === false) {
            return (
                <Redirect to='/login' />
            )
        }

        return (
            <div>
                <h2>this is the Home Page</h2>
                {/*console.log('HomePage Props: ', this.props)*/}
            </div>
        )
    }
}

const mapStateToProps = (state) => {
    return {
        userStatus: state.userInfo.isLoggedIn
    }
}

export default connect(mapStateToProps)(HomePage);