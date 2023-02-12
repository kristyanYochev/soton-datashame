import React, { useState, useEffect } from "react";
import './Charts.css'
 
const Charts: React.FC = () => {

  const [select, setSelect] = useState<number>(0);
  const [buildings, setBuildings] = useState<string[]>([]);
  const [buildingData, setBuildingData] = useState<any[]>([]);
  const [headline, setHeadline] = useState<any>(null);

  useEffect(() => {
    fetchRoute('http://localhost:8080/headline-stats').then(objs => {  console.log(objs); return setHeadline(objs);});
  }, []);

  const buttons = [{
                    title: 'General Data', 
                    callback: async (index:number) => { 
                      setBuildingData([]); 
                      setSelect(index);
                      const objs = await fetchRoute('http://localhost:8080/headline-stats');
                      setHeadline(objs);
                    }}, 
                   {
                    title: "Show All Buildings", 
                    callback: async (index:number) => { 
                      setSelect(index); 
                      setBuildingData([]);
                      const objs = await fetchRoute('http://localhost:8080/buildings'); 
                      setBuildings(objs); 
                    }}]


  async function fetchRoute(route: string): Promise<any> {
    const response = await fetch(route, {mode: 'cors'});
    const data = await response.json();
    return data;
  }

  return <div className="charts">
    <div className="header">
      <h1 className="title">Data</h1>
      <a href="/" className="back">Home</a>
    </div>
    <div className="options">
      <div className="content">
        {buttons.map((btn, index) => {
          return <button key={index.toString()} className={"btn " + (index === select ? "btn-active" : "")} onClick={() => btn.callback(index)} >{btn.title}</button>
        })}
      </div>
    </div>
    <div className="data">

      {select === 0 && headline !== null && (<div className="wrapper">
                        <div className="section section-1">
                          <h1 className="title">Energy Consumption 2020 (KWH)</h1>
                          <div className="content">{headline.power_consumption_2020}KWH ({(headline.power_consumption_2020 - headline.power_consumption_2019)/headline.power_consumption_2019})</div>
                        </div>
                        <div className="section section-2">
                          <h1 className="title">Energy Consumption 2019 (KWH)</h1>
                          <div className="content">{headline.power_consumption_2019}KWH</div>
                        </div>
                        <div className="section section-3">
                          <h1 className="title">Biggest Energy Consumer 2020 (KWH)</h1>
                          <h2 className="subtitle">Building {headline.most_consuming_building.building_code.split('/')[1].slice(1)}</h2>
                          <div className="content">{headline.most_consuming_building.consumption}KWH (59%)</div>
                        </div>
                        <div className="section section-4">
                          <h1 className="title">Biggest Energy Consumer 2021 (KWH)</h1>
                          <h2 className="subtitle">Building 59</h2>
                          <div className="content">2500K5WH (+15%)</div>
                        </div>
                      </div>) }
      {select === 1 && (<div className="wrapper">
                        {Object.values(buildings).map((building, index) => {
                            return <button key={index.toString()} className={"btn"} onClick={async () => {setSelect(-1); const data = await fetchRoute(`http://localhost:8080/buildings/${building}?stat_type=average`); setBuildingData(data);}} >{"Building " + building.split('/')[1].slice(1).toUpperCase()}</button>
                          })}
                      </div>)}
      {/* {select === -1 && (<div className="wrapper">
                            <LineChart width={800} height={600} data={convertBuildingData()}>
                              <CartesianGrid strokeDasharray="3 3" />
                              <XAxis dataKey="date"/>
                              <YAxis/>
                              <Tooltip/>
                              <Legend/>
                              <Line type="monotone" dataKey="kwh" stroke="#8884d8" />
                            </LineChart>
                      </div>)} */}
      
    </div>
  </div>
}

export default Charts;