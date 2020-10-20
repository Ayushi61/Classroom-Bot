import React from 'react'
import Card from 'react-bootstrap/card'
import Button from 'react-bootstrap/button'

function Main() {

    return (
        <div>
            <Card className="custom-card" style={{ width: '18rem' }}>
                <Card.Body>
                    <Card.Title>Data Configuration</Card.Title>
                    <Card.Text>
                        This page will allow you to administer the data for the Slack Bot to work on.
                    </Card.Text>
                    <Button href="/table/datasource" variant="primary">Start Data Configuration</Button>
                </Card.Body>
            </Card>
        </div>
    )
}

export default Main;