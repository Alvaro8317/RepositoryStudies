/* 
? DOCS: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Promise
* Primero se ejecuta el código síncrono y después así se ejecuta el asíncrono
* Resolve es cuando la promesa es exitosa
* Reject es cuando falla la promesa
*/
import { getHeroesById, getHeroesByOwner } from './bases/08-modules';
const promesa = new Promise((resolve, reject) => {
  setTimeout(() => {
    // console.log('2 segundos después y ahí si ejecuto el resolve para que se vaya al then');
    // resolve("Argumento")
    const hero = getHeroesById(2);
    console.log(hero);
    if (hero.id === 2) resolve(hero);
    reject('No se pudo encontrar al mejor heroe');
  }, 1000);
});
/* 
* then cuando la promesa fue exitosa,
! catch en caso de error
? finally se ejecuta haya sido exitosa o fallida la promesa
 */
/* Este podría decirse que es un listener que está escuchando si una promesa se resuelve */
promesa
  .then((hero) => {
    // console.log('Then de la promesa', parametro);
    console.log('El heroe obtenido de la API es: ', hero);
  })
  .catch((reasonReject) => {
    console.warn(`${reasonReject} :(`);
  });

/* A continuación se hace una función que retorna una promesa */
const promiseAsync = (id) =>
  new Promise((resolve, reject) => {
    setTimeout(() => {
      const hero = getHeroesById(id);
      if (hero === undefined) reject('No se pudo encontrar a este heroe');
      resolve(hero)
    }, 1000);
  });
/* Con las promesas se puede obviar el parámetro, a continuación hay un ejemplo */
promiseAsync(2)
  .then(console.log)
  .catch(console.warn)
  .finally(() => console.log("Y murió!"))
/* Aquí lo que realiza .then y .catch es que envía el parámetro que reciben directamente a console.log o .warn */