import random
import string

def generate_strong_password(length=16):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters for strong security.")

    # Define character pools
    lower = string.ascii_lowercase  # a-z
    upper = string.ascii_uppercase  # A-Z
    digits = string.digits          # 0-9
    special = string.punctuation    # Special characters like !@#$%^&*

    # Ensure the password contains at least one character from each pool
    all_characters = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random characters from all pools
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    # Return the password as a string
    return ''.join(password)

# Generate a strong password of desired length
password = generate_strong_password(16)  # You can change the length here
print("Generated Strong Password:", password)