import {
  getHeroeById,
  getHeroesByOwner,
} from '../../src/base-pruebas/08-imp-exp';

describe('Test of 08', () => {
  test('should return a hero by id', () => {
    const id = 1;
    const hero = getHeroeById(id);
    expect(hero).toEqual({ id: 1, name: 'Batman', owner: 'DC' });
  });
  test('should return undefined if not exists', () => {
    const id = 100;
    const hero = getHeroeById(id);
    /* Primera forma */
    expect(hero).toBe(undefined);
    /* Segunda forma, mejor práctica */
    expect(hero).toBeFalsy();
  });
});
describe('test of 08, homework', () => {
  test('should have a length of three', () => {
    const owner = 'DC';
    const heroes = getHeroesByOwner(owner);
    expect(heroes).toHaveLength(3);
    for (let i = 1; i < heroes.length; i++) {
      expect(heroes[i].owner).toEqual(owner);
    }
  });
  test('should have a length of two', () => {
    const owner = 'Marvel';
    const heroes = getHeroesByOwner(owner);
    expect(heroes).toHaveLength(2);
    for (let i = 1; i < heroes.length; i++) {
      expect(heroes[i].owner).toEqual(owner);
    }
  });
});
