class CourseService {

  constructor() {
    this.data = {
      excel_upload: false,
      loaded: false,
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
          "Link": "/form/class",
          "Class Name": "CSC SE Fall 2020",
          "Team ID": "T001",
          "Semester": "Fall 2020"
        },
        {
          "No.": "2",
          "Link": "/form/class",
          "Class Name": "CSC SE Fall 2019",
          "Team ID": "T002",
          "Semester": "Fall 2019"
        }
      ]
    };
  }

  getData() {
    return fetch('http://' + process.env.REACT_APP_BACKEND_HOST + ':' + process.env.REACT_APP_BACKEND_PORT + '/api/course')
      .then((response) => response.json())
      .then((responseData) => {
        let data = {};
        data.columns = [];
        data.columns.push("Link");
        data.columns = data.columns.concat(Object.keys(responseData.data[0].fields));
        delete data.columns[data.columns.indexOf('bot_token')];
        delete data.columns[data.columns.indexOf('admin_user_id')];
        data.rows = [];
        responseData.data.forEach(element => {
          delete element.fields.bot_token;
          delete element.fields.admin_user_id;
          element.fields["Link"] = "/form/course/"+element.fields.workspace_id;
          data.rows.push(element.fields);
        });
        data.excel_upload = false;
        data.loaded = false;
        data.manual_add = true;
        return data;
      })
      .catch(error => console.warn(error));
  }

  getCourseData(workspace_id) {
    return fetch('http://' + process.env.REACT_APP_BACKEND_HOST + ':' + process.env.REACT_APP_BACKEND_PORT + '/api/course?workspace_id='+workspace_id)
    .then((response) => response.json())
      .then((responseData) => {
        return responseData.data[0].fields;
      })
      .catch(error => console.warn(error));
  }

  isValid() {

  }

  saveOne() {

  }

}

export default CourseService;
