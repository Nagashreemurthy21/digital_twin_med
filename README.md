# digital_twin_med

# 🧠 GenAI Medical Digital Twin Platform

A **GenAI-powered Digital Twin system** for **medical devices**, simulating real-world behavior, safety, and compliance for **Class II & Class III devices** such as **Ventilators** and **Continuous Glucose Monitors (CGM)**.

This project combines **Digital Twin simulation**, **medical compliance validation**, and **Generative AI–based system design** with an interactive frontend dashboard.

---

## 🚀 Features

### 🔹 Digital Twin Simulation
- Ventilator airflow, pressure, power & alarm simulation
- CGM glucose sensing, ADC conversion & alert logic
- Physics-inspired and clinically meaningful models

### 🔹 Medical Compliance Engine
- ISO 60601-1 (Electrical Safety)
- ISO 14971 (Risk Management)
- Automatic hazard identification & mitigation suggestions

### 🔹 GenAI System Design
- Requirement → Architecture generation
- Deterministic generator (demo/exam safe)
- Optional LLaMA / TinyLLaMA integration with fallback

### 🔹 Interactive Frontend
- Clean medical-grade dashboard UI
- Live sliders & real-time feedback
- Status badges for alarms & alerts
- Smooth animations and modern UX

---

## 🏗️ Tech Stack

### Frontend
- React.js
- Axios
- CSS (custom dashboard styling)

### Backend
- FastAPI
- Pydantic
- NumPy

### GenAI
- Hugging Face Transformers
- TinyLLaMA (CPU-friendly)
- Safe JSON extraction with fallback logic

---

## 📂 Project Structure

digital_twin_med/
│
├── backend/
│ ├── main.py
│ ├── digital_twin.py
│ ├── cgm_digital_twin.py
│ ├── compliance.py
│ ├── genai_engine.py
│ ├── llama_engine.py
│ ├── models.py
│ └── requirements.txt
│
├── frontend/
│ └── frontend/
│ ├── src/
│ │ ├── App.js
│ │ ├── App.css
│ │ └── index.js
│ └── package.json
│
└── README.md



---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Nagashreemurthy21/digital_twin_med.git
cd digital_twin_med


▶️ Running the Backend (FastAPI)
cd backend
pip install -r requirements.txt
uvicorn main:app --reload


▶️ Running the Frontend (React)
cd frontend/frontend
npm install
npm install axios
npm start


🧪 How to Use
1.Select Ventilator or CGM
2.Adjust simulation parameters using sliders
3.Click Run Digital Twin
4.View live metrics, alerts, and compliance status



👩‍💻 Author
Nagashree Murthy
GitHub: https://github.com/Nagashreemurthy21


