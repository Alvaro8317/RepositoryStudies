import { getImagen } from '../../src/base-pruebas/11-async-await';

describe('Tests in 11', () => {
  test('should return the url of an image or the error', async () => {
    try {
      const url = await getImagen();
      expect(typeof url).toBe('string');
    } catch (error) {
      expect(error).toBeInstanceOf(Error);
    }
  });
});
