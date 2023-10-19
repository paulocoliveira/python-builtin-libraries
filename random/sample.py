import random
import string

# Define function to generate random username
def generate_random_username(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Define function to generate random password
def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Generate random username and password
random_username = generate_random_username()
random_password = generate_random_password()

# Print generated credentials
print(f"Generated Username: {random_username}")
print(f"Generated Password: {random_password}")
