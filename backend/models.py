from pydantic import BaseModel, Field
from typing import List, Dict, Optional


# -----------------------------
# REQUIREMENT INPUT MODEL
# -----------------------------
class RequirementInput(BaseModel):
    device_type: str = Field(
        example="Ventilator",
        description="Type of medical device"
    )
    device_class: str = Field(
        example="Class III",
        description="Medical device class"
    )
    functional_requirements: List[str] = Field(
        example=[
            "Deliver controlled airflow",
            "Maintain airway pressure",
            "Trigger alarms on failure"
        ],
        description="List of functional requirements"
    )
    constraints: Dict[str, str] = Field(
        example={
            "power": "Battery + AC",
            "standard": "ISO 60601-1"
        },
        description="Design constraints"
    )


# -----------------------------
# SYSTEM ARCHITECTURE MODEL
# -----------------------------
class SystemArchitecture(BaseModel):
    components: Dict[str, str] = Field(
        example={
            "MCU": "STM32",
            "Pressure Sensor": "MPX5010",
            "Motor": "BLDC Motor"
        }
    )
    interfaces: List[str] = Field(
        example=["I2C", "ADC", "PWM", "GPIO"]
    )


# -----------------------------
# VENTILATOR SIMULATION INPUT
# -----------------------------
class SimulationInput(BaseModel):
    motor_speed: float = Field(
        example=150,
        description="Motor speed for airflow simulation"
    )


# -----------------------------
# CGM SIMULATION INPUT
# -----------------------------
class CGMSimulationInput(BaseModel):
    glucose_level: float = Field(
        example=140,
        description="Blood glucose level in mg/dL"
    )


# -----------------------------
# DIGITAL TWIN OUTPUT MODELS
# -----------------------------
class VentilatorSimulationResult(BaseModel):
    airflow_lpm: float
    pressure_cmH2O: float
    motor_current_A: float
    power_W: float
    alarm_status: str


class CGMSimulationResult(BaseModel):
    actual_glucose_mg_dl: float
    sensor_reading: float
    adc_value: int
    alert_status: str
