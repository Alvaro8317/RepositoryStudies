/*
 * documentación: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment
 */
/* Desestructuración o asignación desestructurante */
const persona = {
  name: 'Tony',
  edad: 45,
  clave: 'Iron man',
  rango: 'Soldado',
};
/* Forma de acceder a cada uno de los elementos */
console.log(persona.name);
console.log(persona.edad);
console.log(persona.clave);
/* Hace un mapeo entre el objeto literal y la variable a asignar */
const { clave, name: namePersona, edad: edadPersona } = persona;
console.log(namePersona, edadPersona, clave);
/*
 * La desestructuración también se aplica para funciones en parámetros
 * También se puede dejar valores por defecto
 */
const returnPerson = (user, { name: nombre, edad, rango = 'Capitan' }) => {
  console.log(user);
  console.log(nombre);
  console.log(edad);
  console.log(rango);
};
returnPerson(persona, persona);
const useContext = ({ clave, edad }) => ({
  nombreClave: clave,
  anios: edad,
  /* Para desestructurar un objeto dentro de otro objeto se usa latlng:{x, y} */
  latlng: {
    lat: 154.32,
    lng: -0.234,
  },
});
const {
  nombreClave,
  anios,
  /* Desestructuración anidada */
  latlng: { lat, lng },
} = useContext(persona);
console.log(nombreClave, anios);
console.log(lat, lng)
