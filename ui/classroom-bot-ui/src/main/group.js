import React from "react";
import Table from "react-bootstrap/Table";
import Editable from "react-x-editable";
//import FormGroup from 'react-bootstrap/esm/FormGroup';

function Group() {
  return (
    <div>
      <div class="container-fluid">
        <div class="row">
          <div class="col-sm-12 table-div">
            <Table striped bordered hover size="sm">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Group Name</th>
                  <th>Group Members</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>1</td>
                  <td>
                    <Editable
                      name="username"
                      dataType="text"
                      mode={"inline"}
                      placement="top"
                      title="Enter username"
                      value="Enter group name"
                    />
                  </td>
                  <td>
                    <Editable
                      name="username"
                      dataType="text"
                      title="Enter username"
                      showButtons={false}
                      validate={(value) => {
                        if (!value) {
                          return "Required";
                        }
                      }}
                    />
                  </td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>
                    <Editable
                      name="username"
                      dataType="text"
                      mode={"inline"}
                      title="Enter username"
                      value="Enter group name"
                    />
                  </td>
                  <td>
                    <Editable
                      name="username"
                      dataType="text"
                      title="Enter username"
                      showButtons={false}
                      validate={(value) => {
                        if (!value) {
                          return "Required";
                        }
                      }}
                    />
                  </td>
                </tr>
              </tbody>
            </Table>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Group;
