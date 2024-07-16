/*
 * Dejar una función port fuera del componente es mejor para evitar que se renderice la función
 * useEffect es para lanzar efectos secundarios, el primer parámetro es una función que se quiere ejecutar y el segundo, que es opcional - obligatorio que son las dependencias
 * En JSX no se usa class porque se puede confundir, para clases CSS se deja className
 * Esparcir las propiedades
 */

import PropTypes from 'prop-types';
import { useFetchGifs } from '../hooks/useFetchGifs';
// import { GifItem } from './GifItem'; Sin importación barril
import { GifItem } from './GifItem';
/*
 * Los custom hooks se recomienda que empiecen por use
 */

export const GifGrid = ({ category }) => {
  const { images, isLoading } = useFetchGifs(category);
  console.log(images, isLoading);

  return (
    <>
      <h3>{category}</h3>
      {/* Tecnica para dejar un cargando: */}
      {isLoading && <h2>Cargando...</h2>}
      <div className='card-grid'>
        {images.map((image) => (
          <GifItem key={image.id} {...image} />
        ))}
      </div>
    </>
  );
};

GifGrid.propTypes = {
  category: PropTypes.string.isRequired,
};
