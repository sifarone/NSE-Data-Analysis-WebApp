import React from 'react';
import InitJobs from './InitJobs';
import UploadDataToDB from './UploadDataToDB';
import UploadCSVFilesToServer from './UploadCSVFilesToServer';
import DeleteDataFromDB from './DeleteDataFromDB';
import AddUser from './AddUser';

export default class AdminMain extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            actions : []
        }
    }

    render () {
        return (
            <div>
                <InitJobs />
                <hr />
                <UploadDataToDB />
                <hr />
                <UploadCSVFilesToServer />
                <hr />
                <DeleteDataFromDB />
                <hr />
                <AddUser />
            </div>
        )
    }
}