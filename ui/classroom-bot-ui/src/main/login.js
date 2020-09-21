import React, { Component } from 'react'
import Form from 'react-bootstrap/form'
import Button from 'react-bootstrap/button'
import LoginService from '../services/loginService'
import Alert from 'react-bootstrap/alert'

class Login extends Component {
    
    constructor (props) {
        super(props);
        this.state = {
            username: '',
            password: ''
        }
        this.loginService = new LoginService();
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange (event) {
        let obj = {};
        obj[event.target.id] = event.target.value
        this.setState(obj);
    }

    async handleSubmit (event) {
        let alert_div = document.getElementsByClassName('alert-div')[0];
        alert_div.style.display = 'block';
        alert_div.querySelectorAll('.spinner-border')[0].style.display = "block";

        let response = await this.loginService.loginUser(this.state);
        if (response == null) {
            alert_div.querySelectorAll('.spinner-border')[0].style.display = "none";
            alert_div.querySelectorAll('.alert-text')[0].style.display = "block";
            alert_div.querySelectorAll('.alert-text')[0].innerHTML = "The process could not be completed";
        } else {
            alert_div.querySelectorAll('.spinner-border')[0].style.display = "none";
            alert_div.querySelectorAll('.alert-text')[0].style.display = "block";
            alert_div.querySelectorAll('.alert-text')[0].innerHTML = "Logged in";
            this.props.app.logged_in = true;
            this.props.app.user = response;
            window.location.href = '/main';
        }
        return false;
    }


    render() {
        return (
            <div>
                {/* {this.props.app.logged_in && (<Redirect to='/main'/>)} */}
                <div className="row centered">
                    <div className="col-sm-3">

                    </div>
                    <div className="col-sm-6 form-box">
                        <Form>
                            <Form.Group controlId="username">
                                <Form.Label>Username</Form.Label>
                                <Form.Control type="text" placeholder="Username" onChange={this.handleChange} />
                                <Form.Text className="text-muted">
                                    Please enter the admin username
                                </Form.Text>
                            </Form.Group>
                            <Form.Group controlId="password">
                                <Form.Label>Password</Form.Label>
                                <Form.Control type="password" placeholder="Password" onChange={this.handleChange} />
                            </Form.Group>
                            <div className="row">
                                <div className="col-sm-2 custom-pad">
                                    <Button variant="primary" type="Button" onClick={this.handleSubmit}>
                                        Submit
                                    </Button>
                                </div>
                                <div className="col-sm-10 custom-pad alert-div">
                                    <Alert key="1" variant="danger">
                                        <div className="spinner-border spinner-border-sm" role="status">
                                            <span className="sr-only">Loading...</span>
                                        </div>
                                        <span className="col-sm-10 alert-text">
                                        </span>
                                    </Alert>
                                </div>
                            </div>
                        </Form>
                    </div>
                    <div className="col-sm-3">

                    </div>
                </div>
            </div>
        );
    }
}

export default Login;