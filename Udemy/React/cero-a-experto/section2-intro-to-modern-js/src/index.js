const active = true;
let message = '';
/* Sin usar operador ternario */
if (active) {
  message = true;
} else {
  message = false;
}

console.log(message);

/* Con operador ternario */
const message2 = active ? 'Activo' : 'Inactivo';
console.log(message2);


const message3 = active && 'Activo'
console.log(message3)
