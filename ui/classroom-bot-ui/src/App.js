import React, { Component } from 'react';
import TopBar from './common/topBar'
import Body from './common/body'
import './css/main.css'

class App extends Component {
  
  constructor(props) {
      super(props);
      this.state = {
          logged_in: true,
          user: null
      }
  }

  render () {
    return (
        <div>
          <TopBar app={this.state} />
          <Body app={this.state} />
        </div>
    );
  };
}

export default App;
