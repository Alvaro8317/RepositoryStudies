import { useFetch } from '../hooks';
import { useCounter } from '../hooks/useCounter';
import { LoadingMessage } from './LoadingMessage';
import { PokemonCard } from './PokemonCard';
/*
 * Los componentes mantienen renderizándose una y otra vez, hay varias razones por las cuales podrían cambiar
 * Un listado de dependencias vacío significa que ejecutará el efecto secundario una vez que se rendice el componente
 */
export const MultipleCustomHooks = () => {
  const { counter, decrement, increment } = useCounter(1);
  const { data, hasError, isLoading } = useFetch(
    `https://pokeapi.co/api/v2/pokemon/${counter}`
  );
  return (
    <>
      <h1>Pokeapi</h1>
      <hr />
      <pre>Pokemon info</pre>
      {/* {isLoading && <p>Cargando... </p>} */}
      {isLoading ? (
        <LoadingMessage />
      ) : (
        <PokemonCard
          id={counter}
          name={data.name}
          sprites={[
            data.sprites.front_default,
            data.sprites.front_shiny,
            data.sprites.back_default,
            data.sprites.back_shiny,
          ]}
        />
      )}
      {/* <h2>{data?.name}</h2> */}
      {/* <pre>{JSON.stringify(data, null, 2)}</pre> */}
      <button
        onClick={() => (counter > 1 ? decrement() : null)}
        className='btn btn-primary mt-2'
        type='button'
      >
        Anterior
      </button>
      <button
        onClick={() => increment()}
        className='btn btn-primary mt-2'
        type='button'
      >
        Siguiente
      </button>
    </>
  );
};
