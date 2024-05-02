/*
 * Toda app de react empieza con un componente o functional component, como un   punto de entrada
 * Las clases no son recomendadas en react, mejor con componentes basados en funciones o functional components
 * Todos los nombres de los componentes van con PascalCase
 * El funcional component no va usualmente en main.jsx
 * Equivalente a document.createElement
 * No es recomendable porque title debe de venir pero se añade una lógica al componente innecesaria, aquí entra los propTypes
 * Escribir el functional component.propTypes sirve para indicar que tipo de dato se requiere y si es obligatorio o no, si se envía un datatype incorrecto renderiza pero deja el error en consola. Con isRequired se indica si es obligatorio o no un campo
 * rafc genera un nuevo componente con las extensiones de vscode
 * Se pueden crear los valores por defecto en defaultProps o en los parámetros del functional component, pero mejor práctica en defaultProps porque con 5 parámetros por defecto se volvería difícil de leer el código
 */
import PropTypes from 'prop-types';
const App = ({ title = 'No hay título', subtitle = 'No hay subtitulo' }) => {
  // if (!title) {
  //   throw new Error('El title no existe');
  // }
  return (
    <>
      <div>Hola React</div>
      <h1 data-testid='test-title'>{title}</h1>
      <h2>{subtitle}</h2>
    </>
  );
};
/* Tipos de dato y si son requeridos o no */
App.propTypes = {
  title: PropTypes.string.isRequired,
  subtitle: PropTypes.string.isRequired,
};
/* Props por defecto */
// App.defaultProps = {
//   subtitle: 'No hay subtitulo',
// };
export default App;
