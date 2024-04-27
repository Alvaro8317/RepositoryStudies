/* Funciones en JS, se recomienda mejor crear funciones con constant functions
porque de la siguiente manera, se puede tener primero el warning como se muestra
a continuación que dice
! 'saludar' is a function
* no obstante, permite reemplazar una función por una variable como se ve a continuación en el código
*/
function saludar(nombre) {
  return `Hola, ${nombre}`;
}
/* A pesar que deje el warning, se puede dar el error */
saludar = 30;
// console.log(saludar("Alvaro"));
console.log(saludar);

const saludarConstante = function (nombre) {
  return `Hola, ${nombre}`;
};
/* Da de una vez el error */
// saludarConstante = 20
console.log(saludarConstante('g'));
/* Las funciones arrow tienen más ventajas que una función normal */
const saludarConFlecha = (nombre) => {
  return `Hola, ${nombre}`;
};
const saludarConFlechaImplicito = (nombre) => `Hola, ${nombre}`;
const saludarConFlechaImplicitoSinParam = () => `Hola mundo`;
console.log(saludarConFlecha('Pedro'));
console.log(saludarConFlechaImplicito('Mylou'));
console.log(saludarConFlechaImplicitoSinParam());
/* 
? ¿Se pueden generar returns implicitos con arrow functions y objetos literales?
* Si se puede, dejando el objeto literal rodeado por ()
*/
const getUser = () => ({
  uuid: 'ABC123',
  username: 'Papucho0831',
});
console.log(getUser());

const getUsuarioActivo = (nombre) => ({
  uuid: 'ABC456',
  username: nombre,
});

const userActive = getUsuarioActivo('Alvaro');
console.log(userActive);
