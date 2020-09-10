import React, { Component } from "react";
import { BrowserRouter as Router, Route, Redirect } from "react-router-dom";
import Main from "../main/main";
import Datasource from "../main/datasource";
import ClassForm from "../main/classForm";
import Login from "../main/login";

class Body extends Component {

  constructor(props) {
      super(props);
      this.loggedIn = this.props.app.logged_in;
  }

  render () {
    return (
      <div>
        <Router>
          <Route exact path="/" component={Main} />
          <Route exact path="/main" component={Main} />
          <Route exact path="/table/:name" component={Datasource} />
          <Route exact path="/form/class" component={ClassForm} />
          <Route exact path="/login" component={() => <Login app={this.props.app} /> } />
          {!this.loggedIn ? <Redirect to="/login" /> : <div></div>}
        </Router>
      </div>
    );
  }
}

export default Body;
