import React, { useState, useEffect } from 'react';
import { Outlet } from 'react-router-dom';
import './Charts.css';

const Charts: React.FC = () => {
    const [select, setSelect] = useState<number>(0);
    const [buildings, setBuildings] = useState<string[]>([]);
    const [buildingData, setBuildingData] = useState<any[]>([]);
    const [headline, setHeadline] = useState<any>(null);

    useEffect(() => {
        fetchRoute('http://localhost:8080/headline-stats').then((objs) => {
            console.log(objs);
            return setHeadline(objs);
        });
    }, []);

    const buttons = [
        {
            title: 'General Data',
            callback: async (index: number) => {
                setBuildingData([]);
                setSelect(index);
                const objs = await fetchRoute(
                    'http://localhost:8080/headline-stats'
                );
                setHeadline(objs);
            },
        },
        {
            title: 'Show All Buildings',
            callback: async (index: number) => {
                setSelect(index);
                setBuildingData([]);
                const objs = await fetchRoute(
                    'http://localhost:8080/buildings'
                );
                setBuildings(objs);
            },
        },
    ];

    async function fetchRoute(route: string): Promise<any> {
        const response = await fetch(route, { mode: 'cors' });
        const data = await response.json();
        return data;
    }

    return (
        <div className="charts">
            <div className="header">
                <h1 className="title">Data</h1>
                <a href="/" className="back">
                    Home
                </a>
            </div>
            <div className="options">
                <div className="content">
                    {buttons.map((btn, index) => {
                        return (
                            <button
                                key={index.toString()}
                                className={
                                    'btn ' +
                                    (index === select ? 'btn-active' : '')
                                }
                                onClick={() => btn.callback(index)}
                            >
                                {btn.title}
                            </button>
                        );
                    })}
                </div>
            </div>
            <Outlet />
            {/* <div className="data">
                {select === 0 && headline !== null && (
                    <div className="wrapper"></div>
                )}
                {select === 1 && (
                    <div className="wrapper">
                        {Object.values(buildings).map((building, index) => {
                            return (
                                <button
                                    key={index.toString()}
                                    className={'btn'}
                                    onClick={async () => {
                                        setSelect(-1);
                                        const data = await fetchRoute(
                                            `http://localhost:8080/buildings/${building}?stat_type=average`
                                        );
                                        setBuildingData(data);
                                    }}
                                >
                                    {'Building ' +
                                        building
                                            .split('/')[1]
                                            .slice(1)
                                            .toUpperCase()}
                                </button>
                            );
                        })}
                    </div>
                )}
                {select === -1 && (<div className="wrapper">
                            <LineChart width={800} height={600} data={convertBuildingData()}>
                              <CartesianGrid strokeDasharray="3 3" />
                              <XAxis dataKey="date"/>
                              <YAxis/>
                              <Tooltip/>
                              <Legend/>
                              <Line type="monotone" dataKey="kwh" stroke="#8884d8" />
                            </LineChart>
                      </div>)}
            </div> */}
        </div>
    );
};

export default Charts;
