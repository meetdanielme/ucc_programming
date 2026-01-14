def computegrade(score):
    if score < 0.0 or score > 1.0:
        return "This score is invalid"
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"

score = float(input("Enter score: "))
print(computegrade(score))