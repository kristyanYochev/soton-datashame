import React, { FC } from "react";
import { Pages } from "../utils/enums";
import { SharedProps } from "../utils/props";

import '../styles/Home.css';



const Home: FC<SharedProps> = ({setPage}) => {
  return <div className="hero">
      <div className="title-section">
        <h1 className="title">Soton Shame</h1>
        <h2 className="subtitle">Your campus energy tracker</h2>
      </div>
      <div className="display">
        <button onClick={() => setPage(Pages.Charts)} className="view-charts">View Information</button>
      </div>
    </div>
}

export default Home;