# PASSWORD GENERATOR

import random       # Import random module to generate random sequence
import string       # Import string to use predefined set

# Function to generate password
def password_generator():
    try:
        print("Welcome to Password Generator !")
        # Prompt to let user enter the length of letter
        length_letter = int(input("Enter the length of letter :"))
        # Prompt to let user enter the length of numbers
        length_numbers = int(input("Enter the length of numbers :"))
        # Prompt to let user enter the length of special characters
        length_special_character = int(input("Enter the length of special character :"))

        # Total length of password can't be zero 
        if length_letter + length_numbers + length_special_character == 0:
            print("Password length cannot be zero!")
            return 
        
        # Generates random non-repeating letter
        random_letter = random.sample(string.ascii_letters, k=length_letter)
        # Generates random non-repeating special characters
        random_special_character = random.sample(string.punctuation,k=length_special_character)
        # Generates random non-repeating numbers
        random_numbers = random.sample(string.digits,k=length_numbers)

        # Combination of all random letters , special caharacters and numbers
        password_generated = random_letter + random_numbers + random_special_character

        # Helps in shiffling all the random parts 
        random.shuffle(password_generated)

        # Create password from suffled list
        password = ''.join(password_generated)
        print(f"Password = {password}")

    except ValueError :
        print("Invalid value has been enetered")

password_generator()