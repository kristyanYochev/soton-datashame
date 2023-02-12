import React, { useEffect, useState } from 'react';
import { callApi } from '../../api_call';
import {
    Chart as ChartJS,
    BarElement,
    Tooltip,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
} from 'chart.js';
import { Line } from 'react-chartjs-2';

ChartJS.register(
    BarElement,
    Tooltip,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement
);

type SampleData = { value: number; timestamp: number }[];

async function fetchChartData(building_code: string): Promise<SampleData> {
    return callApi(`/buildings/${building_code}?stat_type=average`);
}

const DataVisualisation: React.FC = () => {
    const [data, setData] = useState<SampleData>();

    useEffect(() => {
        const init = async () => {
            const chartData = await fetchChartData('elec/b16/ekw');
            setData(chartData);
            console.log('Should have finishe dloading chart');
        };

        init().catch(console.error);
    }, []);

    return (
        <>
            {!data && <h1>Loading...</h1>}
            {data && (
                <Line
                    data={{ datasets: [{ data }] }}
                    options={{
                        parsing: { xAxisKey: 'timestamp', yAxisKey: 'value' },
                    }}
                />
            )}
        </>
    );
};

export default DataVisualisation;
