import React, { useState } from 'react';
import { useDispatch } from 'react-redux';

import 'date-fns';
import { makeStyles } from '@material-ui/core/styles';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import NativeSelect from '@material-ui/core/NativeSelect';
import Input from '@material-ui/core/Input';
import InputLabel from '@material-ui/core/InputLabel';
import FormControl from '@material-ui/core/FormControl';
import Button from '@material-ui/core/Button';
import DateFnsUtils from '@date-io/date-fns';
import { MuiPickersUtilsProvider,
         KeyboardDatePicker} from '@material-ui/pickers';
import { ExpansionPanel,
          ExpansionPanelDetails,
          ExpansionPanelSummary
  } from '@material-ui/core';
import Typography from '@material-ui/core/Typography';

import { indexDataChartAction } from '../../actions/ChartActions';

const useStyles = makeStyles({
  root: {
    background: "#b0bec5"
  },
});

const CashMenu = (props) => {

  const classes = useStyles();
  const dispatch = useDispatch();

  const [symbol, setSymbol] = useState('');

  const getData = () => {
    /*console.log('symbol : ', symbol); */
    dispatch(indexDataChartAction(symbol));
  }

  //console.log('IndexMenu component : indexSymbolList > ', props.indexSymbolList)
  
  if (props.indexSymbolList.length) { 

    return (
      <ExpansionPanel className={classes.root}>
        <ExpansionPanelSummary
          expandIcon={<ExpandMoreIcon />}
          id="panel1a-header"
        >
          <Typography variant='body2'>Index Analysis</Typography>
        </ExpansionPanelSummary>

        <ExpansionPanelDetails>
          <FormControl className={classes.formControl}>
          <InputLabel shrink htmlFor="age-native-simple">Symbol</InputLabel>
            <NativeSelect
              style={{fontSize: 12}}
              value={symbol}
              input={<Input name="Symbol" id="Symbol-native-helper" />}
              onChange={(e) => setSymbol(e.target.value)}
            >
              {props.indexSymbolList.map((symbol, i) => <option style={{fontSize: 12}} key={i} value={symbol}>{symbol}</option>)}
            </NativeSelect>
          </FormControl>
        </ExpansionPanelDetails>
        
        <ExpansionPanelDetails>
          <FormControl className={classes.formControl}>
          <Button variant="contained" color="primary" className={classes.button} onClick={() => getData()}>
            Get data
          </Button>
          </FormControl>
        </ExpansionPanelDetails>

      </ExpansionPanel>
    );
  }
  else {
    return (
      <div>
        Not yet ready
      </div>
    )
  }
}

export default CashMenu;