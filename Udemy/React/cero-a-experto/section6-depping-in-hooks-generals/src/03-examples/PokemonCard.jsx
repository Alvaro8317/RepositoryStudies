import PropTypes from 'prop-types';
import { useLayoutEffect, useRef, useState } from 'react';
export const PokemonCard = ({ id, name, sprites = [] }) => {
  const pRef = useRef();
  const [boxSize, setBoxSize] = useState({ width: 0, height: 0 });
  useLayoutEffect(() => {
    const { height, width } = pRef.current.getBoundingClientRect();
    setBoxSize({ width, height });
  }, []);
  return (
    <>
      <section style={{ height: 200 }}>
        <h2 className='text-capitalize' ref={pRef}>
          #{id} - {name}
        </h2>
        <div className='container'>
          {sprites.map((sprite) => {
            return <img src={sprite} alt={name} key={sprite} />;
          })}
        </div>
      </section>
      <code>{JSON.stringify(boxSize)}</code>
    </>
  );
};
PokemonCard.propTypes = {
  id: PropTypes.number.isRequired,
  name: PropTypes.string.isRequired,
  sprites: PropTypes.array,
};
