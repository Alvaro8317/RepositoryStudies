import { renderHook } from '@testing-library/react';
import { useFetchGifs } from '../../src/hooks/useFetchGifs';

describe('tests of useFetchGifs', () => {
  test('should return the initial state', () => {
    const { result } = renderHook(() => useFetchGifs('Assassins Creed'));
    const { images, isLoading } = result.current;
    expect(images.length).toBe(0);
    expect(isLoading).toBeTruthy();
  });
});
