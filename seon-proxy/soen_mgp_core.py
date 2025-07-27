print("✔️ Loaded soen_mgp_core.py with sW support.")

def calculate_moral_weight(P, R, I, kappa, T, delta_t, S, L, G, sW=1.0):
    """
    Computes Moral Weight (MW) based on GST + Effection-modified formula.
    sW = semantic Weight coefficient
    """
    try:
        base = (P * R * I * kappa * T * (1 + delta_t))
        law_component = (L * kappa)
        regret_component = (G * delta_t)
        mw_raw = base - S + law_component + regret_component
        MW = sW * mw_raw
        return {
            "moral_weight": round(MW, 4),
            "collapse_vector": kappa,
            "sW": round(sW, 4),
            "explanation": f"MW: {round(MW, 4)} from sW:{sW}, P:{P}, R:{R}, I:{I}, κ:{kappa}, T:{T}, Δt:{delta_t}, S:{S}, L:{L}, G:{G}"
        }
    except Exception as e:
        return {"error": f"Calculation error: {e}"}

if __name__ == "__main__":
    print("Using MGP Function from this file.")
    print(__file__)

    # Sample inputs — adjust as needed
    P = 0.9      # Presence
    R = 0.8      # Resonance
    I = 1.0      # Intent clarity
    kappa = 1    # Collapse vector (+1 = convergence)
    T = 0.95     # Truth proximity
    delta_t = 2  # Time elapsed
    S = 0.1      # Self-deception
    L = 0.7      # Law alignment
    G = 0.4      # Regret

    result = calculate_moral_weight(P, R, I, kappa, T, delta_t, S, L, G)

    print("🧮 Seon MGP Output:")
    for key, value in result.items():
        print(f"{key}: {value}")

