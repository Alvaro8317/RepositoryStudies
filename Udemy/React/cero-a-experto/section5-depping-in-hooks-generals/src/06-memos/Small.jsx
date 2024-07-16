import React from 'react';
// eslint-disable-next-line react/display-name, react/prop-types
export const Small = React.memo(({ value }) => {
  console.log('Me volví a dibujar :(');
  return <small>{value}</small>;
});
