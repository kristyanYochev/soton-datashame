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

    return (
        <>
            {!headline && <h1>Loading...</h1>}
            {headline && (
                <>
                    <div className="section section-1">
                        <h1 className="title">Energy Consumption 2020 (KWH)</h1>
                        <div className="content">
                            {headline.power_consumption_2020}KWH (
                            {(headline.power_consumption_2020 -
                                headline.power_consumption_2019) /
                                headline.power_consumption_2019}
                            )
                        </div>
                    </div>
                    <div className="section section-2">
                        <h1 className="title">Energy Consumption 2019 (KWH)</h1>
                        <div className="content">
                            {headline.power_consumption_2019}KWH
                        </div>
                    </div>
                    <div className="section section-3">
                        <h1 className="title">
                            Biggest Energy Consumer 2020 (KWH)
                        </h1>
                        <h2 className="subtitle">
                            Building{' '}
                            {headline.most_consuming_building.building_code
                                .split('/')[1]
                                .slice(1)}
                        </h2>
                        <div className="content">
                            {headline.most_consuming_building.consumption}KWH
                            (59%)
                        </div>
                    </div>
                    <div className="section section-4">
                        <h1 className="title">
                            Biggest Energy Consumer 2021 (KWH)
                        </h1>
                        <h2 className="subtitle">Building 59</h2>
                        <div className="content">2500K5WH (+15%)</div>
                    </div>
                </>
            )}
        </>
    );
};

export default Headline;
