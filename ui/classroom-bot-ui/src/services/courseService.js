class CourseService {

  constructor() {
    this.api = 'http://' + process.env.REACT_APP_BACKEND_HOST + ':' + process.env.REACT_APP_BACKEND_PORT + '/api/course';

    this.data = {
      excel_upload: false,
      loaded: false,
      columns: [],
      rows: []
    };
  }

  getData() {
    return fetch(this.api)
      .then((response) => response.json())
      .then((responseData) => {
        let data = {};
        data.columns = [];
        data.columns.push("Link");
        data.columns = data.columns.concat(Object.keys(responseData.data[0].fields));
        data.rows = [];
        responseData.data.forEach(element => {
          element.fields["Link"] = "/form/course/" + element.fields.workspace_id;
          element.fields["id"] = element.pk;
          data.rows.push(element.fields);
        });
        data.excel_upload = false;
        data.loaded = false;
        data.manual_add = true;
        return data;
      })
      .catch(error => {
        console.warn(error);
        let data = {};
        data.columns = [];
        data.rows = [];
        data.excel_upload = false;
        data.loaded = false;
        data.manual_add = true;
        return data;
      });
  }

  getCourseData(workspace_id) {
    return fetch(this.api + '?workspace_id=' + workspace_id)
      .then((response) => response.json())
      .then((responseData) => {
        return responseData.data[0].fields;
      })
      .catch(error => console.warn(error));
  }

  saveOne(data) {
    let formData = new FormData();
    for (var key in data) {
      formData.append(key, data[key]);
    }
    return fetch(this.api, {
      method: 'POST',
      body: formData
    }).then(response => {
      let data = response.json();
      data['status'] = 'success';
      return data;
    }).catch(error => {
      let data = {};
      data['error'] = error;
      data['status'] = 'error';
      return data;
    });
  }

}

export default CourseService;
