import React from 'react'
import Card from 'react-bootstrap/card'
import { Chart } from 'react-charts'

function Main() {

    const data = React.useMemo(
        () => [
            {
                label: 'Series 1',
                data: [[0, 1], [1, 2], [2, 4], [3, 2], [4, 7]]
            },
            {
                label: 'Series 2',
                data: [[0, 3], [1, 1], [2, 5], [3, 6], [4, 4]]
            }
        ],
        []
    )
    const series = React.useMemo(() => ({ type: 'bar' }), [])
    const series2 = React.useMemo(
        () => ({
          type: 'bubble',
          showPoints: false
        }),
        []
      )
    const axes = React.useMemo(
        () => [
            { primary: true, type: 'linear', position: 'bottom' },
            { type: 'linear', position: 'left' }
        ],
        []
    )


    return (
        <div>
            <div class="row">
                <div class="col-sm-6 card-block">
                    <Card>
                        <Card.Body>
                            <Card.Title>Graph 1</Card.Title>
                            <div class="chart-container">
                                <Chart data={data} axes={axes} />
                            </div>
                        </Card.Body>
                    </Card>
                </div>
                <div class="col-sm-6 card-block">
                    <Card>
                        <Card.Body>
                            <Card.Title>Graph 2</Card.Title>
                            <div class="chart-container">
                                <Chart
                                    data={data}
                                    series={series}
                                    axes={axes}
                                    primaryCursor
                                />
                            </div>
                        </Card.Body>
                    </Card>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-12 card-block">
                    <Card>
                        <Card.Body>
                            <Card.Title>Graph 3</Card.Title>
                            <div class="chart-container">
                                <Chart
                                    data={data}
                                    series={series2}
                                    axes={axes}
                                    grouping="single"
                                    tooltip
                                />
                            </div>
                        </Card.Body>
                    </Card>
                </div>
            </div>
        </div>
    )
}

export default Main;