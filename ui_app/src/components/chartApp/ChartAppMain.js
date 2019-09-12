import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { makeStyles } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import AppBar from '@material-ui/core/AppBar';
import CssBaseline from '@material-ui/core/CssBaseline';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import { ExpansionPanel } from '@material-ui/core';

import StkFnOMenu from './StkFnOMenu';
import CashMenu from './CashMenu';
import ChartCashEMA from './ChartCashEMA';
import IdxFnOMenu from './IdxFnOMenu';
import ChartCashPriceVsDelivPerc from './ChartCashPriceVsDelivPerc';
import ChartStkCashFutOpt from './ChartStkCashFutOpt';
import ChartStkOptOIvsChOI from './ChartStkOptOIvsChOI';
import ChartIdxOptOIvsChOI from './ChartIdxOptOIvsChOI';
import StkOptionChainMenu from './StkOptionChainMenu';
import IdxOptionChainMenu from './IdxOptionChainMenu';
import ChartStkOptionChain from './ChartStkOptionChain';
import ChartIdxOptionChain from './ChartIdxOptionChain';

import AdminMain from '../../components/admin/AdminMain';

import {
  initialDataChartAction
 } from '../../actions/ChartActions';

const drawerWidth = 300;

const useStyles = makeStyles(theme => ({
  root: {
    display: 'flex',
  },
  appBar: {
    zIndex: theme.zIndex.drawer + 1,
    height: 60,
  },
  toolBar: {
    height: 60,
  },
  drawer: {
    width: drawerWidth,
    flexShrink: 0
  },
  drawerPaper: {
    width: drawerWidth,
    background: "#b0bec5"
  },
  content: {
    flexGrow: 1,
    padding: theme.spacing(3),
    background: "#cfd8dc"
  },
  toolbar: theme.mixins.toolbar,
})); 

