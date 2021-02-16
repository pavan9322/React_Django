import React, {Component, render} from 'react';
import 'antd/dist/antd.css';

import CustomLayout from './containers/layout';
import {BrowserRouter as Router} from 'react-router-dom';

import BaseRouter from './routes';



class App extends Component {
  render () {
    return (
      <div className="App">
        <Router>
        <CustomLayout>
          <BaseRouter/>
        </CustomLayout>
        </Router>
        </div>
    )
  }
}

export default App;
