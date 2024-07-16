import { render, screen } from '@testing-library/react';
import { GifItem } from '../../src/components/GifItem';

describe('Tests of GifItem Component', () => {
  const title = 'metal gear art GIF';
  const url = 'https://giphy.com/gifs/oktotally-art-pixel-jQQ854R8tx3wI';
  test('should match the snapshot', () => {
    const { container } = render(<GifItem title={title} url={url} />);
    expect(container).toMatchSnapshot();
  });
  test('should show the image with the url and the title', () => {
    render(<GifItem title={title} url={url} />);
    // screen.debug();
    expect(screen.getByRole('img').src).toBe(url);
    expect(screen.getByRole('img').alt).toBe(title);
  });
  test('should show the title in the component', () => {
    render(<GifItem title={title} url={url} />);
    expect(screen.getByText(title)).toBeTruthy();
  });
});
