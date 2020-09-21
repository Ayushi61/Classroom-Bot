import React, { Component } from "react";
import Form from "react-bootstrap/form";
import Button from "react-bootstrap/button";
import Alert from "react-bootstrap/alert";
import CourseService from '../services/courseService'

class CourseForm extends Component {

  constructor(props) {
    super(props);
    this.CourseService = new CourseService();
    this.submit = this.submit.bind(this);
    this.state = {
      validated: false,
      show_alert: false
    };
  }

  componentDidMount() {
    let workspace_id = "new";
    if (this.props.match != null) 
      workspace_id = this.props.match.params.id;
    if (workspace_id !== "new") {
      this.CourseService.getCourseData(workspace_id).then((response) => {
        Object.keys(response).forEach(element => {
          let ele = document.getElementById(element);
          if (ele !== null) {
            ele.value = response[element];
            ele.disabled = true;
          }
        });
      });
    }
  }

  submit(event) {
    let form = event.currentTarget;
    event.preventDefault();
    event.stopPropagation();
    if (form.checkValidity() === false) {
      this.setState({
        validated: false
      })
    }
    let data = {};
    Array.from(form.elements).forEach(element => {
      data[element.id] = element.value;
    });
    data['bot_token'] = Math.floor(100000 + Math.random() * 900000);
    data['admin_user_id'] = "id";
    this.CourseService.saveOne(data).then((success) => {
      if (success) {
        this.setState({
          show_alert: true,
          alert_message: "Data successfully updated"
        });
      } else {
        this.setState({
          show_alert: true,
          alert_message: "Some error occured and data not saved"
        });
      }
    });
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
                <div className="col-sm-2">
                  <Button className="custom-form-btn" variant="primary" type="Submit">
                    Save
                  </Button>
                </div>
                <div className="col-sm-2">
                  <Button className="custom-form-btn" variant="outline-primary" href="/table/course">Cancel</Button>
                </div>
                <div className="col-sm-8">
                  <Alert key="1" variant="danger" show={this.state.show_alert}>
                    {this.state.alert_message}
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
