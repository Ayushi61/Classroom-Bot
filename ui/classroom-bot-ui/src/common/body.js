import React from "react";
import { BrowserRouter as Router, Route, Redirect } from "react-router-dom";
import Main from "../main/main";
import Datasource from "../main/datasource";
import Commands from "../main/commands";
import CommandForm from "../main/commandForm";
import Login from "../main/login";

function Body() {
  const loggedIn = true; // Needs to be brought from service

  return (
    <div>
      <Router>
        <Route exact path="/" component={Main} />
        <Route exact path="/commands" component={Commands} />
        <Route exact path="/commands/:command" component={CommandForm} />
        <Route exact path="/datasource" component={Datasource} />
        <Route exact path="/login" component={Login} />
        {!loggedIn ? <Redirect to="/login" /> : <div></div>}
      </Router>
    </div>
  );
}

export default Body;
