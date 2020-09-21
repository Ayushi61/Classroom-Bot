import React, { Component } from "react";
import Form from "react-bootstrap/form";
import Button from "react-bootstrap/button";
import Alert from "react-bootstrap/alert";

class GroupForm extends Component {

  constructor(props) {
    super(props);
    this.state = {
      validated: false,
      show_alert: false,
      max_members: [...Array(5).keys()],
      participants: [
        {
          unity_id: "pchaudh5",
          name: "Prithviraj Chaudhuri"
        },
        {
          unity_id: "atrivedi",
          name: "Adarsh Trivedi"
        },
        {
          unity_id: "ayushi",
          name: "Ayushi Rajendran"
        }
      ]
    };
  }

  componentDidMount() {
    let number = this.props.match.params.number;
    if (number === "new") {
    } else {
    }
  }

  render() {
    return (
      <div>
        <div className="row">
          <div className="col-sm-2"></div>
          <div className="col-sm-8 form-box pad-top">
            <Form noValidate validated={this.state.validated.toString()}>
              <Form.Group controlId="GroupNo">
                <Form.Label>Group Number</Form.Label>
                <Form.Control required type="text" placeholder="Group no." />
                <Form.Text className="text-muted">
                  Please enter the Group number
              </Form.Text>
              </Form.Group>
              {this.state.max_members.map(i => (
                <Form.Group controlId={"member"+(i+1)}>
                  <Form.Label>Member {(i+1)}</Form.Label>
                  <Form.Control required as="select">
                    <option></option>
                    {this.state.participants.map(p => (
                      <option value={p.unity_id}>{p.name}</option>
                    ))}
                  </Form.Control>
                  <Form.Text className="text-muted">
                    Select a participant for the group
                  </Form.Text>
                </Form.Group>
              ))}

              <div className="row">
                <div className="col-sm-1.5">
                  <Button variant="outline-primary">Cancel</Button>
                </div>
                <div className="col-sm-1">
                  <Button variant="primary" type="Submit">
                    Save
                </Button>
                </div>
                <div className="col-sm-9">
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
}
export default GroupForm;
