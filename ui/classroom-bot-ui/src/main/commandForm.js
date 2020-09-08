import React from 'react'
import Form from 'react-bootstrap/form'
import Button from 'react-bootstrap/button'
import Alert from 'react-bootstrap/alert'

function CommandForm (props) {

    console.log(props.match.params.command);
    
    return (
        <div>
            <div class="row">
                <div class="col-sm-2">

                </div>
                <div class="col-sm-8 form-box pad-top">
                    <Form>
                        <Form.Group controlId="commandName">
                            <Form.Label>Command Name</Form.Label>
                            <Form.Control type="text" placeholder="Name" />
                            <Form.Text className="text-muted">
                                Please enter the command name
                            </Form.Text>
                        </Form.Group>
                        <Form.Group controlId="commandTemplate">
                            <Form.Label>Command Template</Form.Label>
                            <Form.Control type="text" placeholder="Template" />
                            <Form.Text className="text-muted">
                                Please enter the command template. Please enter the command template in the format VERB TYPE [ARG1] [ARG2] e.g. get document doc1
                            </Form.Text>
                        </Form.Group>
                        <Form.Group controlId="dataSource">
                            <Form.Label>Data Source</Form.Label>
                            <Form.Control as="select" custom>
                                <option>Groups</option>
                                <option>Documents</option>
                            </Form.Control>
                            <Form.Text className="text-muted">
                                Select the datasource
                            </Form.Text>
                        </Form.Group>
                        <Form.Group controlId="method">
                            <Form.Label>Method</Form.Label>
                            <Form.Control as="select" custom>
                                <option>setGroupData (data)</option>
                                <option>getGroupData (data)</option>
                            </Form.Control>
                            <Form.Text className="text-muted">
                                Select the service method to associate with this command
                            </Form.Text>
                        </Form.Group>
                        <Form.Group controlId="access">
                            <Form.Label>Access Control</Form.Label>
                            <Form.Control as="select" custom>
                                <option>Admin</option>
                                <option>User</option>
                                <option>Custom</option>
                            </Form.Control>
                            <Form.Text className="text-muted">
                                Select the role that you wanna give the access to
                            </Form.Text>
                        </Form.Group>
                        <Form.Group>
                            <Form.Check 
                                type="checkbox"
                                id="active"
                                label="Active"
                            />
                        </Form.Group>
                        <div class="row">
                            <div class="col-sm-1.5">
                                <Button variant="outline-primary">
                                    Cancel
                                </Button>
                            </div>
                            <div class="col-sm-1">
                                <Button variant="primary" type="Submit">
                                    Save
                                </Button>
                            </div>
                            <div class="col-sm-9">
                                <Alert key="1" variant="danger">
                                    This is a danger alert—check it out!
                                </Alert>
                            </div>
                        </div>
                    </Form>
                </div>
                <div class="col-sm-2">

                </div>
            </div>
        </div>
    )
}

export default CommandForm;