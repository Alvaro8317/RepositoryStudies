/*
 * Cuando se requiera almacenar información y esta va a cambiar el HTML, lo más posible es que exista un hook que lo solucione
 * Se recomienda que un state tenga valor inicial, ya que undefined podría dar varios errores.
 * Cuando inicia on, es porque emite algo, usual en los eventos, onAbort, onClick, onError, etc.
 */

import { useState } from 'react';
import { AddCategory, GifGrid } from './components';
// import { GifGrid } from './components/GifGrid';

export const GifExpertApp = () => {
  const [categories, setCategories] = useState([]);
  const onAddCategory = (newCategory) => {
    if (categories.includes(newCategory)) return;
    setCategories([...categories, newCategory]);
  };

  return (
    <>
      <h1>GifExpertApp</h1>
      <AddCategory onNewCategory={onAddCategory} />
      {categories.map((category) => (
        <GifGrid key={category} category={category} />
      ))}
    </>
  );
};
