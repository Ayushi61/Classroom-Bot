import React, { Component } from "react";
import { BrowserRouter as Router, Route, Redirect } from "react-router-dom";
import Main from "../main/main";
import Datasource from "../main/datasource";
import CourseForm from "../main/courseForm";
import GroupForm from "../main/groupForm";
import Login from "../main/login";
import Cookies from 'js-cookie';

class Body extends Component {
  constructor(props) {
    super(props);
    if (Cookies.get('loggedInUser') == null)
      this.state = {
        loggedIn: false
      };
    else
    this.state = {
      loggedIn: true
    };
  }

  render() {
    return (
      <div>
        <Router>
          <Route exact path="/" component={Main} />
          <Route exact path="/main" component={Main} />
          <Route exact path="/table/:name" component={Datasource} />
          <Route exact path="/form/course/:id" component={CourseForm} />
          <Route exact path="/form/group/:course/:number" component={GroupForm} />
          <Route exact path="/form/group/:course" component={GroupForm} />
          <Route
            exact
            path="/login"
            component={() => <Login app={this.props.app} />}
          />
          {!this.state.loggedIn ? <Redirect to="/login" /> : <div></div>}
        </Router>
      </div>
    );
  }
}

export default Body;
