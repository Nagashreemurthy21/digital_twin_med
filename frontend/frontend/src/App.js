import { useState } from "react";
import axios from "axios";
import "./App.css";

const API_BASE = "http://127.0.0.1:8000";

function App() {
  const [device, setDevice] = useState("Ventilator");

  // Ventilator state
  const [motorSpeed, setMotorSpeed] = useState(120);

  // CGM state
  const [glucose, setGlucose] = useState(140);

  // Result
  const [output, setOutput] = useState(null);
  const [loading, setLoading] = useState(false);

  const runSimulation = async () => {
    setLoading(true);
    setOutput(null);

    try {
      let response;

      if (device === "Ventilator") {
        response = await axios.post(`${API_BASE}/simulate`, {
          motor_speed: Number(motorSpeed)
        });
      } else {
        response = await axios.post(`${API_BASE}/simulate-cgm`, {
          glucose_level: Number(glucose)
        });
      }

      setOutput(response.data);
    } catch (error) {
      setOutput({ error: "Backend not reachable" });
    }

    setLoading(false);
  };

  return (
    <div className="app-container">
      <h1>🧠 GenAI Medical Digital Twin</h1>
      <p className="subtitle">
        Class-II & Class-III Medical Device Simulation Platform
      </p>

      {/* Device Selector */}
      <div className="card">
        <label>Device Type</label>
        <select value={device} onChange={e => setDevice(e.target.value)}>
          <option value="Ventilator">Ventilator (Class III)</option>
          <option value="CGM">Continuous Glucose Monitor (Class II)</option>
        </select>
      </div>

      {/* Ventilator Controls */}
      {device === "Ventilator" && (
        <div className="card">
          <label>Motor Speed (RPM): {motorSpeed}</label>
          <input
            type="range"
            min="50"
            max="300"
            value={motorSpeed}
            onChange={e => setMotorSpeed(e.target.value)}
          />
        </div>
      )}

      {/* CGM Controls */}
      {device === "CGM" && (
        <div className="card">
          <label>Glucose Level (mg/dL): {glucose}</label>
          <input
            type="range"
            min="40"
            max="300"
            value={glucose}
            onChange={e => setGlucose(e.target.value)}
          />
        </div>
      )}

      {/* Action Button */}
      <button onClick={runSimulation} disabled={loading}>
        {loading ? "Running Simulation..." : "Run Digital Twin"}
      </button>

      {/* Output */}
      {output && (
        <div className="output-card">
          <h3>Simulation Output</h3>
          <pre>{JSON.stringify(output, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
