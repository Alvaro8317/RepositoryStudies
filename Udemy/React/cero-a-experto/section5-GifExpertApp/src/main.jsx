import ReactDOM from 'react-dom/client';
import { GifExpertApp } from './GifExpertApp.jsx';
import './Styles.css'
/* 
* El modo estricto solo se usa en desarrollo, al generar el build de producción no es afectado por el strict mode, esta es una doble verificación que react hace para validar que todo va a funcionar como se espera.
*/
ReactDOM.createRoot(document.getElementById('root')).render(
  // <React.StrictMode>
    <GifExpertApp />
  // </React.StrictMode>
);
