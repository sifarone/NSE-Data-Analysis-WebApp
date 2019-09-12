import React from 'react';
import { Line } from 'react-chartjs-2'

const calculateEMA = (period, data) => {
    //console.log('calculateEMA: ', period, data)
    let returnData = {}
    let emaList = []
    const key = 'ema' + period.toString();
    if(data) {
        let historicalEma = data[0]
        const e = 2/(period + 1)
        for (let i = 0; i < data.length; i++) {
            let ema = (data[i] - historicalEma) * e + historicalEma
            historicalEma = ema
            emaList.push(ema)
        }
        returnData[key] = emaList
    }        
    else {
        returnData[key] = []
    } 
    console.log('calculateEMA: ', period, returnData[key])
    return returnData[key]
}

export default class ChartCashEMA extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            chartData: this.props.cdata    // Not to be used in chart rendering, props.cdata should be used         
        }
    }
    
    render() {
        
        return (
            <div style={{ width: 700, height: 420}}>
            {console.log('Child : ',this.props.cdata)}
            
            <Line 
                options={{
                    responsive:true,
                    title: {
                        display: true,
                        text: this.props.title
                    },
                    elements: {
                        point: {
                            radius: 0
                        }
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
                    labels: this.props.cdata.date,
                    datasets: [
                        {
                            type: 'line',
                            borderWidth: 1,
                            lineTesion: 0,
                            fill: false,
                            label: "Cash Price",
                            //backgroundColor: "rgba(255, 0, 255, 0.75)",
                            borderColor: 'black', // Line color
                            data: this.props.cdata.closePrice,
                            yAxisID : 'y-axis-0'
                        },
                        {
                            type: 'line',
                            borderWidth: 1,
                            lineTesion: 0,
                            fill: false,
                            label: "EMA5",
                            //pointStyle: 'line',
                            //backgroundColor: "rgba(255, 0, 255, 0.75)",
                            borderColor: 'brown', // Line color
                            data: calculateEMA(5, this.props.cdata.closePrice),
                            yAxisID : 'y-axis-1'
                        },
                        {
                            type: 'line',
                            borderWidth: 1,
                            lineTesion: 0,
                            fill: false,
                            label: "EMA9",
                            //backgroundColor: "rgba(255, 0, 255, 0.75)",
                            borderColor: 'green', // Line color
                            data: calculateEMA(9, this.props.cdata.closePrice),
                            yAxisID : 'y-axis-1'
                        },
                        {
                            type: 'line',
                            borderWidth: 1,
                            lineTesion: 0,
                            fill: false,
                            label: "EMA14",
                            //backgroundColor: "rgba(255, 0, 255, 0.75)",
                            borderColor: 'blue', // Line color
                            data: calculateEMA(14, this.props.cdata.closePrice),
                            yAxisID : 'y-axis-1'
                        },
                        {
                            type: 'line',
                            borderWidth: 1,
                            lineTesion: 0,
                            fill: false,
                            label: "EMA20",
                            //backgroundColor: "rgba(255, 0, 255, 0.75)",
                            borderColor: 'red', // Line color
                            data: calculateEMA(20, this.props.cdata.closePrice),
                            yAxisID : 'y-axis-1'
                        }
                    ]
                
                }}
            /> 
            </div>
        )
    }
}