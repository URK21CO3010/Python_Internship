import random
import string

def generate_password(length) -> str:

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    
    # Ensure the password contains at least one character from each set
    all_characters = lower + upper + digits + special
    
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the remaining password with random characters
    password += random.choices(population = all_characters, k = length - 4)
    
    # Shuffle the list
    random.shuffle(password)
    
    return ''.join(password)

def generate_passwords(length: int, count: int) -> list:
    
    return [generate_password(length) for _ in range(count)]

def main():
    try:
        length = int(input("Enter password length (minimum length is 12): "))

        if length < 12:
            print("Error: Password length should be at least 12 characters.")
            return

        count = int(input("Enter number of passwords to generate: "))
        
        passwords = generate_passwords(length, count)
        
        print("\nGenerated Passwords:")
        for i, password in enumerate(passwords, 1):
            print(f"{i}: {password}")
            
    except ValueError:
        print("Invalid input. Please enter numeric values for length and count.")

if __name__ == "__main__":
    main()
