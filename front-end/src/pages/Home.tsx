import React from "react";

import './Home.css';

const Home: React.FC = () => {
  return <div className="hero">
      <div className="title-section">
        <h1 className="title">Watt A Shame</h1>
        <h2 className="subtitle">Turning up the heat on energy waste.</h2>
      </div>
      <div className="display">
        <a href="/charts" className="view-charts">View Information</a>
      </div>
    </div>
}

export default Home;