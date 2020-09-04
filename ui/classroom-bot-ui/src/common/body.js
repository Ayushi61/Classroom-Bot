import React from "react";
import { BrowserRouter as Router, Route, Redirect } from "react-router-dom";
import Main from "../main/main";
import Datasource from "../main/datasource";
import Commands from "../main/commands";
import Login from "../main/login";
import Group from "../main/group";

function Body() {
  const loggedIn = true; // Needs to be brought from service

  return (
    <div>
      <Router>
        <Route exact path="/" component={Main} />
        <Route exact path="/commands" component={Commands} />
        <Route exact path="/datasource" component={Datasource} />
        <Route exact path="/login" component={Login} />
        <Route exact path="/datasource/group" component={Group} />
        {!loggedIn ? <Redirect to="/login" /> : <div></div>}
      </Router>
    </div>
  );
}

export default Body;
