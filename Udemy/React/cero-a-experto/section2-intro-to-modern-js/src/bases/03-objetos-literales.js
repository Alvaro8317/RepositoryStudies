/* Estas llaves {} significa que se trata de un objeto literal */
const person = {
  nombre: 'Tony',
  apellido: 'Stark',
  age: 45 /* Es buena práctica dejar la coma al final del objeto literal */,
  direccion: {
    calle: 17,
    numero: 8,
    codigoPostal: 250040,
  },
};
/* Se imprime directamente los datos del objeto literal */
console.log(person);
/* Hacer esto */
console.log({ person });
/* Es lo mismo que esto */
console.log({ person: person });
console.table({ person: person });

const person2 = person;
const person3 = {...person}
person2.nombre = 'Peter';
/* Al modificar person2, modifica también person, porque apuntan al mismo espacio en memoria */
console.log({person});
console.log({person2});

/* Spread operator, se usa para copiar de manera segura un objeto literal */
console.log({person3})