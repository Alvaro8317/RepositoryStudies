/*
 * las funciones dispatcher le dirán a react que debe de renderizar el componente, una se estas es ejemplo, setState
* tanStackQuery permite manejar caché con funcionalidades extensas
 */
import { useEffect, useState } from 'react';
const localCache = {};

export const useFetch = (url) => {
  const [state, setState] = useState({
    data: null,
    isLoading: true,
    hasError: false,
    errorMessage: null,
  });
  const setLoadingState = () => {
    setState({
      data: null,
      isLoading: true,
      hasError: false,
      error: null,
    });
  };
  const getFetch = async () => {
    if (localCache[url]) {
      console.log('Usando caché');
      setState({
        data: localCache[url],
        isLoading: false,
        hasError: false,
        errorMessage: null,
      });
      return;
    }
    setLoadingState();
    const response = await fetch(url);
    await new Promise((resolve) => setTimeout(resolve, 2000));
    if (!response.ok) {
      setState({
        data: null,
        isLoading: false,
        hasError: true,
        errorMessage: response.statusText,
      });
      return;
    }
    const data = await response.json();
    setState({
      data,
      isLoading: false,
      hasError: false,
      errorMessage: null,
    });
    localCache[url] = data;
  };
  useEffect(() => {
    getFetch();
  }, [url]);

  const { data, isLoading, hasError } = state;
  return {
    data,
    isLoading,
    hasError,
  };
};
