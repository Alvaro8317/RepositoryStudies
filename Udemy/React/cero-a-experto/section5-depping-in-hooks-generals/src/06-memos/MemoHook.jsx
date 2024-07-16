import { useMemo, useState } from 'react';
import { useCounter } from '../hooks/useCounter.js';
/*
 * useMemo memoriza un valor, el primer valor tiene que ser una función
 * El segundo valor son las dependencias, "Cambia solo si la dependencia cambia"
 */
const heavyStuff = (iterationsNumber = 100) => {
  for (let i = 0; i < iterationsNumber; i++) {
    console.log('Ahí vamos...');
  }
  return `${iterationsNumber} iterations with success state`;
};
export const MemoHook = () => {
  const { counter, increment } = useCounter(4000);
  const [show, setShow] = useState(true);
  const memorizeValue = useMemo(() => heavyStuff(counter), [counter]);
  return (
    <>
      <h1>
        Counter <small>{counter}</small>
      </h1>

      <hr />
      <h4>{memorizeValue}</h4>
      <button className='btn btn-primary' onClick={() => increment()}>
        +1
      </button>
      <button className='btn btn-primary' onClick={() => setShow(!show)}>
        Show / Hide {JSON.stringify(show)}
      </button>
    </>
  );
};
