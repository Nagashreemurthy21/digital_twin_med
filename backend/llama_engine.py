"""
llama_engine.py
----------------------------------
LLM-based System Design Generator
Uses TinyLLaMA (CPU-friendly)

Can be upgraded to LLaMA-2 / LLaMA-3
by changing MODEL_NAME.
"""

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import json
import re

# -----------------------------
# MODEL CONFIGURATION
# -----------------------------
MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float32,
    device_map="cpu"
)

model.eval()


# -----------------------------
# PROMPT TEMPLATE
# -----------------------------
def build_prompt(requirements_text: str):
    return f"""
You are a medical device system architect.

Based on the following requirements, generate a system design
with components and interfaces.

Requirements:
{requirements_text}

Respond ONLY in valid JSON format like this:
{{
  "components": {{
    "MCU": "example",
    "Sensor": "example"
  }},
  "interfaces": ["I2C", "ADC", "PWM"]
}}
"""


# -----------------------------
# JSON EXTRACTION UTILITY
# -----------------------------
def extract_json(text: str):
    """
    Extract JSON block from LLM output
    """
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass

    # fallback if parsing fails
    return {
        "components": {
            "MCU": "Generic MCU",
            "Sensor": "Generic Sensor",
            "Actuator": "Generic Actuator"
        },
        "interfaces": ["I2C", "GPIO"],
        "note": "Fallback design used (JSON parse failed)"
    }


# -----------------------------
# MAIN LLM FUNCTION
# -----------------------------
def llama_generate_architecture(requirements_text: str):
    prompt = build_prompt(requirements_text)

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=1024
    )

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=300,
            temperature=0.7,
            do_sample=True,
            top_p=0.9
        )

    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Extract and return structured JSON
    architecture = extract_json(decoded)
    return architecture
