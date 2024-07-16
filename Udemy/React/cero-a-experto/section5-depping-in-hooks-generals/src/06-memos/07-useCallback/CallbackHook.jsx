import { useCallback, useState } from 'react';
import { ShowIncrement } from './ShowIncrement';
/*
 * UseCallback es similar a useMemo, pero es para funciones
 * useCallback memoriza el estado de una función incluyendo los valores de las variables que se usen dentro
 *
 */
export const CallbackHook = () => {
  const [counter, setCounter] = useState(10);

  const incrementFunction2 = useCallback((valueToIncrement) => {
    setCounter((actualCounter) => actualCounter + valueToIncrement);
  }, []);
  // const incrementFunction = () => {
  //   setCounter(counter + 1);
  // };
  return (
    <>
      <h1>useCallbackHook: {counter}</h1>
      <hr />
      <ShowIncrement increment={incrementFunction2} />
    </>
  );
};
