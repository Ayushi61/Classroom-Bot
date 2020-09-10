import React, { Component }from "react";
import Table from "react-bootstrap/Table";

class Datasource extends Component {

  constructor (props) {
    super(props);
    this.state = {
      columns: [
        "No.",
        "Table Name",
        "Description",
        "Link"
      ],
      rows: [
        {
          "No.":"1",
          "Link": "/form/class",
          "Table Name": "Class",
          "Description": "Table contains the class details"
        }
      ]
    }
  }

  render () {
    return (
      <div>
        <div class="container-fluid">
          <div class="row">
            <div class="col-sm-12 table-div">
              <Table striped bordered hover size="sm">
                <thead>
                  <tr>
                    {this.state.columns.map(col => (
                      <th>
                        {col}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {this.state.rows.map(row => (
                    <tr>
                      {Object.keys(row).map(k => {
                          if (k === "Link") {
                            return <td><a href={row[k]}>Link</a></td>
                          } else {
                            return <td>{row[k]}</td>
                          }
                        }
                      )}
                    </tr>
                  ))}
                </tbody>
              </Table>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Datasource;
