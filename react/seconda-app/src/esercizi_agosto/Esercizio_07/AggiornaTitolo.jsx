// Esercizio 7: Effetti Collaterali con useEffect
// Obiettivo: Usare useEffect per eseguire un'azione (un "effetto collaterale") in risposta a
// un cambiamento di stato. Componente da creare: AggiornaTitolo.js
// Istruzioni:
// 1.​ Crea il componente AggiornaTitolo.js.
// 2.​ Crea un campo di input controllato (come nell'Esercizio 5) con una variabile di stato
// chiamata nome.
// 3.​ Importa l'hook useEffect da React.
// 4.​ Aggiungi un useEffect che si attivi ogni volta che il valore di nome cambia. Per
// farlo, dovrai usare l'array delle dipendenze: useEffect(() => { ... },
// [nome]);.
// 5.​ All'interno della funzione useEffect, aggiorna il titolo della scheda del browser. Se
// il campo nome è vuoto, il titolo sarà "Benvenuto!", altrimenti document.title =
// \Ciao, ${nome}!`;`.
// 6.​ Quando il componente viene montato, il titolo dovrebbe essere "Benvenuto!".
// Appena l'utente inizia a scrivere, il titolo della pagina si aggiornerà in tempo reale.
// 7.​ Importa e usa <AggiornaTitolo /> in App.js.


import React, { useState, useEffect } from 'react';

const AggiornaTitolo = () => {
  const [nome, setNome] = useState('');

  useEffect(() => {
    document.title = nome ? `Ciao, ${nome}!` : 'Benvenuto!';
  }, [nome]);

  const gestisciCambio = (e) => {
    setNome(e.target.value);
  };

  // Stili inline
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
      width: '260px',
      outline: 'none',
      transition: 'border-color 0.3s',
    },
    inputFocus: {
      borderColor: '#4f46e5',
    },
    label: {
      fontSize: '1.2rem',
      fontWeight: '500',
      color: '#111827',
    }
  };

  return (
    <div style={styles.container}>
      <label htmlFor="nome" style={styles.label}>Inserisci il tuo nome:</label>
      <input
        id="nome"
        type="text"
        value={nome}
        onChange={gestisciCambio}
        placeholder="Scrivi il tuo nome..."
        style={styles.input}
        onFocus={(e) => e.target.style.borderColor = styles.inputFocus.borderColor}
        onBlur={(e) => e.target.style.borderColor = styles.input.border}
      />
    </div>
  );
};

export default AggiornaTitolo;
