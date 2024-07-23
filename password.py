import string
import random

def generate_password(length):
    if length < 1:
        return "Password length must be at least 1."
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 1:
                print("Password length must be at least 1.")
                continue
            password = generate_password(length)
            print(f"Generated password: {password}")
            
            another = input("Do you want to generate another password? (yes/no): ").lower()
            if another != 'yes':
                print("Thank you for using the Random Password Generator. Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the password generator
main()
