import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import CircularProgress from '@material-ui/core/CircularProgress';

const useStyles = makeStyles(theme => ({
  progress: {
    margin: theme.spacing(2),
  },
}));

 const CircularIndeterminate = (props) => {
    const classes = useStyles();
  
    return (
      <div>
        <CircularProgress className={classes.progress} />
        <h4>{props.message}</h4>
        {/*<CircularProgress className={classes.progress} color="secondary" />*/}
      </div>
    );
  }

  CircularIndeterminate.defaultProps = {
      message: 'In Progress ...'
  }

  export default CircularIndeterminate;