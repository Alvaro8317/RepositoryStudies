const characters = ['Naruto', 'Sasuke', 'Hinata'];
console.log(characters[0]);
console.log(characters[1]);
console.log(characters[2]);
/* Desestructuración de arreglos */
const [p1] = characters;
const [, p2] = characters;
const [, , p3] = characters;
console.log(p1);
console.log(p2);
console.log(p3);

const returnArray = () => ['ABC', 123];
const [letters, numbers] = returnArray();
console.log(letters);
console.log(numbers);

const useState = (value) => [
  value,
  () => {
    return 'Hola mundo';
  },
];
/* Sin desestructuración */
const arr = useState('Alvaro');
console.log(arr);
console.log(arr[1]());
/* Con desestructuración */
const [nombre, setNombre] = useState('Alvaro');
console.log(nombre)
console.log(setNombre())
