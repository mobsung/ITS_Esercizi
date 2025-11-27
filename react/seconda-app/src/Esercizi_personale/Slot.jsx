import React, { useState } from 'react';
import Deposit from './Deposit';
import GetNumberOfLines from './GetNumberOfLines';
import GetBet from './GetBet';


const ROWS = 3;
const COLS = 3;

const Slot = () => {

    const [balance, setBalance] = useState(0);
    const [lines, setLines] = useState(0);
    const [bet, setBet] = useState(0);
    
    const handleBalance = (amount) => {
        setBalance(amount);
    };

    const handleGetLines = (amount) => {
        setLines(amount)
    };

    const handleGetBet = (amount) => {
        setBet(amount)
    };
    
  return (
    <>
    <Deposit onDeposit={handleBalance}/>
    <GetNumberOfLines onGetLines={handleGetLines}/>
    <GetBet onGetBet={handleGetBet} balance={balance} lines={lines}/>
    </>
  )
}

export default Slot