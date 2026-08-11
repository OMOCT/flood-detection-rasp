import { useState, useEffect } from "react"
import DataTable from "../components/DataTable"
import api from "../api"
import ChartComponent from "../components/ChartComponent"
import "../styles/Home.css"

function Home() {
  const [flooddata, setFlooddata] = useState([]);
  const [status, setStatus] = useState("");

  useEffect(() => {
    const interval = setInterval(() => {
      getData();
    }, 1000);
    return () => clearInterval(interval);
  }, [])

  const getData = () => {
    api.get("/api/flooddata/")
      .then((res) => res.data)
      .then((data) => { setFlooddata(data); console.log(data) })
      .catch((err) => alert(err));
  }

  return (
    <>
      {/* <DataTable data={flooddata}/> */}
      <div className="dashboard">
      <h1>Flood Monitoring Dashboard</h1>

      <div className="cards">
        <div className="card" >🌊 Status: <span style={{
            color:
              flooddata[0]?.status === "danger" ? "red":
              flooddata[0]?.status === "warning" ? "orange": "green"
          }}>{flooddata[0]?.status}</span></div>
        <div className="card">📏 Distance: {flooddata[0]?.distance}</div>
        <div className="card">💧 Flow: {flooddata[0]?.flow}</div>
      </div>

      <div className="grid">
        <DataTable data={flooddata} />
        <ChartComponent data={flooddata} />
      </div>
    </div>
    </>
  )
}

export default Home
