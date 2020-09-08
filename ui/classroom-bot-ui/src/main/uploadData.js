import React, { Component } from "react";
import Table from "react-bootstrap/Table";
import Button from 'react-bootstrap/button'

class UploadData extends Component {

  constructor (props) {
    super(props);
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
          <div className="row table-div">
            <div className="col-sm-2">
              <Button variant="primary" type="button" onClick={this.triggerInputFile}>
                  Upload
              </Button>
            </div>
            <input ref={fileInput => this.fileInput = fileInput} onChange={this.fileChanged} type="file" className="file-upload" />
            <div className="col-sm-2">
              <Button variant="primary" type="button">
                  Save
              </Button>
            </div>
          </div>
          <div className="row">
            <div className="col-sm-12 table-div">
              <Table striped bordered hover size="sm">
                <thead>
                  <tr>
                    <th>#</th>
                    <th>Group Name</th>
                    <th>Members</th>
                    <th>Active</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>1</td>
                    <td>
                      Group 1
                    </td>
                    <td>pchaudh5, atrivedi</td>
                    <td>True</td>
                  </tr>
                  <tr>
                    <td>2</td>
                    <td>
                      Group 2
                    </td>
                    <td>ayuhshi, rashi</td>
                    <td>True</td>
                  </tr>
                </tbody>
              </Table>
            </div>
          </div>
        </div>
      </div>
    );
  }

}

export default UploadData;
