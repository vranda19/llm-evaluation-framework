def evaluate_response(response):
    score = 0
    
    if "earth" in response.lower():
        score += 1
    if "sun" in response.lower():
        score += 1
    if len(response.split()) > 5:
        score += 1

    return score

response = "The Earth revolves around the Sun in an orbit."
print("Score:", evaluate_response(response))
