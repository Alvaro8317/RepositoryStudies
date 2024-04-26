const apiKey = 'unaApiKey';
const peticion = fetch(
  `https://api.giphy.com/v1/gifs/random?api_key=${apiKey}`
);
/* 
* Promesas sin encadenarse, 
! no se recomiendan 
*/
// peticion
//   .then((response) => {
//     response.json().then((data) => console.log(data));
//   })
//   .catch(console.warn);
/*
 * Caso ideal, promesas en cadena, si una instrucción retorna una promesa, se le pasa al siguiente .then
 */
peticion
  .then((response) => response.json())
  .then(({ data }) => {
    const { url } = data.images.original;
    const img = document.createElement('img');
    img.src = url
    document.body.append(img)
  })
  .catch(console.warn);
