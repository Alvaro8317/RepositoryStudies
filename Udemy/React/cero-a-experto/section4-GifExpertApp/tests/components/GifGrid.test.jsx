import { render, screen } from '@testing-library/react';
import { GifGrid } from '../../src/components/GifGrid';
/* Se importa la función a hacerle el mock */
import { useFetchGifs } from '../../src/hooks/useFetchGifs';
import { gifs } from './mocks/gifs';
jest.mock('../../src/hooks/useFetchGifs');
describe('Tests of gifgrid', () => {
  const category = 'Metal gear';

  test('should show the loading at the start', () => {
    useFetchGifs.mockReturnValue({ images: [], isLoading: true });
    render(<GifGrid category={category} />);
    expect(screen.getByText('Cargando...'));
    expect(screen.getByText(category));
  });

  test('should show items when loads the fetch', () => {
    useFetchGifs.mockReturnValue({ images: gifs, isLoading: false });
    render(<GifGrid category={category} />);
    expect(screen.getAllByRole('img').length).toBe(2);
  });
});
