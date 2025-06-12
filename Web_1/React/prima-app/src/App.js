import logo from './logo.svg';
import './App.css';
import Component1 from './Component1';

function App() {
  let nome = 'pong';
  return (
    <div className="App">
      <Component1></Component1>
        <h1>Prima app di {nome}</h1>
        <h2>
          {
            new Date().toLocaleDateString()+" "+ new Date().toLocaleTimeString()
          }
        </h2>
    </div>
  );
}

export default App;
