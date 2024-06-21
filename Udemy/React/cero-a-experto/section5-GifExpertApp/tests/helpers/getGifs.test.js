import { getGifs } from '../../src/helpers/getGifs';

describe('Tests of getGifs helper', () => {
  test('should return an array of gifs and must have the schema of id, title and url', async () => {
    const gifs = await getGifs('Metal gear solid');
    expect(gifs.length).toBeGreaterThan(0);
    expect(gifs[0]).toEqual({
      id: expect.any(String),
      title: expect.any(String),
      url: expect.any(String),
    });
  });
});
