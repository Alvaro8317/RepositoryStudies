/* Primera alternativa a dejar elementos en la etiqueta root -> Con fragment */
/* Para tener dos elementos en la etiqueta root, se debe de usar una funcionalidad de react */
// import { Fragment } from 'react';

// export const ComponentWithMyName = () => {
//   return (
//     <Fragment>
//       <h2>Alvaro Garzón</h2>
//       <p>This is a p tag</p>
//     </Fragment>
//   );
// };

/* Segunda alternativa, un nodo padre vacío */
/* Esto es un sinonimo a un fragmento, funciona igual pero no necesita importaciones, es un agrupador de jsx. */
/* Aquí permite dejar expresiones JS que no sean un objeto */

/* Si una constante no tiene nada que ver con el componente como que cambie su valor, sino que es inmutable, se recomienda dejar por fuera de cualquier functional component como newMessage */
/* De esta forma, react no reprocesará lo que esté por fuera de los componentes */
/* Con arrays que se renderizan, los renderiza por aparte, ejemplo: [1,2,3,4,5] -> "1" "2" "3" (...) */
const newMessage = { message: 'hola', state: true };
/* Los objetos no son validos como React child, por eso mejor renderizarlos como un objeto. Si realmente se requiere imprimir, se debe de usar JSON.stringify */

/* Si se invoca una función desde el jsx no debería de ser async porque retorna un promise y no se pueden renderizar objetos */
const getMessage = () => ({ message: 'Lalilulelo', state: true });
/* Con react permite usar SSAS, CSS, Tailwind, el que requiera */

/*
 * En react existen los props o properties, mejor conocidas como los props, son las propiedades de la función, usualmente se desestructuran.
 * Es la información que fluye del componente padre al componente hijo
 * El contexto de una aplicación en react es donde están todos los componentes, para este caso son App, ComponentWithMyName, etc.
 */
// export const ComponentWithMyName = (props) => { Sin desestructuración
export const ComponentWithMyName = ({ title }) => {
  console.log(title);
  return (
    <>
      <h1>{JSON.stringify(newMessage)}</h1>
      <h2>{JSON.stringify(getMessage())}</h2>
      <h3>{title}</h3>
      <p>Subtitulo</p>
    </>
  );
};
