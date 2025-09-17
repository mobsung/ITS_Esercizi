// Esercizio 3: Renderizzare Liste con .map()
// Obiettivo: Visualizzare dinamicamente una lista di elementi partendo da un array.
// Componente da creare: MenuRistorante.js
// Istruzioni:
// 1.​ Crea un file piatti.js in src ed esporta un array di oggetti. Ogni oggetto deve
// avere id, nome e prezzo.
// 2.​ Crea il componente MenuRistorante.js e importa l'array di piatti.
// 3.​ Usa il metodo .map() sull'array per renderizzare una lista <ul> di piatti.
// 4.​ Ogni <li> deve contenere il nome e il prezzo del piatto e deve avere un attributo
// key univoco (usa piatto.id).
// 5.​ Importa e usa <MenuRistorante /> in App.js.


import React from 'react';
import piatti from './piatti';

const styles = {
  container: {
    maxWidth: '600px',
    margin: '2rem auto',
    padding: '1.5rem',
    backgroundColor: '#ffffff',
    border: '1px solid #e5e7eb',
    borderRadius: '12px',
    boxShadow: '0 8px 24px rgba(0, 0, 0, 0.05)',
    listStyleType: 'none',
  },
  item: {
    padding: '1rem',
    marginBottom: '1rem',
    borderBottom: '1px solid #f0f0f0',
    backgroundColor: '#f9fafb',
    borderRadius: '8px',
    lineHeight: 1.6,
    fontSize: '1rem',
    transition: 'background-color 0.2s ease',
  },
  bold: {
    color: '#4f46e5',
    fontWeight: 600,
  },
};

const MenuRistorante = () => {
  return (
    <ul style={styles.container}>
      {piatti.map((piatto) => (
        <li key={piatto.id} style={styles.item}>
          <b style={styles.bold}>Nome: </b>{piatto.nome}<br />
          <b style={styles.bold}>Prezzo: </b>€ {piatto.prezzo.toFixed(2)}
        </li>
      ))}
    </ul>
  );
};

export default MenuRistorante;
