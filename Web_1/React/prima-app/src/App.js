import logo from './logo.svg';
import './App.css';
import Component1 from './Component1';
import Clock from './Clock';
import persone from './Esercizi/Esercizio_01';
import Tabellina from './Esercizi/Esercizio_02';
import Stampanumeri from './Esercizi/Esercizio_03';
import StampanumeriPari from './Esercizi/Esercizio_04';

function App() {
  let nome = 'pong';
  return (
    <div className="App">
      {/* <Component1>King</Component1>
      <Component1>Proxy</Component1>
      <Component1>Svetoslav</Component1>
      <h1>Prima app di {nome}</h1>
      <h2><Clock timezone='0' country='Italia'></Clock></h2>
      <h3><Clock timezone='-6' country='USA'></Clock></h3>
      <h4><Clock timezone='7' country='Japan'></Clock></h4>
      <Tabellina numero='7'></Tabellina> */}
      {/* <h1>TEST ESERCIZIO 1</h1>
      {
        persone.map((persona) => {

          return <h1 key={persona.id}>{persona.nome} {persona.cognome}</h1>;

        })
      }
      <br></br>

      <h1>TEST ESERCIZIO 2</h1>
      <h1><Tabellina moltiplicatore='7'></Tabellina></h1><br></br>

      <h1>TEST ESERCIZIO 3</h1>
      <h1><Stampanumeri></Stampanumeri></h1><br></br>

      <h1>TEST ESERCIZIO 4</h1>
      <h1><StampanumeriPari></StampanumeriPari></h1> */}

      
    </div>
  );
}

export default App;
