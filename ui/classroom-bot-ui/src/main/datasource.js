import React, { Component } from "react";
import Table from "react-bootstrap/Table";
import Button from "react-bootstrap/Button";
import CourseService from '../services/courseService'
import GroupService from "../services/groupService";

class Datasource extends Component {

  constructor(props) {
    super(props);
    this.state = {
      excel_upload: false,
      loaded: false,
      manual_add: false,
      columns: [],
      rows: []
    };
    this.triggerInputFile = this.triggerInputFile.bind(this);
    this.fileChanged = this.fileChanged.bind(this);
    this.downloadTemplate = this.downloadTemplate.bind(this);
    this.handleFile = this.handleFile.bind(this);
    this.convertToWord = this.convertToWord.bind(this);
  }

  triggerInputFile(event) {
    this.fileInput.click();
  }

  handleFile = (e) => {
    let data = e.target.result.split('\n');
    let i = 0;
    let temp = {};
    temp.excel_upload = true;
    temp.columns = [];
    temp.rows = [];
    data.forEach(function (row) {
      if (i === 0) {
        temp.columns = row.split(',');
      } else {
        let r = {};
        let j = 0;
        let t = row.split(',');
        t.forEach(function (item) {
          r[temp.columns[j++]] = item;
        });
        temp.rows.push(r);
      }
      i++;
    });
    temp.loaded = true;
    this.setState(temp);
  }

  fileChanged(event) {
    let f = event.target.files[0];
    var reader = new FileReader();
    reader.onloadend = this.handleFile;
    reader.readAsText(f);
  }

  downloadTemplate(event) {
    let csv_text = "";
    csv_text = this.state.columns.join(',') + '\n';
    let j = 0;
    let total_rows = this.state.rows.length;
    this.state.rows.forEach(function (row) {
      let i = 0;
      let columns = Object.keys(row);
      columns.forEach(function (c) {
        if (i === 0)
          csv_text += row[c];
        else
          csv_text += ',' + row[c];
        i++;
      });
      if (j < total_rows - 1)
        csv_text += '\n';
      j++;
    });
    var uri = encodeURIComponent(csv_text);
    var link = document.createElement("a");
    link.setAttribute("href", 'data:text/csv;charset=utf-8,' + uri);
    link.setAttribute("download", "template.csv");
    document.body.appendChild(link);
    link.click();
  }

  componentDidMount() {

    if (this.props.match.params.name === "datasource") {
      this.setState({
        excel_upload: false,
        columns: [
          "No.",
          "Link",
          "Table Name",
          "Description"
        ],
        rows: [
          {
            "No.": "1",
            "Link": "/table/course",
            "Table Name": "Class",
            "Description": "Table contains the class details"
          },
          {
            "No.": "1",
            "Link": "/table/group",
            "Table Name": "Group",
            "Description": "Table contains the Group details"
          },
          {
            "No.": "2",
            "Link": "/table/students",
            "Table Name": "Student",
            "Description": "Table contains the students in the class"
          }
        ]
      });
    } else if (this.props.match.params.name === "group") {
      this.GroupService = new GroupService();
      this.GroupService.getData().then((response) => {
        this.setState(response);
      });
    } else if (this.props.match.params.name === "course") {
      this.courseService = new CourseService();
      this.courseService.getData().then((response) => {
        this.setState(response);
      });
    } else if (this.props.match.params.name === "students") {
      this.setState({
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
      });
    }
  }

  convertToWord(text) {
    text = text.split("_");
    let final = [];
    text.forEach(
      function (item) {
        item = item.charAt(0).toUpperCase() + item.slice(1);
        final.push(item);
      }
    );
    return final.join(" ");
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
                <input type="file" className="file-upload" ref={fileInput => this.fileInput = fileInput} onChange={this.fileChanged} />
                {!this.state.loaded ? (
                  <Button variant="primary" type="button" disabled className="custom-btn">
                    Save
                  </Button>
                ) : (
                    <Button variant="primary" type="button" className="custom-btn">
                      Save
                    </Button>
                  )}
              </div>
            ) : (
                this.state.manual_add ? (
                  <div className="row table-div">
                    <Button variant="primary" type="button" className="custom-btn" href={'/form/' + this.props.match.params.name + '/new'}>
                      New
                    </Button>
                  </div>
                ) : (
                    <div></div>
                  )
              )
            }
            <div className="col-sm-12 table-div">
              <Table striped bordered hover size="sm">
                <thead>
                  <tr>
                    {this.state.columns.map(col => (
                      <th>
                        {this.convertToWord(col)}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {this.state.rows.map(row => (
                    <tr key={Math.random()}>
                      {this.state.columns.map(k => {
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
