import React from 'react';
// eslint-disable-next-line react/display-name, react/prop-types
export const ShowIncrement = React.memo(({ increment }) => {
  console.log('Me rendericé :(');
  return (
    <button className='btn btn-primary' onClick={() => increment(5)}>
      Incrementar
    </button>
  );
});
