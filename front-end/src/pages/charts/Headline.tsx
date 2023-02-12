import React, { useEffect, useState } from 'react';
import { callApi } from '../../api_call';

import './Headline.css';

type HeadlineData = {
    power_consumption_2019: number;
    power_consumption_2020: number;
    most_consuming_building: {
        building_code: string;
        consumption: number;
    };
};

async function fetchHeadlineData(): Promise<HeadlineData> {
    return callApi('/headline-stats') as Promise<HeadlineData>;
}

const Headline: React.FC = () => {
    const [headline, setHeadline] = useState<HeadlineData>();

    useEffect(() => {
        const init = async () => {
            const headlineData = await fetchHeadlineData();
            setHeadline(headlineData);
            console.log('Load Headline');
        };

        init().catch(console.error);
    }, []);

    const mostConsumingBuildingNumber =
        headline?.most_consuming_building.building_code.split('/')[1].slice(1);

    return (
        <>
            {!headline && <h1 style={{ textAlign: 'center' }}>Loading...</h1>}
            {headline && (
                <div className="cols-2-md">
                    <div className="card">
                        <h1 className="title">
                            <span className="emphasis">
                                {headline.power_consumption_2020.toFixed(0)}
                            </span>{' '}
                            kWh
                        </h1>

                        <h2 className="sub-title">
                            Total Energy Consumption in 2020
                        </h2>
                    </div>
                    <div className="card">
                        <h1 className="title">
                            <span className="emphasis">
                                {headline.power_consumption_2019.toFixed(0)}
                            </span>{' '}
                            kWh
                        </h1>
                        <h2 className="sub-title">
                            Total Energy Consumption in 2019
                        </h2>
                    </div>
                    <div className="card">
                        <h1 className="title">
                            <span className="emphasis">
                                Building {mostConsumingBuildingNumber}
                            </span>{' '}
                            consumed{' '}
                            <span className="emphasis">
                                {headline.most_consuming_building.consumption.toFixed(
                                    0
                                )}
                            </span>{' '}
                            kWh in <span className="emphasis">2020</span>
                        </h1>
                        <h2 className="sub-title">
                            Most Energy-Consuming Building in 2020
                        </h2>
                    </div>
                </div>
            )}
        </>
    );
};

export default Headline;
