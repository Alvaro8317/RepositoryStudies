/* Un arreglo es una colección de información que se encuentra dentro de la misma variable */
// const arreglo = new Array() /* Esto crea un array con el constructor, pero se recomienda de la siguiente forma */
// const arregloConSlots = new Array(100) /* La unica excepción para crear un array con constructor */
// console.log(arregloConSlots)
const arreglo = [];
/* Modificación de un array */
arreglo.push(1);
arreglo.push(2);
arreglo.push(3);
arreglo.push(4);
/* 
! No es recomendable usar el push para modificar un array porque modifica el array principal
* Cuando se quiera insertar, mejor usar el operador spread
*/
console.log(arreglo);
const arreglo2 = [1, 2, 3, 4];
const arreglo3 = arreglo2;
arreglo3.push(5);
console.log(arreglo2);
/*
 * Al agregar con push se modifica el array original, mejor usar el spread operator
 */
const arreglo4 = [...arreglo2, 6, 7];
/* Aquí el spread genera copias y extrae los datos */
console.log(arreglo4);
console.log(arreglo2);
/* Un callback es una función que se ejecuta dentro de otra función, para este caso, map ejecuta la función que yo le definí */
/* 
* Si una arrow function es inline, no es necesario dejar el return
* Si no se deja especifico un return, se retorna undefined
* Documentación de MAP: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array/map
*/
const arregloConMap = arreglo2.map((number) => number * 2);
console.log(arregloConMap)
