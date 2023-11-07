import random

# Define the fixed filename
filename = "SavedPasswords.txt"

# Function to generate a strong, randomized password
def generate_password(length, use_lowercase, use_uppercase, use_numbers, use_special_chars):
    characters = ''
    if use_lowercase:
        characters += 'abcdefghijklmnopqrstuvwxyz'
    if use_uppercase:
        characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if use_numbers:
        characters += '0123456789'
    if use_special_chars:
        characters += '!@#$%^&*()_+[]{}|;:,.<>?'

    if not characters:
        return "Cannot generate a password with no character set selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to generate and save passwords to the file
def generate_and_save_passwords(num_passwords, password_length, complexity_options):
    with open(filename, 'a') as file:  # Use 'a' (append) mode to add passwords to the file
        for _ in range(num_passwords):
            password = generate_password(password_length, *complexity_options)
            file.write(password + '\n')

# Function to read and analyze passwords from the file
def read_and_analyze_passwords():
    with open(filename, 'r') as file:
        passwords = [line.strip() for line in file.readlines()]

    if not passwords:
        print("No passwords found in the file.")
        return

    # Find the longest and shortest passwords
    shortest_password = min(passwords, key=len)
    longest_password = max(passwords, key=len)

    print(f"Shortest Password: {shortest_password} (Length: {len(shortest_password)})")
    print(f"Longest Password: {longest_password} (Length: {len(longest_password)})")

# Function to assess password strength
def assess_password_strength(password):
    if len(password) < 8:
        return "Weak"
    elif len(password) < 12:
        return "Moderate"
    else:
        return "Strong"

# Function to generate a report with password statistics
def generate_password_report():
    with open(filename, 'r') as file:
        passwords = [line.strip() for line in file.readlines()]

    num_passwords = len(passwords)
    total_length = sum(len(password) for password in passwords)

    strength_categories = {"Weak": 0, "Moderate": 0, "Strong": 0}

    for password in passwords:
        strength = assess_password_strength(password)
        strength_categories[strength] += 1

    average_length = total_length / num_passwords

    print(f"Number of Passwords: {num_passwords}")
    print(f"Average Password Length: {average_length:.2f}")
    print("Password Strength Categories:")
    for category, count in strength_categories.items():
        print(f"{category}: {count}")

if __name__ == "__main__":
    # User input for password generation and analysis
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the desired password length: "))
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    complexity_options = [use_lowercase, use_uppercase, use_numbers, use_special_chars]

    generate_and_save_passwords(num_passwords, password_length, complexity_options)
    print(f"Passwords saved to {filename}")

    read_and_analyze_passwords()

    generate_password_report()
