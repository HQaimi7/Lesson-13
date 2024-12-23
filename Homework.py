import random

def generate_password(length=12):
    # Define the character sets manually
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special_char = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

    # Combine all characters to form a pool
    all_characters = lower_case + upper_case + digits + special_char

    # Generate a random password by selecting random characters from the pool
    password = random.choices(all_characters, k=length)

    # Shuffle the generated password to ensure randomness
    random.shuffle(password)

    # Join the list into a single string to return
    return "".join(password)

# Generate a random password of length 12
password = generate_password(12)

# Output the generated password
print("Generated Password:")
print(password, "\n")
