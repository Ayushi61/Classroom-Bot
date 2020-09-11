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
    this.downloadTemplate = this.downloadTemplate.bind(this);
  }

  triggerInputFile (event) {
    this.fileInput.click();
  }

  fileChanged (event) {
    console.log(event.target.files[0]);
  }

  downloadTemplate (event) {
    let csv_text = "";
    csv_text = this.state.columns.join(',') + '\n';
    this.state.rows.forEach( function(row){
      let i = 0;
      let columns = Object.keys(row);
      columns.forEach( function(c) {
        if (i === 0)
          csv_text += row[c];
        else
          csv_text += ',' + row[c];
        i ++;
      });
      csv_text += '\n';
    });
    var uri = encodeURIComponent(csv_text);
    var link = document.createElement("a");
    link.setAttribute("href", 'data:text/csv;charset=utf-8,' + uri);
    link.setAttribute("download", "template.csv");
    document.body.appendChild(link);
    link.click();
  }

  render() {
    return (
      <div>
        <div className="container-fluid">
          <div className="row">
            {this.state.excel_upload ? (
              <div className="row table-div">
                <Button variant="outline-primary" type="button" className="custom-btn" onClick={this.downloadTemplate}>
                  Download
                </Button>
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
