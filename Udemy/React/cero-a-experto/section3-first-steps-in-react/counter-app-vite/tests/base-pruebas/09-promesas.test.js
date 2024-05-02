import { getHeroeByIdAsync } from '../../src/base-pruebas/09-promesas';
/*
 * Con asincronismo, se puede usar el async y el await o se puede usar el done(), esta es una función que le indica a jest "Ya acabé"
 */
describe('Tests of 09', () => {
  test('should return a hero async', (done) => {
    const id = 1;
    getHeroeByIdAsync(id).then((hero) => {
      expect(hero).toEqual({
        id: 1,
        name: 'Batman',
        owner: 'DC',
      });
      done();
    });
  });
  test('should return an error', (done) => {
    const id = 100;
    getHeroeByIdAsync(id).catch((err) => {
      expect(err).toBe('No se pudo encontrar el héroe');
      done();
    });
  });
});
