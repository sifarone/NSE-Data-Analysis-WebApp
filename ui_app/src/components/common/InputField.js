import React from 'react';

// Material-UI stuff
import TextField from '@material-ui/core/TextField';

class InputField extends React.Component {
    render () {
        return (
            <div>
                <TextField
                    id="input-field"
                    margin="normal"
                    autoComplete="off"
                    label={this.props.name}
                    value={this.props.value}
                    onChange={this.props.handleChange}
                    variant="outlined"
                />
            </div>
        )
    }
}

export default InputField;