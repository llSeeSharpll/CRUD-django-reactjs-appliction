import './App.css';

import { Home } from './Home'
import { Department } from './Department'
import { Employee } from './Employee'
import { Navigation } from './Navigation'

import { BrowserRouter, Route, Switch } from 'react-router-dom'

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <div className="container">
          <h3 className="m-2 d-flex justify-content-center">
            React Js Tuturail
        </h3>
        <Navigation/>
        <Switch>
          <Route path='/' component={Home} exact/>
          <Route path='/department' component={Department} exact/>
          <Route path='/employee' component={Employee} exact/>
        </Switch>
        </div>
      </BrowserRouter>
    </div>
  );
}

export default App;
