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
      width: '60%',
      alignSelf: 'center'    
    },
    paper: {
      marginTop: theme.spacing(3),
      width: '100%',
      overflowX: 'auto',
      marginBottom: theme.spacing(2),
    },
    table: {
      //minWidth: 650,
      borderBlock: 1
    },
    body: {
        fontSize: 10,
      },
  }));

const ChartStkOptionChain = (props) => {
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
                    <TableCell style={{fontSize: 10}} align="center">{props.cdata.CE.stkOptOpenInterest[index] ? props.cdata.CE.stkOptOpenInterest[index] : '-'}</TableCell>
                    <TableCell style={{fontSize: 10}} align="center">{props.cdata.CE.stkOptChangeInOpenInterest[index] ? props.cdata.CE.stkOptChangeInOpenInterest[index] : '-'}</TableCell>
                    <TableCell style={{fontSize: 10}} align="center">{props.cdata.CE.stkOptContracts[index] ? props.cdata.CE.stkOptContracts[index] : '-'}</TableCell>
                    <TableCell style={{fontSize: 10}} align="center">{props.cdata.CE.stkOptClosePrice[index] ? props.cdata.CE.stkOptClosePrice[index] : '-'}</TableCell>
                    <TableCell style={{fontSize: 10}} align="center">-</TableCell>
                    <TableCell style={{fontSize: 12}} align="center">{sp}</TableCell>
                    <TableCell style={{fontSize: 10}} align="center">-</TableCell>
                    <TableCell style={{fontSize: 10}} align="center">{props.cdata.PE.stkOptClosePrice[index] ? props.cdata.PE.stkOptClosePrice[index] : '-'}</TableCell>
                    <TableCell style={{fontSize: 10}} align="center">{props.cdata.PE.stkOptContracts[index] ? props.cdata.PE.stkOptContracts[index] : '-'}</TableCell>
                    <TableCell style={{fontSize: 10}} align="center">{props.cdata.PE.stkOptChangeInOpenInterest[index] ? props.cdata.PE.stkOptChangeInOpenInterest[index] : '-'}</TableCell>
                    <TableCell style={{fontSize: 10}} align="center">{props.cdata.PE.stkOptOpenInterest[index] ? props.cdata.PE.stkOptOpenInterest[index] : '-'}</TableCell>
                </TableRow>
            ))}
          </TableBody>
        </Table>
      </Paper>
    );

    /*
    return (
      <table>
        <thead>
          <tr>
            <th>OI</th>
            <th>Chng in OI</th>
            <th>Volume</th>
            <th>LTP</th>
            <th>Net Chng</th>
            <th>StrikePrice</th>
            <th>Net Chng</th>
            <th>LTP</th>
            <th>Volume</th>
            <th>Chng in OI</th>
            <th>OI</th>
          </tr>
        </thead>

        <tbody>
          {props.cdata.CE.strikePrice.map((sp, index) => (
            <tr>
              <td style={{alignContent:'center'}}>{props.cdata.CE.stkOptOpenInterest[index] ? props.cdata.CE.stkOptOpenInterest[index] : '-'}</td>
              <td style={{alignContent:'center'}}>{props.cdata.CE.stkOptChangeInOpenInterest[index] ? props.cdata.CE.stkOptChangeInOpenInterest[index] : '-'}</td>
              <td style={{alignContent:'center'}}>{props.cdata.CE.stkOptContracts[index] ? props.cdata.CE.stkOptContracts[index] : '-'}</td>
              <td style={{alignContent:'center'}}>{props.cdata.CE.stkOptClosePrice[index] ? props.cdata.CE.stkOptClosePrice[index] : '-'}</td>
              <td>-</td>
              <td>{sp}</td>
              <td>-</td>
              <td>{props.cdata.PE.stkOptClosePrice[index] ? props.cdata.PE.stkOptClosePrice[index] : '-'}</td>
              <td>{props.cdata.PE.stkOptContracts[index] ? props.cdata.PE.stkOptContracts[index] : '-'}</td>
              <td>{props.cdata.PE.stkOptChangeInOpenInterest[index] ? props.cdata.PE.stkOptChangeInOpenInterest[index] : '-'}</td>
              <td>{props.cdata.PE.stkOptOpenInterest[index] ? props.cdata.PE.stkOptOpenInterest[index] : '-'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    ); */
}

export default ChartStkOptionChain;