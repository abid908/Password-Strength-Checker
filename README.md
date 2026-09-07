# Python Password Checker

A simple and effective Python script to evaluate the strength and security of a password.

## Features
* **Entropy Calculation:** Calculates the mathematical entropy of the password based on character pool size (lowercase, uppercase, digits, and special characters).
* **Rule-Based Scoring:** Awards points for combining different types of characters[cite: 1].
* **Length Bonus:** Gives extra points if the password length is 8 or 12+ characters[cite: 1].
* **Common Password Check:** Instantly flags known weak passwords (e.g., "admin", "123456", "password", "iloveyou") by checking against a built-in common password list[cite: 1].
* **Final Verdict:** Categorizes the password as "Weak", "Moderate", "Strong", or "Very Strong" and provides a score out of 100[cite: 1].

## How to Run
1. Make sure you have Python installed on your system.
2. Download or clone this repository.
3. Run the following command in your terminal:
   ```bash
   python "password checker.py"
