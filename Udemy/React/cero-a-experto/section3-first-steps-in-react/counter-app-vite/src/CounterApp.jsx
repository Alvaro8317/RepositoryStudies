import PropTypes from 'prop-types';
import { useState } from 'react';
/*
 * Con las funciones onClick se recibe como parámetro event, pero con ECMA6+ si una función recibe un parámetro en una arrow function se puede pasar directamente como se muestra en el ejemplo de button y handlerButtonAdd
 * Los claseBase Components son más lentos que los functional components
 * Los hooks en react son solamente funciones que empiezan con "use", cuando se creen nuevos hooks se recomienda que también siga esta nomenclatura
? Hooks
 * Al usar setCounter se especifica que el estado cambio, por ende, vuelva a renderizar el componente
 * En useState, el value es el valor inicial de counter y para cambiar el valor, se usa el segundo parámetro
 * No se debería de cambiar el valor del property para este caso value, con el jsx en el primer button salta al handlerButtonAdd. Cuando hace el renderizado del componente, vuelve a renderizar el componente
 * Cuando cambia el estado, el componente se vuelve a ejecutar, lo que si se mantiene es el valor de useState
 * ¿Por qué funciona así? React funciona para que los cambios sean unilaterales y mantener el counter actualizado
 */

const CounterApp = ({ value }) => {
  console.log('Renderizando CounterApp');
  const [counter, setCounter] = useState(value);
  const handlerButtonAdd = () => setCounter((c) => c + 1);
  const handlerButtonSubstract = () => setCounter(counter - 1);
  const handlerButtonReset = () => setCounter(value);
  return (
    <>
      <h1>CounterApp</h1>
      <h2>{counter}</h2>
      <button onClick={handlerButtonAdd}>+1</button>
      <button onClick={handlerButtonSubstract}>-1</button>
      <button aria-label='btn-reset' onClick={handlerButtonReset}>Reset</button>
    </>
  );
};

CounterApp.propTypes = {
  value: PropTypes.number.isRequired,
};

export default CounterApp;
