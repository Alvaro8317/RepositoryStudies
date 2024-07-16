import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom'
import { MainApp } from './10-useContext/MainApp';
import './index.css';
ReactDOM.createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <MainApp />
  </BrowserRouter>
);
