"""
digital_twin.py
----------------------------------
Digital Twin Simulation Engine
Device: Ventilator (Class III)

Simulates:
- Mechanical airflow
- Airway pressure
- Electrical behavior
- Alarm logic
"""

# -----------------------------
# MECHANICAL SIMULATION
# -----------------------------
def airflow_simulation(motor_speed: float):
    """
    motor_speed: RPM equivalent control value
    returns airflow (L/min) and pressure (cmH2O)
    """
    airflow_lpm = 0.08 * motor_speed
    pressure_cmH2O = airflow_lpm * 1.2

    return airflow_lpm, pressure_cmH2O


# -----------------------------
# ELECTRICAL SIMULATION
# -----------------------------
def electrical_simulation(motor_speed: float):
    """
    Simulates motor current & power
    """
    voltage = 12.0  # volts
    current = 0.02 * motor_speed
    power = voltage * current

    return current, power


# -----------------------------
# CONTROL & SAFETY LOGIC
# -----------------------------
def control_logic(pressure: float):
    """
    Pressure safety checks
    """
    MIN_PRESSURE = 5
    MAX_PRESSURE = 20

    if pressure < MIN_PRESSURE:
        return "LOW_PRESSURE_ALARM"
    elif pressure > MAX_PRESSURE:
        return "OVER_PRESSURE_ALARM"
    else:
        return "NORMAL"


# -----------------------------
# COMPLETE SYSTEM SIMULATION
# -----------------------------
def system_simulation(motor_speed: float):
    """
    Full Digital Twin execution
    """
    airflow, pressure = airflow_simulation(motor_speed)
    current, power = electrical_simulation(motor_speed)
    alarm_status = control_logic(pressure)

    return {
        "airflow_lpm": round(airflow, 2),
        "pressure_cmH2O": round(pressure, 2),
        "motor_current_A": round(current, 2),
        "power_W": round(power, 2),
        "alarm_status": alarm_status
    }
