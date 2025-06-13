import logo from './logo.svg';
import './App.css';
import Component1 from './Component1';
import Clock from './Clock';
import Tabellina from './Tabellina';

function App() {
  let nome = 'pong';
  return (
    <div className="App">
      <Component1>King</Component1>
      <Component1>Proxy</Component1>
      <Component1>Svetoslav</Component1>
      <h1>Prima app di {nome}</h1>
      <h2><Clock timezone='0' country='Italia'></Clock></h2>
      <h3><Clock timezone='-6' country='USA'></Clock></h3>
      <h4><Clock timezone='7' country='Japan'></Clock></h4>
      <Tabellina numero='7'></Tabellina>
    </div>
  );
}

export default App;
