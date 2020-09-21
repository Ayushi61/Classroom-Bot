class GroupService {

    constructor() {
        this.api = 'http://' + process.env.REACT_APP_BACKEND_HOST + ':' + process.env.REACT_APP_BACKEND_PORT + '/api/group';

        this.data = {
            excel_upload: false,
            columns: [],
            rows: []
        };
    }

    getData() {
        return fetch(this.api+'?type=all')
            .then((response) => response.json())
            .then((responseData) => {

                console.log(responseData);
                let data = {};
                data.columns = [];
                data.columns.push("Link");
                data.columns = data.columns.concat(Object.keys(responseData.data[0].fields));
                delete data.columns[data.columns.indexOf('students')];
                data.rows = [];
                responseData.data.forEach(element => {
                    delete element.fields.students;
                    element.fields["Link"] = "/form/group/" + element.fields.registered_course+'/'+element.fields.group_number;
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

    getGroupData(course_id, group_number) {
        return fetch(this.api + '?type=group_number&course_id='+course_id+'&group_number='+group_number)
            .then((response) => response.json())
            .then((responseData) => {
                return responseData.data[0].fields;
            })
            .catch(error => console.warn(error));
    }

    saveOne(data) {
        return fetch(this.api, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
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

export default GroupService;
