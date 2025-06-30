import './App.css';
import ProfiloUtente from './Esercizi/Esercizi_argomenti_slide_2/ProfiloUtente.js';
import {utenti} from './Esercizi/Esercizi_argomenti_slide_2/utenti.js';
import AumentaDiminuisci from './Esercizi/Esercizio_slide_3/AumentaDIminuisci.js';
function App() {
  const gruppi = [];
  for (let i = 0; i < utenti.length; i += 3) {
    gruppi.push(utenti.slice(i, i + 3));
  }
  return (
    <div className="container mt-4">
      {gruppi.map((gruppo, idx) => (
        <div className="row mb-4" key={idx}>
          {gruppo.map((utente) => (
            <div className="col-md-4" key={utente.id}>
              <ProfiloUtente utente={utente} />
            </div>
          ))}
        </div>
      ))}
      <AumentaDiminuisci></AumentaDiminuisci>
    </div>
  );
}

export default App;
