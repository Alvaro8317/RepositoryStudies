import { useState, useEffect } from 'react';
import { Message } from './Message';
/*
 * useEffect es para generar efectos secundarios
 * Cada vez que el componente se renderiza, se dispara el useEffect
 * Lo ideal es que un useEffect tenga una dependencia que es el segundo valor
 * El primer argumento es "lo que haré cuando me renderice", el segundo es "lista de dependencias"
 * Las dependencias son las condiciones que tendrá en cuenta para ver si se dispara el useEffect
 * Si se deja la lista de dependencias en [] significa que el useEffect solo se ejecutará cuando se renderice
 * Se recomienda que se creen efectos por cada efecto secundario en vez de uno solo que haga muchas cosas
 * Para este caso, el segundo efecto siempre se ejecutará cuando se renderice el componente
 */
export const SimpleForm = () => {
  const [formState, setFormState] = useState({
    username: 'alvaro831',
    email: 'eduardo831_@google.com',
  });
  const { username, email } = formState;
  const onInputChange = ({ target }) => {
    const { name, value } = target;
    // console.log(`Name: ${name}, Value: ${value}`);
    setFormState({ ...formState, [name]: value });
  };
  useEffect(() => {
    // console.log('UseEffect called by first time');
  }, []);
  useEffect(() => {
    // console.log('UseEffect called by formState');
  }, [formState]);
  useEffect(() => {
    // console.log('Email changed');
  }, [email]);
  // useEffect(
  //   () => {
  //     /* Callback */
  //     first;
  //     /* Cleanup */
  //     return () => {
  //       second;
  //     };
  //   } /* dependencias */,
  //   [third]
  // );

  return (
    <>
      <h1>Formulario simple</h1>
      <hr />
      <input
        type='text'
        className='form-control'
        placeholder='Username'
        name='username'
        value={username}
        onChange={onInputChange}
      />
      <input
        type='email'
        className='form-control mt-2'
        placeholder='eduardo831_@google.com'
        name='email'
        value={email}
        onChange={onInputChange}
      />
      {/* {<Message className='hidden' />} */}
      {username === 'alvaro8317' && <Message />}
    </>
  );
};
