import React, { Component } from "react";
import Table from "react-bootstrap/Table";

class Datasource extends Component {

  constructor (props) {
    super(props);
    console.log(this.props.match.params);
    if (this.props.match.params.name === "datasource") {
      this.state = {
        columns: [
          "No.",
          "Action",
          "Table Name",
          "Description"
        ],
        rows: [
          {
            "No.":"1",
            "Link": "/table/class",
            "Table Name": "Class",
            "Description": "Table contains the class details"
          },
          {
            "No.":"2",
            "Link": "/table/students",
            "Table Name": "Student",
            "Description": "Table contains the students in the class"
          }
        ]
      }
    } else if(this.props.match.params.name === "class") {
      this.state = {
        columns: [
          "No.",
          "Action",
          "Class Name",
          "Team ID",
          "Semester"
        ],
        rows: [
          {
            "No.":"1",
            "Link": "/class",
            "Class Name": "CSC SE Fall 2020",
            "Team ID": "T001",
            "Semester": "Fall 2020"
          },
          {
            "No.":"2",
            "Link": "/class",
            "Class Name": "CSC SE Fall 2019",
            "Team ID": "T002",
            "Semester": "Fall 2019"
          }
        ]
      }
    } else if(this.props.match.params.name === "students") {
      this.state = {
        columns: [
          "No.",
          "Student Name",
          "Student ID",
          "Class",
          "Degree Level"
        ],
        rows: [
          {
            "No.":"1",
            "Student Name": "Prithviraj Chaudhuri",
            "Student ID": "pchaudh5",
            "Class": "CSC510 Fall 2020",
            "Degree Level": "Masters"
          },
          {
            "No.":"2",
            "Student Name": "Adarsh Trivedi",
            "Student ID": "atrivedi",
            "Class": "CSC510 Fall 2020",
            "Degree Level": "PhD"
          }
        ]
      }
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
                            return <td><a href={row[k]}>Edit</a></td>
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
