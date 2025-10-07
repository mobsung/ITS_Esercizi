import React from 'react'
import UserInput from './User_input'


const GetBet = ({balance, lines, onGetBet}) => {

  const handleCondition = (value) => {
    if (isNaN(value) || value <= 0 || value > balance / lines) {
      return true
    } else {
      return false
    }
}

  return (
    <UserInput 
        btn_visual='Conferma' 
        input_visual='Inserisci la puntata per linea:' 
        error_visual='Puntata non valida. Riprova.'
        condition={handleCondition}
        onConfirm={onGetBet}
    />
  )
}

export default GetBet