// Esercizio 6: Rendering Condizionale
// Obiettivo: Mostrare o nascondere elementi della UI in base a una condizione. Componente
// da creare: MessaggioSegreto.js
// Istruzioni:
// 1.​ Crea il componente MessaggioSegreto.js.
// 2.​ Usa useState per creare uno stato booleano mostra, inizializzato a false.
// 3.​ Crea un bottone che al onClick inverte il valore di mostra.
// 4.​ Usa l'operatore ternario per cambiare il testo del bottone.
// 5.​ Usa l'operatore && per mostrare un paragrafo con un "messaggio segreto" solo se
// mostra è true.
// 6.​ Importa e usa <MessaggioSegreto /> in App.js.


import React, { useState } from 'react';

const MessaggioSegreto = () => {
  const [mostra, setMostra] = useState(false);
  const segreto = 'Questo è un messaggio segreto';

  // Styling inline in oggetti
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
    button: {
      backgroundColor: '#4f46e5',
      color: '#fff',
      border: 'none',
      padding: '0.75rem 1.5rem',
      fontSize: '1rem',
      borderRadius: '8px',
      cursor: 'pointer',
      transition: 'background-color 0.3s',
    },
    buttonHover: {
      backgroundColor: '#4338ca',
    },
    message: {
      fontSize: '1.2rem',
      color: '#111827',
      padding: '0.5rem 1rem',
      backgroundColor: '#e0e7ff',
      borderRadius: '6px',
    },
  };

  return (
    <div style={styles.container}>
      <button
        onClick={() => setMostra(!mostra)}
        style={styles.button}
        onMouseOver={(e) => e.currentTarget.style.backgroundColor = styles.buttonHover.backgroundColor}
        onMouseOut={(e) => e.currentTarget.style.backgroundColor = styles.button.backgroundColor}
      >
        {mostra ? 'Nascondi' : 'Mostra'}
      </button>

      {mostra && <p style={styles.message}>{segreto}</p>}
    </div>
  );
};

export default MessaggioSegreto;