import React from 'react'
import Form from 'react-bootstrap/form'
import Button from 'react-bootstrap/button'

function Login () {
    return (
        <div>
            <div class="row centered">
                <div class="col-sm-3">

                </div>
                <div class="col-sm-6 form-box">
                    <Form>
                        <Form.Group controlId="username">
                            <Form.Label>Username</Form.Label>
                            <Form.Control type="text" placeholder="Username" />
                            <Form.Text className="text-muted">
                                Please enter the admin username
                            </Form.Text>
                        </Form.Group>
                        <Form.Group controlId="password">
                            <Form.Label>Password</Form.Label>
                            <Form.Control type="password" placeholder="Password" />
                        </Form.Group>
                        <Button variant="primary" type="Submit">
                            Submit
                        </Button>
                    </Form>
                </div>
                <div class="col-sm-3">

                </div>
            </div>
        </div>
    )
}

export default Login;