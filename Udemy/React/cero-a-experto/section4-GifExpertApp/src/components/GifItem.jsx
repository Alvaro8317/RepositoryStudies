import PropTypes from 'prop-types';
export const GifItem = ({ title, url }) => {
  return (
    <div className='card'>
      <img src={url} alt={title} />
      <p> {title} </p>
      {/* <ol>
        <li key={image.id}>{image.title}</li>
      </ol> */}
    </div>
  );
};

GifItem.propTypes = {
  title: PropTypes.string.isRequired,
  url: PropTypes.string.isRequired,
};
