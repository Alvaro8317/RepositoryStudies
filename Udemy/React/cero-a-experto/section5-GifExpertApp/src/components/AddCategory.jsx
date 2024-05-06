import { useState } from 'react';

/*
 * Cada componente puede tener sus propios estados, es decir, sus propios hooks o states
 * Por defecto un form al darle submit o enter, refresca la página, se puede evitar con preventDefault()
 */
import PropTypes from 'prop-types';
export const AddCategory = ({ onAddCategories, onNewCategory }) => {
  const [inputValue, setInputValue] = useState('');
  const onInputChange = ({ target }) => {
    setInputValue(target.value);
  };
  const onSubmit = (event) => {
    event.preventDefault();
    if (!onAddCategories)
      console.log('Using communications from son to father components');
    if (inputValue.trim().length <= 1) return;
    /* Se realiza la inserción desde el componente hijo y no desde el padre, no se recomienda porque se desconoce la implementació y toca implementar la lógica desde los hijos, si se tiene 10 hijos, toca repetir esta misma lógica 10 veces */
    // onAddCategories((categories) => [...categories, inputValue]);
    /* Se realiza la inserción enviandole al componente padre el valor */
    onNewCategory(inputValue.trim());
    setInputValue('');
  };
  return (
    <form onSubmit={onSubmit}>
      <input
        type='text'
        placeholder='Search gifs'
        value={inputValue}
        onChange={onInputChange}
      />
    </form>
  );
};

AddCategory.propTypes = {
  onAddCategories: PropTypes.func,
  onNewCategory: PropTypes.func.isRequired,
};
