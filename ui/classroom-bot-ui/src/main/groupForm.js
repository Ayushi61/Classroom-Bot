import React, { Component } from "react";
import Form from "react-bootstrap/form";
import Button from "react-bootstrap/button";
import Alert from "react-bootstrap/alert";
import GroupService from "../services/groupService";
import StudentService from "../services/studentService";
import CourseService from "../services/courseService";

class GroupForm extends Component {

  constructor(props) {
    super(props);
    this.state = {
      validated: false,
      show_alert: false,
      max_members: [...Array(5).keys()],
      participants: [],
      courses: []
    };
    this.submit = this.submit.bind(this);
    this.GroupService = new GroupService();
    this.StudentService = new StudentService();
    this.CourseService = new CourseService();
  }

  componentDidMount() {
    let number = "";
    if (this.props.match != null)
      number = this.props.match.params.number;
    let course = "new";
    if (this.props.match != null)
      course = this.props.match.params.course;
    if (course !== "new") {
      this.GroupService.getGroupData(course, number).then((response) => {
        Object.keys(response).forEach(element => {
          if (element !== 'students') {
            let ele = document.getElementById(element);
            if (ele !== null) {
              ele.value = response[element];
              ele.disabled = true;
            }
          } else {
          }
        });
      });
    } else {
      this.StudentService.getData().then(response => {
        this.setState({
          participants: response.rows
        });
      });

      this.CourseService.getData().then(response => {
        this.setState({
          courses: response.rows
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
    console.log(data);
    data.course_id = data.registered_course;
    data.group_number = parseInt(data.group_number);
    data.participants = [];
    this.state.max_members.forEach(element => {
      let participant = {};
      let member = data['member' + (element + 1)].split('|');
      if (member.length === 3) {
        participant.email_id = member[1];
        participant.student_unity_id = member[0];
        participant.name = member[2];
        data.participants.push(participant);
      }
    });
    console.log(data);
    this.GroupService.saveOne(data).then((response) => {
      console.log(response);
      if (response.length > 0) {
        this.setState({
          show_alert: true,
          alert_message: response
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
              <Form.Group controlId="group_number">
                <Form.Label>Group Number</Form.Label>
                <Form.Control required type="text" placeholder="Group no." />
                <Form.Text className="text-muted">
                  Please enter the Group number
              </Form.Text>
              </Form.Group>
              <Form.Group controlId="registered_course">
                <Form.Label>Course</Form.Label>
                <Form.Control required as="select">
                  <option></option>
                  {this.state.courses.map(c => (
                    <option key={Math.random()} value={c.id}>{c.department} {c.course_name}</option>
                  ))}
                </Form.Control>
                <Form.Text className="text-muted">
                  Select a participant for the group
                  </Form.Text>
              </Form.Group>
              {this.state.max_members.map(i => (
                <Form.Group key={Math.random()} controlId={"member" + (i + 1)}>
                  <Form.Label>Member {(i + 1)}</Form.Label>
                  {i < 3 ? (
                    <Form.Control required as="select">
                      <option></option>
                      {this.state.participants.map(p => (
                        <option key={Math.random()} value={p.student_unity_id + "|" + p.email_id + "|" + p.name}>{p.name}</option>
                      ))}
                    </Form.Control>
                  ) : (
                      <Form.Control as="select">
                        <option></option>
                        {this.state.participants.map(p => (
                          <option key={Math.random()} value={p.student_unity_id + "|" + p.email_id + "|" + p.name}>{p.name}</option>
                        ))}
                      </Form.Control>
                    )}
                  <Form.Text className="text-muted">
                    Select a participant for the group
                  </Form.Text>
                </Form.Group>
              ))}
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
        </div>
      </div>
    );
  }
}
export default GroupForm;
