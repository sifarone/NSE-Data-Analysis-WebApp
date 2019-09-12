import React from 'react';
import { connect } from 'react-redux';

import LoadingIcon from '../common/LoadingIcon';

import { adminInitJobAction } from '../../actions/AdminActions';

class InitJobs extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            showLoadingIcon: false,
            actionResult : {}
        }
    }

    processJobs = async () => {
        
        this.setState({showLoadingIcon: true});

        await this.props.triggerInitJobs();
        
        this.setState({
          showLoadingIcon: false
        });
    }

    render () {
        return (
            <div>
                <label>
                    Trigger Daily Jobs : 
                    <button onClick={this.processJobs}>Trigger Jobs</button>
                </label>
                  
                { this.state.showLoadingIcon ? <LoadingIcon messgae="Jobs in Progress ..." /> : '' }              
                { Object.keys(this.props.adminInitJobStatus).map((key, i) => <h4 key={i}>{key} : {this.props.adminInitJobStatus[key]}</h4>) } 
            </div>
        )
    }
}

const mapStateToProps = (state) => {
    return {
        adminInitJobStatus: state.adminJobs.adminInitJobStatus
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        triggerInitJobs: (symbol) => dispatch(adminInitJobAction())
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(InitJobs);
