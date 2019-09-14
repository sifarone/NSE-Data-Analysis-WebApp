import React from 'react';
import {Bar} from 'react-chartjs-2';
//import Hammer from "hammerjs";
//import {zoom,pan} from 'chartjs-plugin-zoom';

export default class ChartIndexOpenClosePEratio extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            chartData: this.props.cdata    // Not to be used in chart rendering, props.cdata should be used         
        }
    }
    
    render() {
        return (

            <div>
                <table>
                    <tbody>                        
                        <tr>
                            <td>
                            <div style={{ width: 1000, height: 550}}>
            
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
                                    } /*,
                                    plugins: {
			                			zoom: {
			                				pan: {
			                					enabled: true,
			                					mode: 'x',
			                					speed: 10,
			                					threshold: 10
			                				},
			                				zoom: {
			                					enabled: true,
                                                mode: 'y',
                                                drag: true
			                				}
			                			}
			                		}*/
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
                                            borderColor: 'black', // Line color
                                            data: this.props.cdata.closingValue,
                                            yAxisID : 'y-axis-0'
                                        },
                                        {
                                            type: 'line',
                                            borderWidth: 1,
                                            fill: false,
                                            label: "Open Price",
                                            backgroundColor: "rgba(255, 0, 255, 0.75)",
                                            borderColor: 'blue', // Line color
                                            data: this.props.cdata.openValue,
                                            yAxisID : 'y-axis-0'
                                        },
                                        {
                                            type: 'bar',
                                            borderWidth: 2,
                                            fill: true,
                                            label: "PE Ratio",
                                            backgroundColor: "#ffa000",
                                            data: this.props.cdata.peRatio,
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