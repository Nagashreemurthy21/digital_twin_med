"""
compliance.py
----------------------------------
Medical Device Compliance & Risk Validation Engine

Standards covered:
- ISO 60601-1 : Electrical Safety
- ISO 14971   : Risk Management
"""

# -----------------------------
# COMPLIANCE CHECK FUNCTION
# -----------------------------
def compliance_check(simulation_result: dict):
    risks = []

    # -----------------------------
    # ISO 60601-1 : Electrical Safety
    # -----------------------------
    motor_current = simulation_result.get("motor_current_A", 0)

    if motor_current <= 2.0:
        electrical_status = "PASS"
    else:
        electrical_status = "FAIL"
        risks.append({
            "hazard": "Overcurrent",
            "severity": "High",
            "standard": "ISO 60601-1",
            "mitigation": "Current limiting & fuse"
        })

    # -----------------------------
    # ISO 14971 : Risk Management
    # -----------------------------
    pressure = simulation_result.get("pressure_cmH2O", 0)

    if pressure > 20:
        risks.append({
            "hazard": "Overpressure",
            "severity": "High",
            "standard": "ISO 14971",
            "mitigation": "Pressure relief valve & alarm"
        })

    if pressure < 5:
        risks.append({
            "hazard": "Underpressure",
            "severity": "Medium",
            "standard": "ISO 14971",
            "mitigation": "Closed-loop motor control"
        })

    # -----------------------------
    # FINAL COMPLIANCE REPORT
    # -----------------------------
    return {
        "ISO_60601_1": electrical_status,
        "ISO_14971_risks": risks,
        "overall_status": "PASS" if electrical_status == "PASS" and not risks else "REVIEW_REQUIRED"
    }
