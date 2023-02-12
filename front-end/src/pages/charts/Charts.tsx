import React from 'react';
import DataVisualisation from './Chart';
import './Charts.css';
import Headline from './Headline';

const Charts: React.FC = () => {
    return (
        <div className="charts">
            <div className="header">
                <h1 className="title">Data</h1>
                <a href="/" className="back">
                    Home
                </a>
            </div>
            <Headline />
            <DataVisualisation />
        </div>
    );
};

export default Charts;
