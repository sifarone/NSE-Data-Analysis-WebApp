import React from 'react';

import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

const useStyles = makeStyles(theme => ({
    root: {
      width: '100%',
    },
    paper: {
      marginTop: theme.spacing(3),
      width: '100%',
      overflowX: 'auto',
      marginBottom: theme.spacing(2),
    },
    table: {
      minWidth: 650,
    },
    body: {
        fontSize: 10,
      },
  }));

const ChartIdxOptionChain = (props) => {
    const classes = useStyles();

    return (
        <Paper className={classes.root}>
        <Table className={classes.table} size="small">
          <TableHead>
            <TableRow>
              <TableCell style={{fontSize: 12}} align="center">OI</TableCell>
              <TableCell style={{fontSize: 12}} align="center">Chng in OI</TableCell>
              <TableCell style={{fontSize: 12}} align="center">Volume</TableCell>
              <TableCell style={{fontSize: 12}} align="center">LTP</TableCell>
              <TableCell style={{fontSize: 12}} align="center">Net Chng</TableCell>
              <TableCell style={{fontSize: 12}} align="center">StrikePrice</TableCell>
              <TableCell style={{fontSize: 12}} align="center">Net Chng</TableCell>
              <TableCell style={{fontSize: 12}} align="center">LTP</TableCell>
              <TableCell style={{fontSize: 12}} align="center">Volume</TableCell>
              <TableCell style={{fontSize: 12}} align="center">Chng in OI</TableCell>
              <TableCell style={{fontSize: 12}} align="center">OI</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {props.cdata.CE.strikePrice.map((sp, index) => (
                <TableRow key={index}>
                    <TableCell style={{fontSize: 10}} align="center">{props.cdata.CE.idxOptOpenInterest[index] ? props.cdata.CE.idxOptOpenInterest[index] : '-'}</TableCell>
                    <TableCell style={{fontSize: 10}} align="center">{props.cdata.CE.idxOptChangeInOpenInterest[index] ? props.cdata.CE.idxOptChangeInOpenInterest[index] : '-'}</TableCell>
                    <TableCell style={{fontSize: 10}} align="center">{props.cdata.CE.idxOptContracts[index] ? props.cdata.CE.idxOptContracts[index] : '-'}</TableCell>
                    <TableCell style={{fontSize: 10}} align="center">{props.cdata.CE.idxOptClosePrice[index] ? props.cdata.CE.idxOptClosePrice[index] : '-'}</TableCell>
                    <TableCell style={{fontSize: 10}} align="center">-</TableCell>
                    <TableCell style={{fontSize: 12}} align="center">{sp}</TableCell>
                    <TableCell style={{fontSize: 10}} align="center">-</TableCell>
                    <TableCell style={{fontSize: 10}} align="center">{props.cdata.PE.idxOptClosePrice[index] ? props.cdata.PE.idxOptClosePrice[index] : '-'}</TableCell>
                    <TableCell style={{fontSize: 10}} align="center">{props.cdata.PE.idxOptContracts[index] ? props.cdata.PE.idxOptContracts[index] : '-'}</TableCell>
                    <TableCell style={{fontSize: 10}} align="center">{props.cdata.PE.idxOptChangeInOpenInterest[index] ? props.cdata.PE.idxOptChangeInOpenInterest[index] : '-'}</TableCell>
                    <TableCell style={{fontSize: 10}} align="center">{props.cdata.PE.idxOptOpenInterest[index] ? props.cdata.PE.idxOptOpenInterest[index] : '-'}</TableCell>
                </TableRow>
            ))}
          </TableBody>
        </Table>
      </Paper>
    );
}

export default ChartIdxOptionChain;