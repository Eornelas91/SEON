import re

# Token force map (expandable)
MORAL_TOKENS = {
    "betray":     {"sW": 0.9, "G": 0.9, "R": -0.9},
    "protect":    {"sW": 0.4, "G": 0.7, "R": +0.6},
    "kill":       {"sW": 1.0, "G": 1.0, "R": -1.0},
    "steal":      {"sW": 0.8, "G": 0.7, "R": -0.8},
    "lie":        {"sW": 0.7, "G": 0.6, "R": -0.6},
    "truth":      {"sW": 0.3, "G": 0.9, "R": +0.8},
    "sacrifice":  {"sW": 0.85,"G": 1.0, "R": +1.0},
    "hurt":       {"sW": 0.9, "G": 0.8, "R": -0.7},
    "child":      {"sW": 0.6, "G": 0.6, "R": +0.7},
    "innocent":   {"sW": 0.8, "G": 0.8, "R": +0.9},
    "revenge":    {"sW": 0.75,"G": 0.8, "R": -0.6},
    "mercy":      {"sW": 0.5, "G": 0.8, "R": +0.9}
}

def normalize(word: str) -> str:
    """
    Soft stemmer for common suffixes: handles past tense, plurals, etc.
    """
    if word.endswith("ied"):
        return word[:-3] + "y"
    elif word.endswith("ed"):
        return word[:-2]
    elif word.endswith("ing"):
        return word[:-3]
    elif word.endswith("s"):
        return word[:-1]
    return word


def analyze_effection(text: str) -> dict:
    """
    Analyze text for semantic and moral gravity features.
    Returns:
        sW - semantic Weight coefficient
        G  - intentional gravitas
        R  - resonance amplitude
        tokens - matched moral tokens and their weights
    """
    text = text.lower()
    total_sW = total_G = total_R = 0
    matched_tokens = []
    
    words_in_text = re.findall(r'\b\w+\b', text)
    
    for token in words_in_text:
        base = normalize(token)
        if base in MORAL_TOKENS:
            values = MORAL_TOKENS[base]
            matched_tokens.append({base: values})
            total_sW += values["sW"]
            total_G  += values["G"]
            total_R  += values["R"]

    
    count = len(matched_tokens)
    if count == 0:
        return {
            "sW": 1.0,
            "intentional_gravitas": 0.5,
            "resonance_amplitude": 0.0,
            "tokens": []
        }
    
    return {
        "sW": round(total_sW / count, 4),
        "intentional_gravitas": round(total_G / count, 4),
        "resonance_amplitude": round(total_R / count, 4),
        "tokens": matched_tokens
    }

if __name__ == "__main__":
    example = "I betrayed him to protect my family."
    result = analyze_effection(example)
    print(f"Effection Analysis for: '{example}'")
    print(result)
