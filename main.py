import re

def password_strength(password):
    min_length = 8
    max_length = 20
    complexity_requirements = {
        'lowercase': re.compile(r'[a-z]'),
        'uppercase': re.compile(r'[A-Z]'),
        'digit': re.compile(r'\d'),
        'special': re.compile(r'[!@#$%^&*(),.?":{}|<>]')
    }
    
    strength = {
        'length': False,
        'complexity': False,
        'uniqueness': False
    }
    
    if min_length <= len(password) <= max_length:
        strength['length'] = True
    
    complexity_score = sum(1 for requirement in complexity_requirements.values() if requirement.search(password))
    if complexity_score >= 3:  
        strength['complexity'] = True
    
    common_patterns = [
        re.compile(r'1234'), re.compile(r'password'), re.compile(r'qwerty')
    ]
    if not any(pattern.search(password) for pattern in common_patterns):
        strength['uniqueness'] = True

    feedback = []
    if not strength['length']:
        feedback.append(f"Password must be between {min_length} and {max_length} characters long.")
    if not strength['complexity']:
        feedback.append("Password must include at least three of the following: lowercase letters, uppercase letters, digits, special characters.")
    if not strength['uniqueness']:
        feedback.append("Password should avoid common patterns or easily guessable sequences.")
    
    if all(strength.values()):
        feedback.append("Password is strong!")
    
    return strength, feedback

# Example usage
password = input("Enter a password to check: ")
strength, feedback = password_strength(password)

print("Strength Assessment:")
print(f"Length requirement met: {strength['length']}")
print(f"Complexity requirement met: {strength['complexity']}")
print(f"Uniqueness requirement met: {strength['uniqueness']}")
print("\nFeedback:")
for line in feedback:
    print(line)
