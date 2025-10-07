import React from 'react'
import UserInput from './User_input'

const handleCondition = (value) => {
    if (isNaN(value) || value <= 0) {
      return true
    } else {
      return false
    }
}

const Deposit = ({onDeposit}) => {
  return (
    <UserInput 
        btn_visual='Deposita' 
        input_visual='Inserisci un importo da depositare:' 
        error_visual='Importo non valido. Riprova.'
        condition={handleCondition}
        onConfirm={onDeposit}
    />
  )
}

export default Deposit