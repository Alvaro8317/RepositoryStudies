/* Los template string se usan para multi línea o para meter variables en cadenas string */
const myName = 'Alvaro';
const lastName = 'Garzón';
/* Convencional, antes */
const completeName = myName + ' ' + lastName;
console.log(completeName);
/* Con template strings */
console.log(`Hola, soy 
${myName} 
${lastName} y 1+1 da: ${1 + 1}`);
function getSaludo(nameParam) {
  return `Hola ${nameParam}`;
}
console.log(
  `Invocación a la función: ${getSaludo()}, si no se envía parámetro, todo es undefined, 
  ahora se envía parámetro: ${getSaludo('Alvaro')}`
);
