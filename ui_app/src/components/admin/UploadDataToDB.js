import React from 'react';
import { connect } from 'react-redux';

import LoadingIcon from '../common/LoadingIcon';

import { adminLoadCashDataAction,
        adminLoadArchivedCashDataAction,
        adminLoadFnODataAction,
        adminLoadIndexDataAction,
        adminLoadArchivedIndexDataAction } from '../../actions/AdminActions';

class UploadDataToDB extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            showCashDataLoadingIcon         : false,
            showArchCashDataLoadingIcon     : false,
            showFnOLoadingIcon              : false,
            showIndexLoadingIcon            : false,
            showArchIndexLoadingIcon        : false,
            indexDataLoadStatus             : {}
        }
    }

    loadCashData = async () => {
        this.setState({showCashDataLoadingIcon: true})

        await this.props.loadCashData()

        this.setState({
            showCashDataLoadingIcon: false
        })
    }

    loadArchivedCashData = async () => {
        this.setState({showArchCashDataLoadingIcon: true})

        await this.props.loadArchivedCashData()

        this.setState({
            showArchCashDataLoadingIcon: false
        })
    }

    loadFnoData = async () => {
        this.setState({showFnOLoadingIcon: true})

        await this.props.loadFnOData()

        this.setState({
            showFnOLoadingIcon: false
        })
    }

    loadIndexData = async () => {
        this.setState({showIndexLoadingIcon: true})

        await this.props.loadIndexData()

        this.setState({
            showIndexLoadingIcon: false
        })
    }

    loadArchivedIndexData = async () => {
        this.setState({showArchIndexLoadingIcon: true})

        await this.props.loadArchivedIndexData()

        this.setState({
            showArchIndexLoadingIcon: false
        })
    }

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
                                    Load Archived Cash Data : 
                                    <button onClick={this.loadArchivedCashData}>Load Data</button>
                                </label>
                            </td>

                            <td>
                                { this.state.showArchCashDataLoadingIcon ? <LoadingIcon message="Loading Archived Cash CSV Data to DB ..."/> : '' }
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
                            <td>
                                <label>
                                    Load Index Data : 
                                    <button onClick={this.loadIndexData}>Load Data</button>
                                </label>
                            </td>

                            <td>
                                { this.state.showIndexLoadingIcon ? <LoadingIcon message="Loading Index CSV Data to DB ..."/> : '' }
                            </td>
                        </tr>

                        <tr>
                            <td>
                                <label>
                                    Load Archived Index Data : 
                                    <button onClick={this.loadArchivedIndexData}>Load Data</button>
                                </label>
                            </td>

                            <td>
                                { this.state.showArchIndexLoadingIcon ? <LoadingIcon message="Loading Archived Index CSV Data to DB ..."/> : '' }
                            </td>
                        </tr>

                        <tr>
                            { Object.keys(this.props.adminLoadCashDataStatus).map((key, i) => <h4 key={i}>{key} : {this.props.adminLoadCashDataStatus[key]}</h4>) } 
                            { Object.keys(this.props.adminLoadArchivedCashDataStatus).map((key, i) => <h4 key={i}>{key} : {this.props.adminLoadArchivedCashDataStatus[key]}</h4>) }
                            { Object.keys(this.props.adminLoadFnODataStatus).map((key, i) => <h4 key={i}>{key} : {this.props.adminLoadFnODataStatus[key]}</h4>) } 
                            { Object.keys(this.props.adminLoadIndexDataStatus).map((key, i) => <h4 key={i}>{key} : {this.props.adminLoadIndexDataStatus[key]}</h4>) }
                            { Object.keys(this.props.adminLoadArchivedIndexDataStatus).map((key, i) => <h4 key={i}>{key} : {this.props.adminLoadArchivedIndexDataStatus[key]}</h4>) }
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
        adminLoadArchivedCashDataStatus: state.adminJobs.adminLoadArchivedCashDataStatus,
        adminLoadFnODataStatus: state.adminJobs.adminLoadFnODataStatus,
        adminLoadIndexDataStatus: state.adminJobs.adminLoadIndexDataStatus,
        adminLoadArchivedIndexDataStatus: state.adminJobs.adminLoadArchivedIndexDataStatus
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        loadCashData: () => dispatch(adminLoadCashDataAction()),
        loadArchivedCashData: () => dispatch(adminLoadArchivedCashDataAction()),
        loadFnOData: () => dispatch(adminLoadFnODataAction()),
        loadIndexData: () => dispatch(adminLoadIndexDataAction()),
        loadArchivedIndexData: () => dispatch(adminLoadArchivedIndexDataAction())
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(UploadDataToDB);