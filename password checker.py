import math
import re
COMMON_PASSWORDS = ["admin", "password", "123456", "12345678", "qwerty", "abcd", "letmein", "monkey", "dragon", "111111", "baseball", "iloveyou", "trustno1", "sunshine", "master", "welcome", "shadow", "ashley", "football", "jesus", "michael"]

def calculate_entropy(password):
    pool_size = 0
    #for lower case letters, +26
    if re.search(r'[a-z]', password):
        pool_size += 26
    #for uppercase letters, +26
    if re.search(r'[A-Z]', password):
        pool_size += 26
    #for digits, +10
    if re.search(r'[0-9]', password):
        pool_size += 10
    #for special characters, +32
    if re.search(r'[^a-zA-Z0-9]', password):
        pool_size += 32 
    
    if pool_size == 0:
        return 0
    entropy = len(password) * math.log2(pool_size)
    return round(entropy, 2)

def score_password(password):

    length = len(password)
    entropy = calculate_entropy(password)
    score = 0
    #Rule Based Scoring
    if re.search(r'[a-z]', password):
        score += 10
    if re.search(r'[A-Z]', password):
        score += 10
    if re.search(r'[0-9]', password):
        score += 10
    if re.search(r'[^a-zA-Z0-9]', password):
        score += 10
    if length >= 8:
        score += 10
    if length >= 12:
        score += 20
    final_score = min(100, score + int(entropy))
    if password.lower() in COMMON_PASSWORDS:
        final_score = 0
    if final_score < 40:
        verdict = "Weak"
    elif final_score < 60:
        verdict = "Moderate"
    elif final_score < 80:
        verdict = "Strong"
    else:
        verdict = "Very Strong"
        
    return length, entropy, final_score, verdict

if __name__ == "__main__":
    print("--- Python Password Checker ---")
    
    user_password = input("Enter a password to test: ")
    
    length, entropy, final_score, verdict = score_password(user_password)
#Result Display    
    print("\n--- Password Analysis ---")
    print(f"Length: {length}")
    print(f"Entropy: {entropy}")
    print(f"Score: {final_score}/100")
    print(f"Verdict: {verdict}")