const ChartAppMain = () => {
  const classes = useStyles();
  const dispatch = useDispatch();
  useEffect(() => {dispatch(initialDataChartAction())},[dispatch])

  const [section, setSection] = useState('fnoAnalysis');

  const isLoggedIn  = useSelector((state) => state.userInfo.isLoggedIn);
  const isAdmin     = useSelector((state) => state.userInfo.isAdmin);

  const cashStockSymbolList   = useSelector((state) => state.chartData.cashStockSymbolList);
  const fnoStockSymbolList    = useSelector((state) => state.chartData.fnoStockSymbolList);  
  const fnoIndexSymbolList    = useSelector((state) => state.chartData.fnoIndexSymbolList);
  const stockOptionInfo       = useSelector((state) => state.chartData.stockOptionInfo);
  const stockFutureInfo       = useSelector((state) => state.chartData.stockFutureInfo);
  const indexOptionInfo       = useSelector((state) => state.chartData.indexOptionInfo);
  const indexFutureInfo       = useSelector((state) => state.chartData.indexFutureInfo);
  
  const cashData          = useSelector((state) => state.chartData.cashData);
  const cashFnOData       = useSelector((state) => state.chartData.cashFnOData);
  const stk_pe_oivsdoi    = useSelector((state) => state.chartData.stk_pe_oivsdoi);
  const stk_ce_oivsdoi    = useSelector((state) => state.chartData.stk_ce_oivsdoi);
  const stk_ce_cashOptFut = useSelector((state) => state.chartData.stk_ce_cashOptFut);
  const stk_pe_cashOptFut = useSelector((state) => state.chartData.stk_pe_cashOptFut);
  const idx_pe_oivsdoi    = useSelector((state) => state.chartData.idx_pe_oivsdoi);
  const idx_ce_oivsdoi    = useSelector((state) => state.chartData.idx_ce_oivsdoi);
  const stk_optionChain   = useSelector((state) => state.chartData.stk_optionChain);
  const idx_optionChain   = useSelector((state) => state.chartData.idx_optionChain);

  // Display Selecetd Section component ---------------------------------------------------------------
  const displaySelectedSection = () => {
    if (section === 'stkFnoAnalysis') {
      return (  
        <div>
            <table>
              <tbody>
                  <tr>
                      <td style={{border:"1px solid"}}>
                          { cashFnOData ? 
                              <ChartCashPriceVsDelivPerc 
                                    cdata={cashFnOData} 
                                    title={'Stock Price Vs Delivery Percentage'}/>
                              : <div></div>
                          }
                      </td>

                      <td style={{border:"1px solid"}}>
                          {
                            Object.keys(cashFnOData).length ?
                            <ChartCashEMA
                                cdata={cashFnOData} 
                                title={'EMA'} />
                            : <ChartCashEMA
                                cdata={cashFnOData['closePrice'] = []} 
                                title={'EMA'} />
                          }
                      </td>
                  </tr>
  
                  <tr>
                      <td style={{border:"1px solid"}}>
                          { stk_ce_oivsdoi ?
                              <ChartStkOptOIvsChOI 
                                    cdata={stk_ce_oivsdoi} 
                                    title={'CALL: OI vs Change in OI'}
                                    optType={'CE'} />
                              : <div></div>
                          }
                      </td>

                      <td style={{border:"1px solid"}}>
                          { stk_ce_cashOptFut ?
                              <ChartStkCashFutOpt 
                                    cdata={stk_ce_cashOptFut} 
                                    title={'CALL: Cash Vs Future Vs Option'}
                                    optType={'CE'} />
                              : <div></div>
                          }
                      </td>
                  </tr>
  
                  <tr>
                      <td style={{border:"1px solid"}}>
                          { stk_pe_oivsdoi ?
                              <ChartStkOptOIvsChOI 
                                    cdata={stk_pe_oivsdoi} 
                                    title={'PUT: OI vs Change in OI'}
                                    optType={'PE'} />
                              : <div></div>
                          }
                      </td>

                      <td style={{border:"1px solid"}}>
                          { stk_pe_cashOptFut ?
                              <ChartStkCashFutOpt 
                                    cdata={stk_pe_cashOptFut} 
                                    title={'PUT: Cash Vs Future Vs Option'} 
                                    optType={'PE'} />
                              : <div></div>
                          }
                      </td>
                  </tr>
              </tbody>
            </table>
        </div>
      )
    }
    else if (section === 'idxFnoAnalysis') {
      return (
        <div>
          <table>
            <tbody>
              <tr>
                <td style={{border:"1px solid"}}>
                <div >
                    { idx_ce_oivsdoi ?
                      <ChartIdxOptOIvsChOI 
                            cdata={idx_ce_oivsdoi} 
                            title={'CALL: OI vs Change in OI'}
                            optType={'CE'} />
                      : <div></div>
                    }
                  </div>
                </td>
              </tr>

              <tr>
                <td style={{border:"1px solid"}}>
                <div>
                    { idx_pe_oivsdoi ?
                      <ChartIdxOptOIvsChOI 
                            cdata={idx_pe_oivsdoi} 
                            title={'PUT: OI vs Change in OI'}
                            optType={'PE'} />
                      : <div></div>
                    }
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      )
    }
    else if (section === 'cashAnalysis') {
      return (
        <table>
          <tbody>
            <tr>
              <td style={{border:"1px solid"}}>
                  {
                    cashData ?
                    <ChartCashPriceVsDelivPerc 
                        cdata={cashData} 
                        title={'Stock Price Vs Delivery Percentage'} />
                    : <div></div>
                  }
              </td>

              <td style={{border:"1px solid"}}>
                  {
                    Object.keys(cashData).length ?
                    <ChartCashEMA
                        cdata={cashData} 
                        title={'EMA'} />
                    : <ChartCashEMA
                        cdata={cashData['closePrice'] = []} 
                        title={'EMA'} />
                  }
              </td>
            </tr>
          </tbody>
        </table>
      )
    }
    else if (section === 'stkOptionChain') {
      return (
        <div>
          { Object.keys(stk_optionChain).length ?
            <ChartStkOptionChain 
                  cdata={stk_optionChain} 
                  title={'Stock OptionChain'} />
            : <div></div>
          }
        </div>
      )
    }
    else if (section === 'idxOptionChain') {
      return (
        <div>
          { Object.keys(idx_optionChain).length ?
            <ChartIdxOptionChain 
                  cdata={idx_optionChain} 
                  title={'Index OptionChain'} />
            : <div></div>
          }
        </div>
      )
    }
    else if (section === 'admin') {
      return (
        <AdminMain />
      )
    }
    else {
      return (
        <div>
          Nothing selected
        </div>
      )
    }
  }

  // Display Admin page ----------------------------------------------------------------------
  const showAdmin = () => {
    console.log('showAdmin: isLoggedIn | is Admin > ', isLoggedIn, isAdmin);

    if (isLoggedIn === true && isAdmin === true) {
      setSection('admin');
    }
  }

  // The main chart component ----------------------------------------------------------------------
  return (
    
    <div className={classes.root}>

      <CssBaseline />

      <AppBar position="fixed" className={classes.appBar}>
        <Toolbar className={classes.toolBar}>
          <Typography variant="h6" noWrap>
            EOD Analysis (Beta V1.1)
          </Typography>
          <Button color="inherit" style={{marginRight: -12, marginLeft: "auto"}} onClick={() => showAdmin()}>Admin</Button>
        </Toolbar>
      </AppBar>

      <Drawer
        className={classes.drawer}
        variant="permanent"
        classes={{
          paper: classes.drawerPaper,
        }}
      >
          <ExpansionPanel style={{paddingTop:'60px'}} onClick={() => setSection('cashAnalysis')}>
            <CashMenu 
              cashStockSymbolList = {cashStockSymbolList} />  
          </ExpansionPanel>

          <ExpansionPanel onClick={() => setSection('stkFnoAnalysis')}>
            <StkFnOMenu 
              fnoStockSymbolList    = {fnoStockSymbolList} 
              stockOptionInfo       = {stockOptionInfo} 
              stockFutureInfo       = {stockFutureInfo} />
          </ExpansionPanel>

          <ExpansionPanel onClick={() => setSection('idxFnoAnalysis')}>
            <IdxFnOMenu 
              fnoIndexSymbolList    = {fnoIndexSymbolList} 
              indexOptionInfo       = {indexOptionInfo} 
              indexFutureInfo       = {indexFutureInfo} />
          </ExpansionPanel>

          <ExpansionPanel onClick={() => setSection('stkOptionChain')}>
            <StkOptionChainMenu 
              fnoStockSymbolList    = {fnoStockSymbolList}
              stockOptionInfo       = {stockOptionInfo} />
          </ExpansionPanel>

          <ExpansionPanel onClick={() => setSection('idxOptionChain')}>
            <IdxOptionChainMenu 
              fnoIndexSymbolList    = {fnoIndexSymbolList} 
              indexOptionInfo       = {indexOptionInfo} />
          </ExpansionPanel>

      </Drawer>

      <main className={classes.content}>
        <div className={classes.toolbar} />
         { displaySelectedSection() }
      </main>
    </div>
  );
}

export default ChartAppMain;
