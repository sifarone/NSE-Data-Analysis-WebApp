import React from 'react';
import {Bar} from 'react-chartjs-2'

export default class CashChart extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            chartData: this.props.cdata    // Not to be used in chart rendering, props.cdata should be used         
        }
    }
    
    render() {
        return (
            <div style={{ width: 900, height: 420}}>
            {/*console.log('Child : ',this.props.chartData)*/}
            
            <Bar 
                options={{
                    responsive:true,
                    scales: {
                        yAxes: [{
                            gridLines: {
                                display: true
                            },
                            stacked: false,
                            position: 'left',
                            id: 'y-axis-0'
                        },
                        {
                            gridLines: {
                                display: false
                            },
                            stacked: false,
                            position: 'right',
                            id: 'y-axis-1'
                        }
                    ]
                    }
                }}

                data={ {
                    labels: this.props.cdata.date,
                    datasets: [
                        {
                            type: 'line',
                            borderWidth: 1,
                            fill: false,
                            label: "Closing Price",
                            backgroundColor: "rgba(255, 0, 255, 0.75)",
                            borderColor: 'blue', // Line color
                            data: this.props.cdata.closePrice,
                            yAxisID : 'y-axis-0'
                        },
                        {
                            type: 'bar',
                            borderWidth: 2,
                            fill: true,
                            label: "delivPer",
                            backgroundColor: "rgba(0, 255, 0, 0.75)",
                            data: this.props.cdata.delivPer,
                            yAxisID : 'y-axis-1'
                        }
                    ]
    
                }}
            />           
            </div>
        )
    }
}