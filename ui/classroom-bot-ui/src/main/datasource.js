import React from "react";
import Table from "react-bootstrap/Table";
import {
  BrowserRouter as Router,
  Route,
  Redirect,
  Link,
} from "react-router-dom";
import Group from "./group";

function Datasource() {
  return (
    <div>
      <div class="container-fluid">
        <div class="row">
          <div class="col-sm-12 table-div">
            <Table striped bordered hover size="sm">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Name</th>
                  <th>Description</th>
                  <th>Active</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>1</td>
                  <td>
                    <Link to="/datasource/group">Group</Link>
                  </td>
                  <td>@Bot retrieve values from group [document]</td>
                  <td>False</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>
                    <a href="/datasource/doc">Documents</a>
                  </td>
                  <td>@Bot retrieve values from documents [document]</td>
                  <td>False</td>
                </tr>
              </tbody>
            </Table>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Datasource;
