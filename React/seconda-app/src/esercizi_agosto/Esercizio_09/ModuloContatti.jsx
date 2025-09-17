// Esercizio 9: Gestire Form Complessi con un Singolo Stato
// Obiettivo: Gestire un form con più campi usando un singolo oggetto per lo stato.
// Componente da creare: ModuloContatti.js
// Istruzioni:
// 1. Crea il componente ModuloContatti.js.
// 2. Usa useState per inizializzare uno stato come oggetto: { nome: '', email:
// '', messaggio: '' };.
// 3. Crea un form con tre input (nome, email) e una textarea (messaggio). Aggiungi
// a ognuno l'attributo name corrispondente.
// 4. Crea una sola funzione handleChange per tutti i campi. All'interno, usa lo spread
// operator per aggiornare solo il campo modificato.
// 5. Gestisci l'evento onSubmit del form per stampare l'oggetto datiForm in console.
// 6. Importa e usa <ModuloContatti /> in App.js.


import React, { useState } from 'react';

const ModuloContatti = () => {
  const [dati, setDati] = useState({ nome: '', email: '', messaggio: '' });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setDati((prevDati) => ({
      ...prevDati,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Dati del form:', dati);
  };

  // === STYLING INLINE ===
  const styles = {
    container: {
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      height: '100vh',
      backgroundColor: '#f9fafb',
      fontFamily: 'Arial, sans-serif',
    },
    form: {
      backgroundColor: '#ffffff',
      padding: '2rem',
      borderRadius: '12px',
      boxShadow: '0 8px 24px rgba(0, 0, 0, 0.05)',
      width: '100%',
      maxWidth: '400px',
      display: 'flex',
      flexDirection: 'column',
      gap: '1.2rem',
    },
    field: {
      display: 'flex',
      flexDirection: 'column',
      gap: '0.4rem',
    },
    label: {
      fontWeight: 'bold',
      fontSize: '0.95rem',
      color: '#374151',
    },
    input: {
      padding: '0.6rem 0.8rem',
      fontSize: '1rem',
      border: '1px solid #d1d5db',
      borderRadius: '8px',
      outline: 'none',
      transition: 'border-color 0.3s',
    },
    textarea: {
      padding: '0.6rem 0.8rem',
      fontSize: '1rem',
      border: '1px solid #d1d5db',
      borderRadius: '8px',
      resize: 'vertical',
      minHeight: '100px',
      outline: 'none',
    },
    button: {
      padding: '0.75rem',
      fontSize: '1rem',
      backgroundColor: '#4f46e5',
      color: '#ffffff',
      border: 'none',
      borderRadius: '8px',
      cursor: 'pointer',
      transition: 'background-color 0.3s',
    },
  };

  return (
    <div style={styles.container}>
      <form onSubmit={handleSubmit} style={styles.form}>
        <div style={styles.field}>
          <label style={styles.label}>Nome:</label>
          <input
            type="text"
            name="nome"
            value={dati.nome}
            onChange={handleChange}
            style={styles.input}
          />
        </div>

        <div style={styles.field}>
          <label style={styles.label}>Email:</label>
          <input
            type="email"
            name="email"
            value={dati.email}
            onChange={handleChange}
            style={styles.input}
          />
        </div>

        <div style={styles.field}>
          <label style={styles.label}>Messaggio:</label>
          <textarea
            name="messaggio"
            value={dati.messaggio}
            onChange={handleChange}
            style={styles.textarea}
          />
        </div>

        <button type="submit" style={styles.button}>Invia</button>
      </form>
    </div>
  );
};

export default ModuloContatti;