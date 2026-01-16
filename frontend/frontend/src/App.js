import { useState } from "react";
import axios from "axios";
import "./App.css";

const API_BASE = "http://127.0.0.1:8000";

function App() {
  const [device, setDevice] = useState("Ventilator");
  const [motorSpeed, setMotorSpeed] = useState(120);
  const [glucose, setGlucose] = useState(140);
  const [output, setOutput] = useState(null);
  const [loading, setLoading] = useState(false);

  const runSimulation = async () => {
    setLoading(true);
    setOutput(null);

    try {
      const response =
        device === "Ventilator"
          ? await axios.post(`${API_BASE}/simulate`, {
              motor_speed: motorSpeed
            })
          : await axios.post(`${API_BASE}/simulate-cgm`, {
              glucose_level: glucose
            });

      setOutput(response.data);
    } catch (err) {
      setOutput({ error: "Backend not reachable" });
    }

    setLoading(false);
  };

  return (
    <div className="app-container fade-in">
      <h1>🧠 GenAI Medical Digital Twin</h1>
      <p className="subtitle">Interactive Medical Device Simulation</p>

      {/* Device Selector */}
      <div className="card">
        <label>Device Type</label>
        <select value={device} onChange={e => setDevice(e.target.value)}>
          <option>Ventilator</option>
          <option>CGM</option>
        </select>
      </div>

      {/* Controls */}
      {device === "Ventilator" && (
        <div className="card">
          <label>Motor Speed: <strong>{motorSpeed} RPM</strong></label>
          <input
            type="range"
            min="50"
            max="300"
            value={motorSpeed}
            onChange={e => setMotorSpeed(+e.target.value)}
          />
        </div>
      )}

      {device === "CGM" && (
        <div className="card">
          <label>Glucose Level: <strong>{glucose} mg/dL</strong></label>
          <input
            type="range"
            min="40"
            max="300"
            value={glucose}
            onChange={e => setGlucose(+e.target.value)}
          />
        </div>
      )}

      <button onClick={runSimulation} disabled={loading}>
        {loading ? "⏳ Simulating..." : "▶ Run Digital Twin"}
      </button>

      {/* Output Dashboard */}
      {output?.simulation_result && (
        <div className="dashboard slide-up">
          {device === "Ventilator" && (
            <>
              <Metric label="Airflow (L/min)" value={output.simulation_result.airflow_lpm} />
              <Metric label="Pressure (cmH₂O)" value={output.simulation_result.pressure_cmH2O} />
              <Metric label="Power (W)" value={output.simulation_result.power_W} />

              <StatusBadge status={output.simulation_result.alarm_status} />
            </>
          )}

          {device === "CGM" && (
            <>
              <Metric label="Sensor Reading" value={output.simulation_result.sensor_reading} />
              <Metric label="ADC Value" value={output.simulation_result.adc_value} />

              <StatusBadge status={output.simulation_result.alert_status} />
            </>
          )}
        </div>
      )}
    </div>
  );
}

const Metric = ({ label, value }) => (
  <div className="metric">
    <span>{label}</span>
    <strong>{value}</strong>
  </div>
);

const StatusBadge = ({ status }) => {
  const color =
    status.includes("NORMAL") ? "green" :
    status.includes("LOW") || status.includes("HYPO") ? "orange" :
    "red";

  return <div className={`status ${color}`}>{status}</div>;
};

export default App;
