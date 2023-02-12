import React, { useState, useEffect } from 'react';
import { Outlet } from 'react-router-dom';
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
        </div>
    );
};

export default Charts;
