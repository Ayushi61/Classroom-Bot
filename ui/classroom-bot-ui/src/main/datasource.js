import React, { Component } from "react";
import Table from "react-bootstrap/Table";
import Button from "react-bootstrap/Button";

class Datasource extends Component {

  constructor(props) {
    super(props);
    if (this.props.match.params.name === "datasource") {
      this.state = {
        excel_upload: false,
        columns: [
          "No.",
          "Action",
          "Table Name",
          "Description"
        ],
        rows: [
          {
            "No.": "1",
            "Link": "/table/class",
            "Table Name": "Class",
            "Description": "Table contains the class details"
          },
          {
            "No.": "2",
            "Link": "/table/students",
            "Table Name": "Student",
            "Description": "Table contains the students in the class"
          }
        ]
      }
    } else if (this.props.match.params.name === "class") {
      this.state = {
        excel_upload: false,
        columns: [
          "No.",
          "Action",
          "Class Name",
          "Team ID",
          "Semester"
        ],
        rows: [
          {
            "No.": "1",
            "Link": "/class",
            "Class Name": "CSC SE Fall 2020",
            "Team ID": "T001",
            "Semester": "Fall 2020"
          },
          {
            "No.": "2",
            "Link": "/class",
            "Class Name": "CSC SE Fall 2019",
            "Team ID": "T002",
            "Semester": "Fall 2019"
          }
        ]
      }
    } else if (this.props.match.params.name === "students") {
      this.state = {
        excel_upload: true,
        columns: [
          "No.",
          "Student Name",
          "Student ID",
          "Class",
          "Degree Level"
        ],
        rows: [
          {
            "No.": "1",
            "Student Name": "Prithviraj Chaudhuri",
            "Student ID": "pchaudh5",
            "Class": "CSC510 Fall 2020",
            "Degree Level": "Masters"
          },
          {
            "No.": "2",
            "Student Name": "Adarsh Trivedi",
            "Student ID": "atrivedi",
            "Class": "CSC510 Fall 2020",
            "Degree Level": "PhD"
          }
        ]
      }
    }
    this.triggerInputFile = this.triggerInputFile.bind(this);
    this.fileChanged = this.fileChanged.bind(this);
  }

  triggerInputFile (event) {
    this.fileInput.click();
  }

  fileChanged (event) {
    console.log(event.target.files[0]);
  }

  render() {
    return (
      <div>
        <div className="container-fluid">
          <div className="row">
            {this.state.excel_upload ? (
              <div className="row table-div">
                <Button variant="primary" type="button" className="custom-btn" onClick={this.triggerInputFile}>
                  Upload
                  </Button>
                <input type="file" className="file-upload" ref={fileInput => this.fileInput = fileInput} onChange={this.fileChanged}/>
                <Button variant="primary" type="button" disabled className="custom-btn">
                  Save
                  </Button>
              </div>
            ) : (
                <div></div>
              )
            }
            <div className="col-sm-12 table-div">
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
