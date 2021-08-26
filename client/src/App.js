import logo from './logo.svg';
import './App.css';
import Amplify, { API, graphqlOperation } from 'aws-amplify';
import { createRecord } from './graphql/mutations';

Amplify.configure({
  API: {
    aws_appsync_graphqlEndpoint: process.env.REACT_APP_ENDPOINT,
    aws_appsync_region: process.env.REACT_APP_REGION,
    aws_appsync_apiKey: process.env.REACT_APP_API_KEY,
    aws_appsync_authenticationType: "API_KEY"
  }
})

function App() {
  const test = API.graphqlOperation(create, {pk: 'test'})
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
