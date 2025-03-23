import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import Campaigns from './components/Campaigns';
import Reports from './components/Reports';
import Heatmap from './components/Heatmap';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/login" component={Login} />
          <Route path="/dashboard" component={Dashboard} />
          <Route path="/campaigns" component={Campaigns} />
          <Route path="/reports" component={Reports} />
          <Route path="/heatmap" render={(props) => <Heatmap phishingPageId="PHISHING_PAGE_ID" />} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;