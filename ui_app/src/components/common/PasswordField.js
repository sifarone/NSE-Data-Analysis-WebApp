import React from 'react';

// Material-UI stuff
import TextField from '@material-ui/core/TextField';

class PasswordField extends React.Component {
    render () {
        return (
            <div>
                <TextField
                    id="password-field"
                    margin="normal"
                    label="Password"
                    type="password"
                    value={this.props.value}
                    onChange={this.props.handleChange}
                    variant="outlined"
                />
            </div>
        )
    }
}

export default PasswordField;