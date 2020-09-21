class StudentService {

    constructor() {
        this.api = 'http://' + process.env.REACT_APP_BACKEND_HOST + ':' + process.env.REACT_APP_BACKEND_PORT + '/api/student';

        this.data = {
            excel_upload: true,
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
                data.columns = data.columns.concat(Object.keys(responseData.data[0].fields));
                data.rows = [];
                responseData.data.forEach(element => {
                    data.rows.push(element.fields);
                });
                data.excel_upload = true;
                data.loaded = false;
                data.manual_add = false;
                return data;
            })
            .catch(error => {
                console.warn(error);
                let data = {};
                data.columns = [];
                data.rows = [];
                data.excel_upload = true;
                data.loaded = false;
                data.manual_add = false;
                return data;
            });
    }

    saveAll(data) {
        let rows = data.rows;
        let success = [];
        rows.forEach(element => {
            let formData = new FormData();
            for (var key in element) {
                let key2 = key;
                if (key.trim() === 'registered_course')
                    key2 = 'course_id';
                formData.append(key2, element[key]);
            }
            fetch(this.api, {
                method: 'POST',
                body: formData
            }).then(response => {
                console.log(response);
                success.push(response);
            }).catch(error => {
                success.push(error);
            });
        });
        return success;
    }

}

export default StudentService;