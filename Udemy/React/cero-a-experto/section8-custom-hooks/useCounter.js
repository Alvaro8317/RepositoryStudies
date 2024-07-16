import { useState } from 'react';

/* use se usa al principio como convención para los custom hooks */
export const useCounter = (initialValue = 10) => {
  const [counter, setCounter] = useState(initialValue);
  const increment = (value = 1) => setCounter(counter + value);
  const decrement = (value = 1) => {
    if (counter === 0) return;
    setCounter(counter - value);
  };
  const reset = () => setCounter(initialValue);
  return {
    counter,
    increment,
    decrement,
    reset,
  };
};
