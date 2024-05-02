const { render } = require('@testing-library/react');
import FirstApp from '../src/FirstApp';
/*
 *El render hace muchas cosas, pero una es que renderiza el componente en memoria
 * El render también actualiza el screen que es un componente, también expone otras propiedades como el container, que es similar al DOM
 * Un snapshot, es una fotografia de lo actual (si no se ha tomado la fotografia) y cada vez que se ejecuta toMatchSnapshot, valida si existe una snapshot, en caso que no, la crea con lo renderizado, en caso que sí, la compara y valida que no tenga diferencias, si hay diferencias, falla la prueba
 * La prueba del snapshot es útil para confirmar que la aplicación quedará en un estado especifico
 * El container es un nodo del DOM
 * Contain es menos estricto
 * toBe se encarga de validar que coincida todo, incluyendo espacios vacíos
 * toContain es más flexible y valida que una cadena existe
 * Los métodos getBy(...) retornan y validan un solo tipo, para más, usar getAll
 */
describe('Test of First App Component', () => {
  // test('Should match the snapshot', () => {
  //   const title = 'Hola';
  //   const { container } = render(<FirstApp title={title} />);
  //   expect(container).toMatchSnapshot();
  // });
  test('should show the title in a h1', () => {
    const title = 'Alvaro Garzón';
    const { container, getByText, getByTestId } = render(
      <FirstApp title={title} />
    );
    expect(getByText(title)).toBeTruthy();
    expect(getByTestId('test-title')).toBeTruthy();
    expect(getByTestId('test-title').innerHTML).toBe(title);
    expect(getByTestId('test-title').innerHTML).toContain(title);
    // const h1 = container.querySelector('h2');
    // expect(h1.innerHTML).toBe(title);
    // expect(h1.innerHTML).toContain(title);
  });
  test('should show the subtitle by props', () => {
    const title = 'Alvaro Garzón';
    const subtitle = 'I am a subtitle';
    const { container, getByText, getAllByText } = render(
      <FirstApp title={title} subtitle={subtitle} />
    );
    expect(getByText(subtitle)).toBeTruthy();
    expect(getAllByText(subtitle).length).toBe(1)
  });
});
