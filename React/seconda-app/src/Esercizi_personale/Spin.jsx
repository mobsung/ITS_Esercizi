import React from 'react'
import SYMBOLS_COUNT from symbols

const ROWS = 3;
const COLS = 3;

export const spin = () => {
  const symbols = [];

  // Build the full symbol pool
  for (const [symbol, count] of Object.entries(SYMBOLS_COUNT)) {
    for (let i = 0; i < count; i++) {
      symbols.push(symbol);
    }
  }

  const reels = [];

  // For each column (reel)
  for (let i = 0; i < COLS; i++) {
    reels.push([]);
    const reelSymbols = [...symbols];

    // For each row in the reel
    for (let j = 0; j < ROWS; j++) {
      const randomIndex = Math.floor(Math.random() * reelSymbols.length);
      const selectedSymbol = reelSymbols[randomIndex];

      reels[i].push(selectedSymbol);
      reelSymbols.splice(randomIndex, 1); // Remove selected to avoid duplicates
    }
  }

  return reels;
};


const Spin = () => {
  return (
    <div>Spin</div>
  )
}

export default Spin