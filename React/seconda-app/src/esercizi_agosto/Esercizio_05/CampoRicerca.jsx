// Esercizio 5: Gestire Input Utente (Controlled Components)
// Obiettivo: Creare un campo di input il cui valore è controllato dallo stato di React.
// Componente da creare: CampoRicerca.js
// Istruzioni:
// 1.​ Crea il componente CampoRicerca.js.
// 2.​ Usa useState per creare uno stato testoRicerca, inizializzato a ''.
// 3.​ Crea un <input type="text" /> e collega il suo value allo stato
// {testoRicerca}.4.​ Gestisci l'evento onChange per aggiornare lo stato con il valore dell'input
// (e.target.value).
// 5.​ Sotto l'input, aggiungi un paragrafo che mostra in tempo reale cosa sta scrivendo
// l'utente: <p>Stai cercando: {testoRicerca}</p>.
// 6.​ Importa e usa <CampoRicerca /> in App.js.


import React, { useState } from 'react';

const CampoRicerca = () => {
  const [testoRicerca, setTestoRicerca] = useState('');

  const gestisciCambio = (e) => {
    setTestoRicerca(e.target.value);
  };

  // Oggetti di stile
  const styles = {
    container: {
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      height: '100vh',
      flexDirection: 'column',
      gap: '16px',
      backgroundColor: '#f9fafb',
      fontFamily: 'Arial, sans-serif',
    },
    input: {
      padding: '0.75rem 1rem',
      fontSize: '1rem',
      borderRadius: '8px',
      border: '1px solid #d1d5db',
      width: '250px',
      outline: 'none',
      transition: 'border-color 0.3s',
    },
    inputFocus: {
      borderColor: '#4f46e5',
    },
    text: {
      fontSize: '1.1rem',
      color: '#374151',
    },
  };

  return (
    <div style={styles.container}>
      <input
        type="text"
        value={testoRicerca}
        onChange={gestisciCambio}
        placeholder="Scrivi testo"
        style={styles.input}
        onFocus={(e) => e.target.style.borderColor = styles.inputFocus.borderColor}
        onBlur={(e) => e.target.style.borderColor = styles.input.border}
      />
      <p style={styles.text}>Stai cercando: {testoRicerca}</p>
    </div>
  );
};

export default CampoRicerca;
