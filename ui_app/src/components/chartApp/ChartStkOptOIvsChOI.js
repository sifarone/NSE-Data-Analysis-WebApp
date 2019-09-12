import React from 'react';
import { connect } from 'react-redux';
import { Bar } from 'react-chartjs-2';

import moment from 'moment';

import 'date-fns';
import DateFnsUtils from '@date-io/date-fns';
import InputLabel from '@material-ui/core/InputLabel';
import FormControl from '@material-ui/core/FormControl';
import Button from '@material-ui/core/Button';
import { MuiPickersUtilsProvider,
         KeyboardDatePicker} from '@material-ui/pickers';

import { stkCallOptOIvsDeltaOIChartAction,
    stkPutOptOIvsDeltaOIChartAction } from '../../actions/ChartActions';

class ChartStkOptOIvsChOI extends React.Component {
        constructor(props) {
            super(props)
    
            this.state = {
                chartData: props.cdata,   // Not to be used in chart rendering, props.cdata should be used
                date: new Date()         
            }
        }
        
        setSelectedDate = (value) => {
            this.setState({date: value})
        }

        triggerAction = () => {
            //console.log('ChartCashFutOpt : --- combinedFnoInputParams : ',this.props.combinedFnoInputParams);
            //console.log('ChartCashFutOpt : --- strikePrice : ',this.state.strikePrice);
    
            if (this.props.optType === 'CE') {
                this.props.triggerCallOIvsDeltaOIChartAction(
                    this.props.combinedStkFnoInputParams.symbol,
                    this.props.combinedStkFnoInputParams.stkOptExpDate,
                    this.props.combinedStkFnoInputParams.strikePrice,
                    this.props.combinedStkFnoInputParams.stkFutExpDate,
                    this.state.date
                )
            }
            else if (this.props.optType === 'PE') {
                this.props.triggerPutOIvsDeltaOIChartAction(
                    this.props.combinedStkFnoInputParams.symbol,
                    this.props.combinedStkFnoInputParams.stkOptExpDate,
                    this.props.combinedStkFnoInputParams.strikePrice,
                    this.props.combinedStkFnoInputParams.stkFutExpDate,
                    this.state.date
                )
            }
            else {
                console.log('ChartStkOptOIvsChOI : ERROR')
            }
        }
        
        render() {
            return (
                <div>
                    <table>
                        <tbody>
                            <tr style={{border:"1px solid"}}>
                                <td>
                                <MuiPickersUtilsProvider utils={DateFnsUtils}>
                                    <FormControl>
                                    <InputLabel shrink htmlFor="age-native-simple">Date</InputLabel>
                                      <KeyboardDatePicker
                                        disableToolbar
                                        variant="inline"
                                        format="dd-MMM-yyyy"
                                        margin="normal"
                                        id="date-picker-inline"
                                        value={this.state.date}
                                        onChange={(date) => this.setSelectedDate(moment(date).format('DD-MMM-YYYY'))}
                                        KeyboardButtonProps={{
                                          'aria-label': 'change date',
                                        }}
                                      />
                                    </FormControl>
                                </MuiPickersUtilsProvider>
                                </td>

                                <td>
                                <FormControl>
                                    <Button variant="contained" onClick={() => this.triggerAction()}>
                                        Get data
                                    </Button>
                                </FormControl>
                                </td>
                            </tr>

                            <tr>
                                <td>
                                <div style={{ position: "relative", width: 700, height: 420}}>
                                    <Bar 
                                        options={{
                                            responsive:true,
                                            title: {
                                                display: true,
                                                text: this.props.title
                                            },
                                            scales: {
                                                yAxes: [{
                                                    gridLines: {
                                                        display: true
                                                    },
                                                    //stacked: true,
                                                    position: 'left',
                                                    id: 'y-axis-0'
                                                },
                                                {
                                                    gridLines: {
                                                        display: false
                                                    },
                                                    //stacked: true,
                                                    position: 'right',
                                                    id: 'y-axis-1'
                                                }
                                            ]
                                            }
                                        }}
                                    
                                        data={{
                                            labels: this.props.cdata.strikePrice,
                                            datasets: [
                                                {
                                                    type: 'line',
                                                    borderWidth: 1,
                                                    lineTesion: 0,
                                                    lineColor: 'blue',
                                                    fill: false,
                                                    label: "Open Interest",
                                                    backgroundColor: "rgba(255, 0, 255, 0.75)",
                                                    borderColor: 'blue', // Line color
                                                    data: this.props.cdata.stkOptOpenInterest,
                                                    yAxisID : 'y-axis-0'
                                                },
                                                {
                                                    type: 'bar',
                                                    borderWidth: 2,
                                                    fill: true,
                                                    label: "Change in OI",
                                                    //backgroundColor: "rgba(0, 255, 0, 0.75)",
                                                    backgroundColor: "#ffa000",
                                                    data: this.props.cdata.stkOptChangeInOpenInterest,
                                                    yAxisID : 'y-axis-1'
                                                }
                                            ]
                                        
                                        }}    
                                    />           
                                </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>                
            )
        }
}

const mapStateToProps = (state) => {
    return {
        fnoStockSymbolList: state.chartData.fnoStockSymbolList,
        stockOptionInfo : state.chartData.stockOptionInfo,
        stockFutureInfo : state.chartData.stockFutureInfo,
        combinedStkFnoInputParams : state.chartData.combinedStkFnoInputParams,
    }
}


const mapDispatchToProps = (dispatch) => {
    return {
        triggerCallOIvsDeltaOIChartAction: (symbol, stkOptExpDate, strikePrice, stkFutExpDate, date) =>
                                             dispatch(stkCallOptOIvsDeltaOIChartAction(symbol, stkOptExpDate, strikePrice, stkFutExpDate, date)),
        triggerPutOIvsDeltaOIChartAction: (symbol, stkOptExpDate, strikePrice, stkFutExpDate, date) => 
                                            dispatch(stkPutOptOIvsDeltaOIChartAction(symbol, stkOptExpDate, strikePrice, stkFutExpDate, date))        
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(ChartStkOptOIvsChOI);
