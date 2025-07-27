from effection_parser import analyze_effection
from soen_mgp_core import calculate_moral_weight

def process_moral_statement(text: str, overrides: dict = None) -> dict:
    """
    Full pipeline: natural language → semantic analysis → moral weight calculation.
    Allows optional overrides for any MGP variable.
    """
    effection = analyze_effection(text)

    # Default MGP variables (can be overridden)
    defaults = {
        "P": 0.9,  # Presence
        "R": effection["resonance_amplitude"],
        "I": effection["intentional_gravitas"],
        "kappa": 1,  # Collapse direction
        "T": 0.9,  # Truth proximity
        "delta_t": 1,  # Time elapsed
        "S": 0.2,  # Self-deception
        "L": 0.5,  # Law alignment
        "G": 0.3,  # Regret
        "sW": effection["sW"]
    }

    # Allow runtime overrides
    if overrides:
        defaults.update(overrides)

    # Calculate MW
    result = calculate_moral_weight(**defaults)

    return {
        "input": text,
        "tokens": effection["tokens"],
        "parameters": defaults,
        "moral_weight_result": result
    }

# Optional test
if __name__ == "__main__":
    sample = "I betrayed him to protect my family."
    output = process_moral_statement(sample)
    print("🧠 Seon Moral Analysis:")
    for k, v in output.items():
        print(f"{k}: {v}")
