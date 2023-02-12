import React from 'react';
import Home from './pages/Home';
import Charts from './pages/Charts';

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
