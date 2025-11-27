import React from 'react'
import UserInput from './User_input'


const handleCondition = (value) => {
    if (isNaN(value) || value <= 0 || value > 3) {
      return true
    } else {
      return false
    }
}

const GetNumberOfLines = ({onGetLines}) => {
  return (
    <UserInput 
        btn_visual='Conferma' 
        input_visual='Inserisci il numero di righe (1/3):' 
        error_visual='Numero di righe non valido. Riprova.'
        condition={handleCondition}
        onConfirm={onGetLines}
    />
  )
}

export default GetNumberOfLines