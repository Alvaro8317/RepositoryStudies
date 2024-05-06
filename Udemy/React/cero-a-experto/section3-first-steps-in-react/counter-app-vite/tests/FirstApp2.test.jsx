const { render, screen } = require('@testing-library/react');
import FirstApp from '../src/FirstApp';
/*
 * Se crea este archivo para emplear mejores prácticas
 * Screen es el objeto que se está renderizando
 */
describe('Test of First App Component', () => {
  const title = 'Hola, soy un título';
  const subtitle = 'Hola, soy un subtítulo';
  test('Should match the snapshot', () => {
    const { container } = render(<FirstApp title={title} />);
    expect(container).toMatchSnapshot();
  });
  test('should show the title "Hola, soy un título"', () => {
    render(<FirstApp title={title} />);
    // screen.debug();
    expect(screen.getByText(title)).toBeTruthy();
  });
  test('should show the title in h1', () => {
    render(<FirstApp title={title} />);
    expect(screen.getByRole('heading', { level: 1 }).innerHTML).toContain(
      title
    );
  });
  test('should show the subtitle by props', () => {
    render(<FirstApp title={title} subtitle={subtitle} />);
    expect(screen.getAllByText(subtitle).length).toBe(1);
  });
});
