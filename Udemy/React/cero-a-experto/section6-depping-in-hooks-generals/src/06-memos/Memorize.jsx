import { useState } from 'react';
import { useCounter } from '../hooks/useCounter.js';
import { Small } from './Small.jsx';
/* 
* Sin usar memorize, si un componente hijo no tiene cambios pero el componente padre sí, vuelve a renderizar su hijo
* Memorizar es recomendable cuando un componente es muy grande o tienen un proceso muy pesado que se realizaría solo cuando cambian los properties
*/
export const Memorize = () => {
  const { counter, increment } = useCounter(1);
  const [show, setShow] = useState(true);
  return (
    <>
      <h1>
        Counter <Small value={counter} />
      </h1>

      <hr />
      <button className='btn btn-primary' onClick={() => increment()}>
        +1
      </button>
      <button className='btn btn-primary' onClick={() => setShow(!show)}>
        Show / Hide {JSON.stringify(show)}
      </button>
    </>
  );
};
