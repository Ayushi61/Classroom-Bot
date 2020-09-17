import React, { Component } from "react";
//import TopBar from './common/topBar'
//import Body from './common/body'
import "./css/main.css";

class API extends Component {
  constructor(props) {
    super(props);
    this.state = {
      //logged_in: true,
      //user: null
      data: [],
      isLoaded: false,
    };
  }

  componentDidMount() {
    fetch(
      "http://ec2-3-16-10-131.us-east-2.compute.amazonaws.com:8000/api/course?workspace_id=ABC123"
    )
      .then((res) => res.json())
      .then((json) => {
        console.log(json.data);
        this.setState({
          isLoaded: true,
          items: json.data,
        });
      });
  }

  render() {
    var { isLoaded, items } = this.state;

    if (!isLoaded) {
      return <div>Loading..</div>;
    } else {
      return (
        //<div className="App">Data is loaded</div>
        <div>
          <ul>
            {items &&
              items.map((item) => (
                <li key={item.model}>
                  workspace_id:{item.fields.workspace_id}
                </li>
              ))}
            ;
          </ul>
        </div>
      );
    }
  }
  //    return (
  //        <div className="App">
  //          <TopBar app={this.state} />
  //          <Body app={this.state} />
  //        </div>
  //    );
  //  };
  //};
}

export default API;
