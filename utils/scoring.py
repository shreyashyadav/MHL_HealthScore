def calculate_bmi(weight, height):
    if height > 0:
        return weight / (height ** 2)
    return 0

def calculate_score(data):
    score = 0
    # Demographic Information
    score += int(data.get('age', 0))
    score += int(data.get('sex', 0))
    score += int(data.get('region_a', 0))
    score += int(data.get('region_b', 0))

    # Physical Measurements
    bmi = float(data.get('bmi', 0))
    print("bmi :",bmi)
    if bmi < 18.5 or (bmi >= 25 and bmi < 30):
        score += 2
    elif bmi >= 30:
        score += 3
    else:
        score += 1

    #score += int(data.get('bmi', 0))

    # Medical History
    score += int(data.get('chronic_conditions', 0))
    score += int(data.get('family_history', 0))
    score += int(data.get('surgeries', 0))
    score += int(data.get('hospitalizations', 0))
    score += int(data.get('medications', 0))

    # Lifestyle Factors
    score += int(data.get('smoking', 0))
    score += int(data.get('alcohol', 0))
    score += int(data.get('exercise', 0))
    score += int(data.get('diet', 0))
    score += int(data.get('sleep', 0))
    score += int(data.get('stress', 0))
    score += int(data.get('substance_use', 0))

    # Current Health Status
    score += int(data.get('symptoms', 0))
    score += int(data.get('recent_illnesses', 0))
    return score

def get_recommendation(score):
    if score <= 20:
        return "Low Risk: Basic tests (CBC, BMP, Lipid profile)"
    elif score <= 40:
        return "Moderate Risk: Additional tests (Liver function tests, Kidney function tests, HbA1c)"
    else:
        return "High Risk: Comprehensive tests (Complete metabolic panel, Cardiac markers, Advanced imaging if necessary)"
