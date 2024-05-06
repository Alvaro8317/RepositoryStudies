import { useEffect, useState } from 'react';
import { getGifs } from '../helpers/getGifs';

/*
 * Un hook no es más que una función que regresa algo
 */
export const useFetchGifs = (category) => {
  const [images, setImages] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const getImages = async () => {
    const gifs = await getGifs(category);
    setImages(gifs);
    setIsLoading(false);
  };
  useEffect(() => {
    getImages();
  }, []);
  return {
    images,
    isLoading,
  };
};
