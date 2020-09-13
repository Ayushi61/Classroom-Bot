import React from "react";
// import { useState } from "react";
import Form from "react-bootstrap/form";
import Button from "react-bootstrap/button";
import Alert from "react-bootstrap/alert";

function GroupForm() {
  // const data = [
  //   { Name: "Rashi", id: 1 },
  //   { Name: "Ayushi", id: 2 },
  //   { Name: "Adarsh", id: 3 },
  //   { Name: "Prithvi", id: 4 },
  //   { Name: "Prithviraj", id: 5 },
  // ];

  // const [options] = useState(data);
  return (
    <div>
      <div class="row">
        <div class="col-sm-2"></div>
        <div class="col-sm-8 form-box pad-top">
          <Form>
            <Form.Group controlId="GroupID">
              <Form.Label>Group ID</Form.Label>
              <Form.Control type="text" placeholder="Group id" />
              <Form.Text className="text-muted">
                Please enter the Group ID
              </Form.Text>
            </Form.Group>
            <Form.Group controlId="GroupNo">
              <Form.Label>Group Number</Form.Label>
              <Form.Control type="text" placeholder="Group no." />
              <Form.Text className="text-muted">
                Please enter the Group number
              </Form.Text>
            </Form.Group>
            <Form.Group controlId="ProjName">
              <Form.Label>Project Name</Form.Label>
              <Form.Control type="text" placeholder="Proj name" />
              <Form.Text className="text-muted">
                Please enter the Project Name
              </Form.Text>
            </Form.Group>
            <Form.Group controlId="student">
              <Form.Label>Students</Form.Label>
              <div style={{ width: "90%", display: "flex" }}>
                
              </div>
              <Form.Text className="text-muted">
                Select the name of the students in a group
              </Form.Text>
            </Form.Group>
            <Form.Group>
              <Form.Check type="checkbox" id="active" label="Active" />
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
      </div>
    </div>
  );
}
export default GroupForm;
