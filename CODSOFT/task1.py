# Calculator to perform basic operation 

# Function to display menu of calculator
def menu():
    print("Choose the Operation from following : ")
    print("1. Addition")        # Option for Addition
    print("2. Subtraction")     # Option for Subtraction
    print("3. Multiplication")  # Option for Multiplication
    print("4. Division")        # Option for Division
    print("5. Modulus")         # Option for Modulus
    print("6. Exponent")        # Option for Exponent
    print("7. Exit \n")         # Option for Exit


# Function to perform basic operation
def operation(choice,number1,number2):
    try:
        if choice == '1':
            # Perform Addition
            return(f"Addition of {number1} + {number2} = {number1 + number2}\n")
        elif choice == '2':
            # Perform Subtraction
            return(f"Subtraction of {number1} - {number2} = {number1 - number2}\n")
        elif choice == '3':
            # Perform Multiplication 
            return(f"Multiplication of {number1} x {number2} = {number1 * number2}\n")
        elif choice == '4':
            # Perform Division
            if number2 == 0:
                raise ZeroDivisionError("Can't Divide by Zero")
            return(f"Division of {number1} / {number2} = {number1 / number2}\n")
        elif choice == '5':
            # Perform Modulus
            return(f"Modulus of {number1} % {number2} = {number1 % number2}\n")
        elif choice == '6':
            # Perform Exponentiation
            return(f"Exponent of {number1} ** {number2} = {number1 ** number2}\n")
    except ValueError as e:
            return("Invalid Values")
    except ZeroDivisionError as e:
            return(str(e))
  

# Main Execution
if __name__ == "__main__" :
    while True:
        menu()      # Display the menu
        try: 
            # Prompt user to enter the choice
            choice = input("Enter the operation you want to perform from (1-7) : ")
            if choice in ['1','2','3','4','5','6','7']:
                if choice == '7':
                    print("Exiting calculator.")
                    print("Thank you.")
                    break   # Exit calculator
                else:
                    # Prompt for two numbers
                    number1 = float(input("Enter the first number : "))
                    number2 = float(input("Enter the second number : "))
                    #Perform choosen operation
                    print(operation(choice,number1,number2))
            else:
                print("Invalid Choice. Please choose from (1-7)")
        except ValueError as e:
            print("Invalid Value.(Only accept Integer value)")
