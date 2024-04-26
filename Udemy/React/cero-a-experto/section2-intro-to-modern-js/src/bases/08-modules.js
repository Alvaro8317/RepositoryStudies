/* Hay varias formas de importar */
/* No se importa con llaves solo cuando es importación por defecto */
import heroes, { owners } from '../data/heroes';
// import {heroes, owners}  from './data/heroes';
// console.log(owners);
const getHeroesById = (id) => heroes.find((hero) => hero.id === id);
// console.log(getHeroesById(5));

const getHeroesByOwner = (owner) =>
  heroes.filter((hero) => hero.owner === owner);
// console.log(getHeroesByOwner('DC'));
export {
  getHeroesById,
  getHeroesByOwner
}