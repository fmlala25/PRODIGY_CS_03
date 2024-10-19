import re

def assess_password_strength(password):
    """
    Assess the strength of a password based on length, use of uppercase and lowercase letters,
    numbers, and special characters.
    """
    # Initialize strength score
    score = 0
    feedback = []

    # Criteria 1: Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Criteria 2: Uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Criteria 3: Lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Criteria 4: Numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Criteria 5: Special characters
    if re.search(r'[@$!%*?&#]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character (e.g., @$!%*?&#).")

    # Provide feedback based on score
    if score == 5:
        return "Password is strong."
    elif score >= 3:
        feedback.append("Password strength: Medium.")
        return " ".join(feedback)
    else:
        feedback.append("Password strength: Weak.")
        return " ".join(feedback)

# Example usage
password = input("Enter your password: ")
result = assess_password_strength(password)
print(result)
