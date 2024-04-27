/* Async y await
 * Async se puede usar para simplificar el código con respecto a las promesas
 */

// const getImagePromise = () => new Promise((res, rej) => res('Hay data'));
const apiKey = 'otraApiKey';
const getImage = async () => {
  try {
    const peticion = await fetch(
      `https://api.giphy.com/v1/gifs/random?api_key=${apiKey}`
    );
    const { data } = await peticion.json();
    const { url } = data.images.original;
    const img = document.createElement('img');
    img.src = url;
    console.log(url);
    document.body.append(img);
  } catch {
    console.info("Unexpected error");
  }
};
getImage();
