export const getImagen = async () => {
  try {
    const apiKey = 'Y9MAGIjbSZuNy5MPyK7PwPib5c8lHkyd';
    const resp = await fetch(
      `http://api.giphy.com/v1/gifs/random?api_key=${apiKey}`
    );
    const { data } = await resp.json();

    const { url } = data.images.original;
    return url;
  } catch (error) {
    throw new Error("Unexpected error with the API")
  }
};
