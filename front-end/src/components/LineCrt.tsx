import React, { PureComponent } from "react";
import {LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip} from 'recharts';

export default class LineCrt extends PureComponent{

  render() {
    // const {data} = this.props;

    return (<div>
      <LineChart width={600} height={300} data={[]} margin={{ top: 5, right: 20, bottom: 5, left: 0 }}>
        <Line type="monotone" dataKey="uv" stroke="#000000" />
        <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
      </LineChart></div>)
  }
};