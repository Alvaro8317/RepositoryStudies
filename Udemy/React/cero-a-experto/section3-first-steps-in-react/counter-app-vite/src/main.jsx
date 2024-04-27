/* Importación a React */
import React from 'react';
/* Herramienta para renderizar react */
import ReactDOM from 'react-dom/client';
/* Aquí se importan los estilos globales */
import './index.css';
import CounterApp from './CounterApp';
/* Se renderiza */


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <CounterApp value={123}></CounterApp>
  </React.StrictMode>
);
