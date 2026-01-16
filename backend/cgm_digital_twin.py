"""
cgm_digital_twin.py
----------------------------------
Digital Twin Simulation Engine
Device: Continuous Glucose Monitor (Class II)

Simulates:
- Glucose sensing
- ADC conversion
- Basic alert logic
"""

import random


# -----------------------------
# SENSOR MODEL
# -----------------------------
def glucose_sensor_model(actual_glucose: float):
    """
    Adds realistic sensor noise (±5 mg/dL)
    """
    noise = random.uniform(-5, 5)
    sensed_glucose = actual_glucose + noise
    return sensed_glucose


# -----------------------------
# ADC MODEL
# -----------------------------
def adc_conversion(sensor_value: float):
    """
    Converts glucose value to 12-bit ADC output
    """
    ADC_RESOLUTION = 4096  # 12-bit
    MAX_GLUCOSE = 400      # mg/dL

    adc_value = int((sensor_value / MAX_GLUCOSE) * ADC_RESOLUTION)
    return max(0, min(adc_value, ADC_RESOLUTION - 1))


# -----------------------------
# CGM DIGITAL TWIN
# -----------------------------
def cgm_simulation(glucose_level: float):
    """
    Complete CGM simulation
    """
    sensor_reading = glucose_sensor_model(glucose_level)
    adc_value = adc_conversion(sensor_reading)

    # Alert logic
    if sensor_reading < 70:
        alert = "HYPOGLYCEMIA"
    elif sensor_reading > 180:
        alert = "HYPERGLYCEMIA"
    else:
        alert = "NORMAL"

    return {
        "actual_glucose_mg_dl": round(glucose_level, 2),
        "sensor_reading": round(sensor_reading, 2),
        "adc_value": adc_value,
        "alert_status": alert
    }
