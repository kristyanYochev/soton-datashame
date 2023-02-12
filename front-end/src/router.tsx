import Home from './pages/Home';
import Charts from './pages/charts/Charts';
import Headline from './pages/charts/Headline';

import { createBrowserRouter } from 'react-router-dom';

export default createBrowserRouter([
    {
        path: '',
        element: <Home />,
    },
    {
        path: 'charts',
        element: <Charts />,
        children: [
            {
                path: '',
                element: <Headline />,
            },
        ],
    },
]);
