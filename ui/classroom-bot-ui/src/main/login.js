import React, { Component } from 'react'
import Form from 'react-bootstrap/form'
import Button from 'react-bootstrap/button'
import { Redirect } from "react-router-dom";
import LoginService from '../services/loginService'
import Alert from 'react-bootstrap/alert'
import Cookies from 'js-cookie';

class Login extends Component {

  constructor(props) {
    super(props);
    this.state = {
      validated: false,
      show_alert: false,
      logged_in: false
    };
    this.loginService = new LoginService();
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  componentDidMount() {
    Cookies.remove('loggedInUser');
  }

  handleChange(event) {
    let obj = {};
    obj[event.target.id] = event.target.value;
    this.setState(obj);
  }

  handleSubmit(event) {
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
    let login = this.loginService.loginUser(data);
    if (login === false) {
      this.setState({
        show_alert: true,
        alert_message: "Incorrect Username or Password"
      })
    } else {
      Cookies.set('loggedInUser', login);
      this.setState({
        logged_in: true
      })
    }
  }

  render() {
    return (
      <div>
        {this.state.logged_in && (<Redirect to='/main'/>)}
        <div className="row centered">
          <div className="col-sm-3"></div>
          <div className="col-sm-6 form-box">
            <Form noValidate validated={this.state.validated.toString()} onSubmit={this.handleSubmit}>
              <Form.Group controlId="username">
                <Form.Label>Username</Form.Label>
                <Form.Control
                  required
                  type="text"
                  placeholder="username"
                  onChange={this.handleChange}
                />
                <Form.Text className="text-muted">
                  Please enter the admin username
                </Form.Text>
              </Form.Group>
              <Form.Group controlId="password">
                <Form.Label>Password</Form.Label>
                <Form.Control
                  required
                  type="password"
                  placeholder="Password"
                  onChange={this.handleChange}
                />
              </Form.Group>
              <div className="row">
                <div className="col-sm-2 custom-pad">
                  <Button
                    variant="primary"
                    type="Submit"
                  >
                    Submit
                  </Button>
                </div>
                <div className="col-sm-10 custom-pad">
                  <Alert key="1" variant="danger" show={this.state.show_alert}>
                    {this.state.alert_message}
                  </Alert>
                </div>
              </div>
            </Form>
          </div>
          <div className="col-sm-3"></div>
        </div>
      </div>
    );
  }
}

export default Login;
