import React from 'react';

const ProfiloUtente = ({ utente }) => {
  const mostraDettagli = () => {
    alert(`Dettagli utente:\n\n
      ID: ${utente.id}\n
      Nome: ${utente.nome} ${utente.cognome}\n
      Età: ${utente.eta}\n
      Professione: ${utente.professione}\n
      Email: ${utente.email}`);
  };
  

  return (
    <div className="card h-100">
      <div className="card-header text-center">
        <h5>{utente.nome} {utente.cognome}</h5>
      </div>
      <div className="card-body text-center">
        <p><span className="badge bg-primary">{utente.eta} anni</span></p>
        <p>{utente.professione}</p>
        <p>{utente.email}</p>
      </div>
      <div className="card-footer text-center">
        <button className="btn btn-outline-info btn-sm" onClick={mostraDettagli}>
          Mostra dettagli
        </button>
      </div>
    </div>
  );
};


export default ProfiloUtente;




//=================================================================================================================
//APP.JS

// import './App.css';
// import ProfiloUtente from './Esercizi/Esercizi_argomenti_slide_2/ProfiloUtente.js';
// import {utenti} from './Esercizi/Esercizi_argomenti_slide_2/utenti.js';

// function App() {
//   const gruppi = [];
//   for (let i = 0; i < utenti.length; i += 3) {
//     gruppi.push(utenti.slice(i, i + 3));
//   }
//   return (
//     <div className="container mt-4">
//       {gruppi.map((gruppo, idx) => (
//         <div className="row mb-4" key={idx}>
//           {gruppo.map((utente) => (
//             <div className="col-md-4" key={utente.id}>
//               <ProfiloUtente utente={utente} />
//             </div>
//           ))}
//         </div>
//       ))}
//     </div>
//   );
// }

// export default App;


//=================================================================================================================

//utenti.js



// export const utenti = [
//   {
//     id: 1,
//     nome: "Wario",
//     cognome: "Issor",
//     eta: 13,
//     professione: "Racer",
//     email: "wario.issor@fast.com"
//   },
//   {
//     id: 2,
//     nome: "Ispilon",
//     cognome: "Iren",
//     eta: 25,
//     professione: "Bird Watcher",
//     email: "Ispilon.Iren@fly.com"
//   },
//   {
//     id: 3,
//     nome: "Ailuig",
//     cognome: "Ihcnaib",
//     eta: 35,
//     professione: "I don't know",
//     email: "ailuig.ihcnaib@maybe.com"
//   },
// ];