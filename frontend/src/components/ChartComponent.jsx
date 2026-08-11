import React from "react";
import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
} from "chart.js";
import { Line } from "react-chartjs-2";

ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement);

const ChartComponent = ({ data }) => {
  const chartData = {
    labels: data.map(item =>
      new Date(item.timestamp).toLocaleTimeString()
    ),
    datasets: [
      {
        label: "Distance",
        data: data.map(item => item.distance),
        borderColor: "#4f46e5",
        backgroundColor: "rgba(79,70,229,0.2)",
        tension: 0.4,
      },
      {
        label: "Flow",
        data: data.map(item => item.flow),
        borderColor: "#16a34a",
        backgroundColor: "rgba(22,163,74,0.2)",
        tension: 0.4,
      },
    ],
  };

  return (
    <div className="chart-container">
      <h3>Sensor Trends</h3>
      <Line data={chartData} />
    </div>
  );
};

export default ChartComponent;
