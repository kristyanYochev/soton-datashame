import ReactDOM from 'react-dom/client';
import './index.css';
import './styles/root.css';
import './styles/reset.css';
import reportWebVitals from './reportWebVitals';
import App from './App';


const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
    <App/>
);

reportWebVitals();
