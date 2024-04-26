// export const heroes = [ importación con const
// export default [ Exportación por default, la importación debería de ser así: import heroes  from './data/heroes';
const heroes = [
  {
    id: 1,
    name: 'Batman',
    owner: 'DC',
  },
  {
    id: 2,
    name: 'Spiderman',
    owner: 'Marvel',
  },
  {
    id: 3,
    name: 'Superman',
    owner: 'DC',
  },
  {
    id: 4,
    name: 'Flash',
    owner: 'DC',
  },
  {
    id: 5,
    name: 'Wolverine',
    owner: 'Marvel',
  },
];
// export const owners = ['UA', 'DC', 'Marvel'];
const owners = ['UA', 'DC', 'Marvel'];
// /* Tercera forma de exportar */
// export default heroes;
// /* import heroes  from './data/heroes'; */
/* Multiples exportaciones */
export {
  heroes as default, 
  owners
}