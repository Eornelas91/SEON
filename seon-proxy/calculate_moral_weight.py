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
