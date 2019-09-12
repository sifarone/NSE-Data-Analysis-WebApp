import React from 'react';
import { connect } from 'react-redux';

import LoadingIcon from '../common/LoadingIcon';

import { adminDeleteCashDataAction,
        adminDeleteStockFnODataAction,
        adminDeleteIndexFnODataAction,
        adminDeleteIndexDataAction } from '../../actions/AdminActions';

class DeleteDataFromDB extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            stkExpiryDate : '',
            idxExpiryDate : '',
            showCashDataLoadingIcon: false,
            showFnOLoadingIcon: false,
            indexDataLoadStatus : {}
        }
    }

    deleteCashData = async () => {
        this.setState({showCashDataLoadingIcon: true})

        await this.props.deleteCashData()

        this.setState({
            showCashDataLoadingIcon: false
        })
    }

    deleteStockFnoData = async () => {
        this.setState({showFnOLoadingIcon: true})

        await this.props.deleteStockFnOData(this.state.stkExpiryDate)

        this.setState({
            showFnOLoadingIcon: false
        })
    }

    deleteIndexFnoData = async () => {
        this.setState({showFnOLoadingIcon: true})

        await this.props.deleteIndexFnOData(this.state.idxExpiryDate)

        this.setState({
            showFnOLoadingIcon: false
        })
    }

    handleOnStkExpDateChange = (e) => {
        this.setState({
            stkExpiryDate: e.target.value
        })
    }

    handleOnIdxExpDateChange = (e) => {
        this.setState({
            idxExpiryDate: e.target.value
        })
    }

    deleteIndexData = async () => { }

    render () {
        return (
            <div>
                <table>
                    <tbody>
                        {/*
                        <tr>
                            <td>
                                <label>
                                    Delete Cash Data : 
                                    <button onClick={this.deleteCashData}>Delete Cash Data</button>
                                </label>
                            </td>

                            <td>
                                { this.state.showCashDataLoadingIcon ? <LoadingIcon message="Deleting Cash Data From DB ..."/> : '' }
                            </td>
                        </tr>
                        */}

                        <tr>
                            <td>
                                <label>
                                    Stock ExpiryDate
                                    <input type="text" value={this.state.stkExpiryDate} onChange={(e) => this.handleOnStkExpDateChange(e)}></input>
                                </label>
                                <label>
                                    Delete Stock Fno Data : 
                                    <button onClick={this.deleteStockFnoData}>Delete Stock FnO Data</button>
                                </label>
                            </td>

                            <td>
                                { this.state.showFnOLoadingIcon ? <LoadingIcon message="Deleting FnO Data From DB ..."/> : '' }
                            </td>
                        </tr>

                        <tr>
                            <td>
                                <label>
                                    Index ExpiryDate
                                    <input type="text" value={this.state.idxExpiryDate} onChange={(e) => this.handleOnIdxExpDateChange(e)}></input>
                                </label>
                                <label>
                                    Delete Index Fno Data : 
                                    <button onClick={this.deleteIndexFnoData}>Delete Index FnO Data</button>
                                </label>
                            </td>

                            <td>
                                { this.state.showFnOLoadingIcon ? <LoadingIcon message="Deleting FnO Data From DB ..."/> : '' }
                            </td>
                        </tr>

                        <tr>
                            { this.props.adminDeleteStockFnODataStatus } 
                            { this.props.adminDeleteIndexFnODataStatus } 
                        </tr>
                    </tbody>
                </table>                    
            </div>
        )
    }
}

const mapStateToProps = (state) => {
    return {
        adminDeleteCashDataStatus           : state.adminJobs.adminDeleteCashDataStatus,
        adminDeleteStockFnODataStatus       : state.adminJobs.adminDeleteStockFnODataStatus,
        adminDeleteIndexFnODataStatus       : state.adminJobs.adminDeleteIndexFnODataStatus,
        adminDeleteIndexDataStatus          : state.adminJobs.adminDeleteIndexDataStatus
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        deleteCashData          : (expDate) => dispatch(adminDeleteCashDataAction(expDate)),
        deleteStockFnOData      : (expDate) => dispatch(adminDeleteStockFnODataAction(expDate)),
        deleteIndexFnOData      : (expDate) => dispatch(adminDeleteIndexFnODataAction(expDate)),
        deleteIndexData         : (expDate) => dispatch(adminDeleteIndexDataAction(expDate))
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(DeleteDataFromDB);