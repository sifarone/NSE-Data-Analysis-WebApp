import React from 'react';
import { connect } from 'react-redux';
import {Line} from 'react-chartjs-2'

import NativeSelect from '@material-ui/core/NativeSelect';
import Input from '@material-ui/core/Input';
import InputLabel from '@material-ui/core/InputLabel';
import FormControl from '@material-ui/core/FormControl';
import Button from '@material-ui/core/Button';

import { stkCashFutCallOptChartAction,
         stkCashFutPutOptChartAction } from '../../actions/ChartActions';

class ChartStkCashFutOpt extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            chartData: props.cdata, // Not to be used in chart rendering, props.cdata should be used
            strikePrice: this.props.combinedStkFnoInputParams.strikePrice
        }
    }

    setStrikePrice = (value) => {
        this.setState({strikePrice: value})
    }

    triggerAction = () => {
        //console.log('ChartCashFutOpt : --- combinedFnoInputParams : ',this.props.combinedFnoInputParams);
        //console.log('ChartCashFutOpt : --- strikePrice : ',this.state.strikePrice);

        if (this.props.optType === 'CE') {
            this.props.triggerCashFutCallOptChartAction(
                this.props.combinedStkFnoInputParams.symbol,
                this.props.combinedStkFnoInputParams.stkOptExpDate,
                this.state.strikePrice,
                this.props.combinedStkFnoInputParams.stkFutExpDate,
                this.props.combinedStkFnoInputParams.date
            )
        }
        else if (this.props.optType === 'PE') {
            this.props.triggerCashFutPutOptChartAction(
                this.props.combinedStkFnoInputParams.symbol,
                this.props.combinedStkFnoInputParams.stkOptExpDate,
                this.state.strikePrice,
                this.props.combinedStkFnoInputParams.stkFutExpDate,
                this.props.combinedStkFnoInputParams.date
            )
        }
        else {
            console.log('ChartCashFutOpt : ERROR')
        }
    }
    
    render() {
        //console.log('ChartCashFutOpt : >>> stockOptionInfo : ', Object.keys(this.props.stockOptionInfo).length);
        //console.log('ChartCashFutOpt : --- symbol : ',this.props.combinedFnoInputParams.symbol);
        //console.log('ChartCashFutOpt : --- optExpDate : ',this.props.combinedFnoInputParams.stkOptExpDate);
        return (
            <div>
                <table>
                    <tbody>
                        
                        <tr>
                            <td>
                            <FormControl>
                            <InputLabel shrink htmlFor="age-native-simple">Strike Price</InputLabel>
                            <NativeSelect 
                                value={this.state.strikePrice} 
                                input={<Input name="StrikePrice" id="StrikePrice-native-helper" />}
                                onChange={(e) => this.setStrikePrice(e.target.value)}
                            >
                                { (Object.keys(this.props.stockOptionInfo).length 
                                    && this.props.combinedStkFnoInputParams.symbol 
                                    && this.props.combinedStkFnoInputParams.stkOptExpDate) ?
                                        (this.props.stockOptionInfo[this.props.combinedStkFnoInputParams.symbol][this.props.combinedStkFnoInputParams.stkOptExpDate]).map((expDate, i) => 
                                            <option key={i} value={expDate}>{expDate}</option>)
                                        : <option value={'empty'}></option> 
                                }
                            </NativeSelect>
                            </FormControl>
                            </td>

                            <td>
                            <FormControl>
                            <Button variant="contained" onClick={() => this.triggerAction()}>
                              Get data
                            </Button>
                          </FormControl>
                          </td>
                        </tr>                       

                        <tr >
                            <td>
                            <div style={{ position: "relative", width: 700, height: 420}}>                        
                                <Line 
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
                                                stacked: true,
                                                position: 'right',
                                                id: 'y-axis-1'
                                            }
                                        ]
                                        }
                                    }}
                                
                                    data={{
                                        labels: this.props.cdata.date,
                                        datasets: [
                                            {
                                                type: 'line',
                                                borderWidth: 1,
                                                lineTesion: 0,
                                                fill: false,
                                                label: "Cash Price",
                                                //backgroundColor: "rgba(255, 0, 255, 0.75)",
                                                borderColor: 'red', // Line color
                                                data: this.props.cdata.closePrice,
                                                yAxisID : 'y-axis-0'
                                            },
                                            {
                                                type: 'line',
                                                borderWidth: 1,
                                                lineTesion: 0,
                                                fill: false,
                                                label: "Future Price",
                                                //backgroundColor: "rgba(255, 0, 255, 0.75)",
                                                borderColor: 'green', // Line color
                                                data: this.props.cdata.stkFutClosePrice,
                                                yAxisID : 'y-axis-0'
                                            },
                                            {
                                                type: 'line',
                                                borderWidth: 1,
                                                lineTesion: 0,
                                                fill: false,
                                                label: "Option Premium",
                                                //backgroundColor: "rgba(255, 0, 255, 0.75)",
                                                borderColor: 'blue', // Line color
                                                data: this.props.cdata.stkOptClosePrice,
                                                yAxisID : 'y-axis-1'
                                            }
                                        ]
                                    
                                    }}
                                
                                    //data={this.state.data}
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
        fnoSymbolList: state.chartData.fnoSymbolList,
        stockOptionInfo : state.chartData.stockOptionInfo,
        stockFutureInfo : state.chartData.stockFutureInfo,
        combinedStkFnoInputParams : state.chartData.combinedStkFnoInputParams,
    }
}


const mapDispatchToProps = (dispatch) => {
    return {
        triggerCashFutCallOptChartAction: (symbol, stkOptExpDate, strikePrice, stkFutExpDate, date) =>
                                             dispatch(stkCashFutCallOptChartAction(symbol, stkOptExpDate, strikePrice, stkFutExpDate, date)),
        triggerCashFutPutOptChartAction: (symbol, stkOptExpDate, strikePrice, stkFutExpDate, date) => 
                                            dispatch(stkCashFutPutOptChartAction(symbol, stkOptExpDate, strikePrice, stkFutExpDate, date))        
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(ChartStkCashFutOpt);
