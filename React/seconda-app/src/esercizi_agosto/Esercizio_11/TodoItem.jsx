// 4. TodoItem.js (Nipote):
// ○ Riceve il singolo oggetto task e le funzioni handleDeleteTask e
// handleToggleTask come props.
// ○ Visualizza il testo del task. Applica uno stile per sbarrare il testo se
// task.completed è true.
// ○ Aggiungi un checkbox che, al onChange, chiami handleToggleTask con
// l'id e lo stato completed invertito.
// ○ Aggiungi un bottone "Elimina" che, al onClick, chiami handleDeleteTask
// con l'id del task.


import React from 'react'

const TodoItem = ({task}) => {
  return (
    <div>{task.text}</div>
  )
}

export default TodoItem