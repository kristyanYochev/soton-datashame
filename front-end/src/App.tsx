import Home from './pages/Home';
import Charts from './pages/Charts';
import React, { useEffect, useState } from 'react';
import { Pages } from './utils/enums';

function pageToLoad(page: Pages, setPage:any) {
  switch(page) {
    case Pages.Home:
      return <Home setPage={setPage}/>
    case Pages.Charts:
      return <Charts setPage={setPage}/>
    default:
      return;
  }
}

const App = () => {
  const [page, setPage] = useState(Pages.Home);

  useEffect(() => {
    const pageObj = localStorage.getItem('page');

    const page = pageObj == null ? null: JSON.parse(pageObj); 
    
    setPage(page ? page : Pages.Home);

  }, [])

  useEffect(()=> {
    localStorage.setItem('page', JSON.stringify(page))
  }, [page])

  return (<div className='app'>{pageToLoad(page, setPage)}</div>)
}

export default App;

