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
    return fetch('http://localhost:8000/api/course')
      .then((response) => response.json())
      .then((responseData) => {
        let data = {};
        data.columns = [];
        data.columns.push("Link");
        data.columns = data.columns.concat(Object.keys(responseData.data[0].fields));
        data.rows = [];
        responseData.data.forEach(element => {
          element.fields["Link"] = "/form/course";
          data.rows.push(element.fields);
        });
        data.excel_upload = false;
        data.loaded = false;
        return data;
      })
      .catch(error => console.warn(error));
  }

}

export default CourseService;
