import React, { Component } from "react";
import Form from "react-bootstrap/form";
import Button from "react-bootstrap/button";
import Alert from "react-bootstrap/alert";

class ClassForm extends Component {
  render() {
    return (
      <div>
        <div class="row">
          <div class="col-sm-2"></div>
          <div class="col-sm-8 form-box pad-top">
            <Form>
              <Form.Group controlId="courseName">
                <Form.Label>Course Name</Form.Label>
                <Form.Control type="text" placeholder="Name" />
                <Form.Text className="text-muted">
                  Please enter the course name
                </Form.Text>
              </Form.Group>
              <Form.Group controlId="semester">
                <Form.Label>Semester</Form.Label>
                <Form.Control type="text" placeholder="Semester" />
                <Form.Text className="text-muted">
                  Please enter the semester
                </Form.Text>
              </Form.Group>
              <Form.Group controlId="department">
                <Form.Label>Department</Form.Label>
                <Form.Control type="text" placeholder="Department" />
                <Form.Text className="text-muted">
                  Please enter the department
                </Form.Text>
              </Form.Group>
              <Form.Group controlId="workspace id">
                <Form.Label>WorkSpace ID</Form.Label>
                <Form.Control type="text" placeholder="Workspace id" />
                <Form.Text className="text-muted">
                  Please enter the Workspace Id
                </Form.Text>
              </Form.Group>
              <div class="row">
                <div class="col-sm-1.5">
                  <Button variant="outline-primary">Cancel</Button>
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
          <div class="col-sm-2"></div>
        </div>
      </div>
    );
  }
}

export default ClassForm;
