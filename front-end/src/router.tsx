import Home from './pages/Home';
import Charts from './pages/charts/Charts';

import { createBrowserRouter } from 'react-router-dom';

export default createBrowserRouter([
    {
        path: "/",
        element: <Home />
    },
    {
        path: "/charts",
        element: <Charts />
    }
]);
