import React from 'react';
import { connect } from 'react-redux';

import LoadingIcon from '../common/LoadingIcon';

import { adminLoadCashDataAction,
        adminLoadFnODataAction } from '../../actions/AdminActions';

class UploadDataToDB extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            showCashDataLoadingIcon: false,
            showFnOLoadingIcon: false,
            indexDataLoadStatus : {}
        }
    }

    loadCashData = async () => {
        this.setState({showCashDataLoadingIcon: true})

        await this.props.loadCashData()

        this.setState({
            showCashDataLoadingIcon: false
        })
    }

    loadFnoData = async () => {
        this.setState({showFnOLoadingIcon: true})

        await this.props.loadFnOData()

        this.setState({
            showFnOLoadingIcon: false
        })
    }

    loadIndexData = async () => { }

    render () {
        return (
            <div>
                <table>
                    <tbody>
                        <tr>
                            <td>
                                <label>
                                    Load Cash Data : 
                                    <button onClick={this.loadCashData}>Load Data</button>
                                </label>
                            </td>

                            <td>
                                { this.state.showCashDataLoadingIcon ? <LoadingIcon message="Loading Cash CSV Data to DB ..."/> : '' }
                            </td>
                        </tr>

                        <tr>
                            <td>
                                <label>
                                    Load Fno Data : 
                                    <button onClick={this.loadFnoData}>Load Data</button>
                                </label>
                            </td>

                            <td>
                                { this.state.showFnOLoadingIcon ? <LoadingIcon message="Loading FnO CSV Data to DB ..."/> : '' }
                            </td>
                        </tr>

                        <tr>
                            { Object.keys(this.props.adminLoadCashDataStatus).map((key, i) => <h4 key={i}>{key} : {this.props.adminLoadCashDataStatus[key]}</h4>) } 
                            { Object.keys(this.props.adminLoadFnODataStatus).map((key, i) => <h4 key={i}>{key} : {this.props.adminLoadFnODataStatus[key]}</h4>) } 
                        </tr>
                    </tbody>
                </table>                    
            </div>
        )
    }
}

const mapStateToProps = (state) => {
    return {
        adminLoadCashDataStatus: state.adminJobs.adminLoadCashDataStatus,
        adminLoadFnODataStatus: state.adminJobs.adminLoadFnODataStatus
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        loadCashData: () => dispatch(adminLoadCashDataAction()),
        loadFnOData: () => dispatch(adminLoadFnODataAction())
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(UploadDataToDB);