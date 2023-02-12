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
    const [selected, setSelected] = useState<string>('');
    const [buildings, setBuildings] = useState<string[]>([]);
    const [data, setData] = useState<SampleData>();

    async function getBuildingData() {

        const chartData = await fetchChartData(selected);
        setData(chartData);
    }

    async function changeBuilding(event:any) {
        console.log(event.target.value);
        setSelected(event.target.value);
    }

    useEffect(() => {
        const init = async () => {
            const buildingsList = await callApi('/buildings');
            setBuildings(buildingsList);
            setSelected('elec/b1/ekw');
        };

        init().catch(console.error);
    }, []);

    useEffect(() => {
        console.log(selected);
        getBuildingData();
    }, [selected]);

    return (
        <>
            <div className="selection">
                <label htmlFor="buildings" className='label'>Select Building: </label>
                <select name="Buildings" id="buildings" className="buildings" onChange={changeBuilding}>
                    {buildings.map((building) => {
                        return <option key={building} value={building}>{"Building " + building.split('/')[1].slice(1).toUpperCase()}</option>
                    })}
                </select>
            </div>
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
