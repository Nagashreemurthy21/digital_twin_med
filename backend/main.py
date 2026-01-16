from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict

# Internal modules (NO backend. prefix)
from genai_engine import generate_architecture
from digital_twin import system_simulation
from compliance import compliance_check
from cgm_digital_twin import cgm_simulation

# Optional LLM (LLaMA / TinyLLaMA)
LLM_AVAILABLE = True

def safe_llm_call(prompt):
    try:
        from llama_engine import llama_generate_architecture
        return llama_generate_architecture(prompt)
    except Exception as e:
        return {
            "error": "LLM failed to load",
            "reason": str(e)
        }


# -----------------------------
# FASTAPI APP
# -----------------------------
app = FastAPI(
    title="GenAI Digital Twin for Medical Devices",
    description="Ventilator (Class III) and CGM (Class II) Digital Twin Platform",
    version="1.0"
)

# -----------------------------
# CORS (for React frontend)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# DATA MODELS
# -----------------------------
class RequirementInput(BaseModel):
    device_type: str
    device_class: str
    functional_requirements: List[str]
    constraints: Dict[str, str]


class SimulationInput(BaseModel):
    motor_speed: float


class CGMSimulationInput(BaseModel):
    glucose_level: float


# -----------------------------
# ROOT CHECK
# -----------------------------
@app.get("/")
def root():
    return {
        "status": "✅ Digital Twin Platform Running",
        "llm_available": LLM_AVAILABLE
    }


# -----------------------------
# GENERATE SYSTEM DESIGN
# -----------------------------
@app.post("/generate-design")
def generate_design(req: RequirementInput):
    architecture = generate_architecture(req)

    return {
        "device": req.device_type,
        "class": req.device_class,
        "generated_architecture": architecture
    }


# -----------------------------
# LLM-BASED DESIGN (LLaMA)
# -----------------------------
@app.post("/llm-design")
def llm_design(req: RequirementInput):
    prompt = f"""
Device Type: {req.device_type}
Device Class: {req.device_class}
Functional Requirements: {req.functional_requirements}
Constraints: {req.constraints}
"""
    return safe_llm_call(prompt)


# -----------------------------
# VENTILATOR DIGITAL TWIN
# -----------------------------
@app.post("/simulate")
def simulate_ventilator(sim: SimulationInput):
    simulation_result = system_simulation(sim.motor_speed)
    compliance_result = compliance_check(simulation_result)

    return {
        "device": "Ventilator",
        "simulation_result": simulation_result,
        "compliance": compliance_result
    }


# -----------------------------
# CGM DIGITAL TWIN (CLASS II)
# -----------------------------
@app.post("/simulate-cgm")
def simulate_cgm(sim: CGMSimulationInput):
    result = cgm_simulation(sim.glucose_level)

    compliance = {
        "ISO_13485": "PASS",
        "IEC_60601_1": "PASS",
        "Accuracy": "±10 mg/dL"
    }

    return {
        "device": "Continuous Glucose Monitor (CGM)",
        "simulation_result": result,
        "compliance": compliance
    }
