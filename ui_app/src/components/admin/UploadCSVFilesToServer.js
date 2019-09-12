import React from 'react';
import { connect } from 'react-redux';

import { adminUploadCashCsvFileAction,
         adminUploadFnOCsvFileAction,
         adminUploadIndexCsvFileAction,
         adminDeleteCashDirAction,
         adminDeleteCashArchivedDirAction,
         adminDeleteFnODirAction,
         adminDeleteIndexDirAction,
         adminDeleteIndexArchivedDirAction } from '../../actions/AdminActions';

class UploadCSVFilesToServer extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            selectedCashCsvFile     : '',
            selectedFnOCsvFile      : '',
            selectedIndexCsvFile    : ''
        }
    }

    onCashCsvFileSelect = (e) => {
        this.setState({
            selectedCashCsvFile: e.target.files[0]
        })
        console.log('Files to be uploaded : ', this.state.selectedCashCsvFile)
    }

    onCashCsvFileSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append(this.state.selectedCashCsvFile.name, this.state.selectedCashCsvFile);

        this.props.loadCashCsvFile(formData)
    }

    onFnOCsvFileSelect = (e) => {
        this.setState({
            selectedFnOCsvFile: e.target.files[0]
        })
        console.log('Files to be uploaded : ', this.state.selectedFnOCsvFile)
    }

    onFnOCsvFileSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append(this.state.selectedFnOCsvFile.name, this.state.selectedFnOCsvFile);

        this.props.loadFnOCsvFile(formData)
    }

    onIndexCsvFileSelect = (e) => {
        this.setState({
            selectedIndexCsvFile: e.target.files[0]
        })
        console.log('Files to be uploaded : ', this.state.selectedIndexCsvFile)
    }

    onIndexCsvFileSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append(this.state.selectedIndexCsvFile.name, this.state.selectedIndexCsvFile);

        this.props.loadFnOCsvFile(formData)
    }

    render () {
        return (
            <div>
                <form onSubmit={(e) => this.onCashCsvFileSubmit(e)}>
                    <label>Upload Cash CSV File </label>
                    <input type="file" name="cashCsvFile" onChange={(e) => this.onCashCsvFileSelect(e) } />
                    <input type="submit" value="Upload" />
                </form>

                <h3>
                    {this.props.adminUploadCashCsvFileStatus}
                </h3>

                <form onSubmit={(e) => this.onFnOCsvFileSubmit(e)}>
                    <label>Upload FnO CSV File </label>
                    <input type="file" name="cashCsvFile" onChange={(e) => this.onFnOCsvFileSelect(e) } />
                    <input type="submit" value="Upload" />
                </form>

                <h3>
                    {this.props.adminUploadFnOCsvFileStatus}
                </h3>

                <form onSubmit={(e) => this.onIndexCsvFileSubmit(e)}>
                    <label>Upload Index CSV File </label>
                    <input type="file" name="cashCsvFile" onChange={(e) => this.onIndexCsvFileSelect(e) } />
                    <input type="submit" value="Upload" />
                </form>

                <h3>
                    {this.props.adminUploadIndexCsvFileStatus}
                </h3>

                <hr />

                <label>
                    Clear Cash Data Directory on Server 
                    <button onClick={() => this.props.clearCashDir()}>Clear Cash Dir</button>
                </label>

                <h3>
                    {this.props.adminDeleteCashDirStatus}
                </h3>

                <label>
                    Clear Cash Archived Data Directory on Server 
                    <button onClick={() => this.props.clearCashArchivedDir()}>Clear Cash Arch Dir</button>
                </label>

                <h3>
                    {this.props.adminDeleteCashArchivedDirStatus}
                </h3>

                <label>
                    Clear Cash FnO Data Directory on Server 
                    <button onClick={() => this.props.clearFnODir()}>Clear FnO Dir</button>
                </label>

                <h3>
                    {this.props.adminDeleteFnODirStatus}
                </h3>

                <label>
                    Clear Cash Index Data Directory on Server 
                    <button onClick={() => this.props.clearIndexDir()}>Clear Index Dir</button>
                </label>

                <h3>
                    {this.props.adminDeleteIndexDirStatus}
                </h3>

                <label>
                    Clear Cash Archived Index Data Directory on Server 
                    <button onClick={() => this.props.clearIndexArchivedDir()}>Clear Index Arch Dir</button>
                </label>

                <h3>
                    {this.props.adminDeleteIndexArchivedDirStatus}
                </h3>
                
            </div>
            
        );
    }
}


const mapStateToProps = (state) => {
    return {
        adminUploadCashCsvFileStatus        : state.adminJobs.adminUploadCashCsvFileStatus,
        adminUploadFnOCsvFileStatus         : state.adminJobs.adminUploadFnOCsvFileStatus,
        adminUploadIndexCsvFileStatus       : state.adminJobs.adminUploadIndexCsvFileStatus,
        adminDeleteCashDirStatus            : state.adminJobs.adminDeleteCashDirStatus,
        adminDeleteCashArchivedDirStatus    : state.adminJobs.adminDeleteCashArchivedDirStatus,
        adminDeleteFnODirStatus             : state.adminJobs.adminDeleteFnODirStatus,
        adminDeleteIndexDirStatus           : state.adminJobs.adminDeleteIndexDirStatus,
        adminDeleteIndexArchivedDirStatus   : state.adminJobs.adminDeleteIndexArchivedDirStatus
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        loadCashCsvFile         : (formData) => dispatch(adminUploadCashCsvFileAction(formData)),
        loadFnOCsvFile          : (formData) => dispatch(adminUploadFnOCsvFileAction(formData)),
        loadIndexCsvFile        : (formData) => dispatch(adminUploadIndexCsvFileAction(formData)),
        clearCashDir            : (formData) => dispatch(adminDeleteCashDirAction(formData)),
        clearCashArchivedDir    : (formData) => dispatch(adminDeleteCashArchivedDirAction(formData)),
        clearFnODir             : (formData) => dispatch(adminDeleteFnODirAction(formData)),
        clearIndexDir           : (formData) => dispatch(adminDeleteIndexDirAction(formData)),
        clearIndexArchivedDir   : (formData) => dispatch(adminDeleteIndexArchivedDirAction(formData))
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(UploadCSVFilesToServer);
