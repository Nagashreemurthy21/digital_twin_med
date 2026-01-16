"""
genai_engine.py
----------------------------------
Requirement → System Architecture Generator

This module represents the GenAI layer.
Currently implemented as a deterministic
architecture generator (exam & demo safe).
Can be replaced with LLaMA / RAG later.
"""

def generate_architecture(requirements):
    device_type = requirements.device_type.lower()

    # -----------------------------
    # VENTILATOR (CLASS III)
    # -----------------------------
    if "ventilator" in device_type:
        components = {
            "MCU": "STM32F4",
            "Pressure Sensor": "MPX5010",
            "Flow Sensor": "YF-S201",
            "Blower Motor": "BLDC Motor",
            "Valve": "Solenoid Valve",
            "Alarm": "Buzzer + LED",
            "Display": "LCD",
            "Power": "Battery + SMPS"
        }

        interfaces = [
            "I2C (Sensors)",
            "ADC (Pressure)",
            "PWM (Motor Control)",
            "GPIO (Alarm, Valve)",
            "UART (Display)"
        ]

    # -----------------------------
    # CGM (CLASS II)
    # -----------------------------
    elif "glucose" in device_type or "cgm" in device_type:
        components = {
            "MCU": "nRF52832",
            "Glucose Sensor": "Electrochemical Sensor",
            "ADC": "12-bit ADC",
            "BLE Module": "Bluetooth Low Energy",
            "Battery": "Coin Cell",
            "Mobile App": "Android / iOS"
        }

        interfaces = [
            "ADC (Sensor Input)",
            "SPI (ADC)",
            "BLE (Wireless)",
            "GPIO (Status LED)"
        ]

    # -----------------------------
    # DEFAULT (GENERIC DEVICE)
    # -----------------------------
    else:
        components = {
            "MCU": "Generic MCU",
            "Sensor": "Generic Sensor",
            "Actuator": "Generic Actuator",
            "Power": "DC Supply"
        }

        interfaces = [
            "I2C",
            "SPI",
            "GPIO"
        ]

    return {
        "components": components,
        "interfaces": interfaces,
        "design_status": "Generated successfully"
    }
