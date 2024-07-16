import { useFetch } from '../hooks';
import { useCounter } from '../hooks/useCounter';
import { LoadingMessage } from '../03-examples/LoadingMessage';
import { PokemonCard } from '../03-examples/PokemonCard';
export const Layout = () => {
  const { counter, decrement, increment } = useCounter(1);
  const { data, hasError, isLoading } = useFetch(
    `https://pokeapi.co/api/v2/pokemon/${counter}`
  );
  return (
    <>
      <h1>Pokeapi</h1>
      <hr />
      <pre>Pokemon info</pre>
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
