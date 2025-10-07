import './App.css'
import { useState } from 'react';
import Navbar from './esercizi_agosto/NavBar';
import Saluto from './esercizi_agosto/Esercizio_01/Saluto';
import CardUtente from './esercizi_agosto/Esercizio_02/CardUtente';
import MenuRistorante from './esercizi_agosto/Esercizio_03/MenuRistorante';
import Termostato from './esercizi_agosto/Esercizio_04/Termostato';
import CampoRicerca from './esercizi_agosto/Esercizio_05/CampoRicerca';
import MessaggioSegreto from './esercizi_agosto/Esercizio_06/MessaggioSegreto';
import AggiornaTitolo from './esercizi_agosto/Esercizio_07/AggiornaTitolo';
import GalleriaFoto from './esercizi_agosto/Esercizio_08/GalleriaFoto'
import ModuloContatti from './esercizi_agosto/Esercizio_09/ModuloContatti';
import BlogApp from './esercizi_agosto/Esercizio_10/BlogApp';
import TodoApp from './esercizi_agosto/Esercizio_11/TodoApp';
import MainComponent from './esercizi_agosto/use-context/MainComponent';
import Slot from './Esercizi_personale/Slot';


function App() {
  const [esercizio, setEsercizio] = useState('')

  const renderCondzionale = () => {
    switch (esercizio) {
      case 'Saluto':
        return <Saluto />

      case 'CardUtente':
        return <CardUtente />

      case 'MenuRistorante':
        return <MenuRistorante />

      case 'Termostato':
        return <Termostato />

      case 'CampoRicerca':
        return <CampoRicerca />

      case 'MessaggioSegreto':
        return <MessaggioSegreto />

      case 'AggiornaTitolo':
        return <AggiornaTitolo />

      case 'GalleriaFoto':
        return <GalleriaFoto />

      case 'ModuloContatti':
        return <ModuloContatti />
        
      case 'BlogApp':
        return <BlogApp />
      
      case 'TodoApp':
        return <TodoApp />
      
      case 'MainComp':
        return <MainComponent />
    }

  };
  return (
    <>
      <Navbar onSetEsercizio={setEsercizio} />
      <div>{renderCondzionale()}</div>
      <Slot/>
    </>
  )
}

export default App;
