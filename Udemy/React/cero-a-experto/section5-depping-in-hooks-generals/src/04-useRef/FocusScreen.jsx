import { useRef } from 'react';
/*
 * La idea de useRef es que permite mantener una referencia y que cuando la referencia cambia, no se renderice el componente nuevamente. En useRef se puede dejar cualquier tipo de dato.
* Si hay múltiples componentes, react no se confundirá porque usa el useRef para tener el espacio en memoria del componente
 */
export const FocusScreen = () => {
  // const onClickBtn = () => {
  //   /* Si tengo varios input, este event no me asegura que vaya a seleccionar el que realmente deseo */
  //   document.querySelector('input').select();
  // };
  const inputRef = useRef();
  console.log(inputRef);
  const onClickBtn = () => {
    /* Si tengo varios input, este event no me asegura que vaya a seleccionar el que realmente deseo */
    // document.querySelector('input').select();
    console.log(inputRef);
    inputRef.current.select()
  };
  return (
    <>
      <h1>Focus Screen</h1>
      <hr />
      <input
        ref={inputRef}
        type='text'
        placeholder='Ingrese su nombre'
        className='form-control'
      />
      <button className='btn btn-primary mt-2' onClick={onClickBtn}>
        Set focus
      </button>
    </>
  );
};
