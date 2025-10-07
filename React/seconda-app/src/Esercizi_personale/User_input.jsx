import React, { useState } from 'react';

const UserInput = ({ onConfirm, input_visual, btn_visual, error_visual, condition  }) => {
  const [inputValue, setInputValue] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    const numberInputValue = parseFloat(inputValue);

    if (condition(inputValue)) {
      setError(error_visual);
    } else {
      setError('');
      onConfirm(numberInputValue); // restituisce il valore valido
      setInputValue(''); // reset del campo input
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        {input_visual}
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
        />
      </label>
      <button type="submit">{btn_visual}</button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </form>
  );
};

export default UserInput;
