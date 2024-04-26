console.log('Hola mundo');
/* Variables y constantes */
/* No usar más var */
/* Constantes que crean el espacio en memoria */
const myName = 'Alvaro';
/* Variable que puede cambiar */
let lastName = 'Garzón';
lastName = 'Garzón Pira';
console.log(myName, lastName);

if (true) {
  /* Es una variable de scope, cuando se acaba el bloque de código, se borra la variable */
  /* Esta MyName son completamente distintas */
  /* Var lleva a múltiples errores */
  const myName = 'Alvaro Eduardo';
  console.log(myName);
}

console.log(myName);
