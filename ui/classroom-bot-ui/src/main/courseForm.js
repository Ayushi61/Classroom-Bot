import React, { Component } from "react";
import Form from "react-bootstrap/form";
import Button from "react-bootstrap/button";
import Alert from "react-bootstrap/alert";
import CourseService from '../services/courseService'

class CourseForm extends Component {

  constructor(props) {
    super(props);
    this.CourseService = new CourseService();
    this.isValid = this.isValid.bind(this);
    this.submit = this.submit.bind(this);
    this.state = {
      validated: false
    };
  }

  componentDidMount() {
    let workspace_id = this.props.match.params.id;
    if (workspace_id === "new") {
    } else {
      this.CourseService.getCourseData(workspace_id).then((response) => {
        Object.keys(response).forEach(element => {
          let ele = document.getElementById(element);
          if (ele !== null)
            document.getElementById(element).value = response[element];
        });
        document.getElementById('workspace_id').disabled = true;
      });
    }
  }

  isValid(event) {
    this.CourseService.isValid();
    console.log("Validating form");
  }

  submit(event) {
    const form = event.currentTarget;
    if (form.checkValidity() === false) {
      this.setState({
        validated: false
      })
      event.preventDefault();
      event.stopPropagation();
    }

    this.CourseService.saveOne();
    console.log("Submitting the form");
  }

  render() {
    return (
      <div>
        <div className="row">
          <div className="col-sm-2"></div>
          <div className="col-sm-8 form-box pad-top">
            <Form noValidate validated={this.state.validated.toString()} onSubmit={this.submit}>
              <Form.Group controlId="course_name">
                <Form.Label>Course Name</Form.Label>
                <Form.Control required type="text" placeholder="Name" />
                <Form.Text className="text-muted">
                  Please enter the course name
                </Form.Text>
              </Form.Group>
              <Form.Group controlId="semester">
                <Form.Label>Semester</Form.Label>
                <Form.Control required type="text" placeholder="Semester" />
                <Form.Text className="text-muted">
                  Please enter the semester
                </Form.Text>
              </Form.Group>
              <Form.Group controlId="department">
                <Form.Label>Department</Form.Label>
                <Form.Control required type="text" placeholder="Department" />
                <Form.Text className="text-muted">
                  Please enter the department
                </Form.Text>
              </Form.Group>
              <Form.Group controlId="workspace_id">
                <Form.Label>WorkSpace ID</Form.Label>
                <Form.Control required type="text" placeholder="Workspace id" />
                <Form.Text className="text-muted">
                  Please enter the Workspace Id
                </Form.Text>
              </Form.Group>
              <div className="row">
                <div className="col-sm-1">
                  <Button className="custom-form-btn" variant="primary" type="Submit">
                    Save
                  </Button>
                </div>
                <div className="col-sm-1">
                  <Button className="custom-form-btn" variant="outline-primary">Cancel</Button>
                </div>
                <div className="col-sm-10">
                  <Alert key="1" variant="danger">
                    This is a danger alert—check it out!
                  </Alert>
                </div>
              </div>
            </Form>
          </div>
          <div className="col-sm-2"></div>
        </div>
      </div>
    );
  }
}

export default CourseForm;
