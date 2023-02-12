import React, { FC } from "react";

import '../styles/Home.css';



const Home: FC = () => {
  return <div className="hero">
      <div className="title-section">
        <h1 className="title">Soton Shame</h1>
        <h2 className="subtitle">Your campus energy tracker</h2>
      </div>
      <div className="display">
        <a href="/charts" className="view-charts">View Information</a>
      </div>
    </div>
}

export default Home;