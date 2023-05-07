# Dela Cruz, Lailanie E. _ BSCPE 1-4
# Assignment 5
# Programming Exercise

# CREATING SIMPLE APP CALCULATOR
def calculator():
    try:
        while True:
            # Ask the user to choose a math operation
            print("Choose a math operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            choice = int(input("Enter your choice (1-4): "))

            # Check if the choice is valid
            if choice not in [1, 2, 3, 4]:
                raise ValueError("Invalid choice")

            # Ask the user for two numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform the chosen operation and display the result
            # if the user choose addition,
            if choice == 1:
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
                
# Ask the user if they want to try again
# If the user enters an invalid input, a ValueError is raised.           
# If the user chooses division and enters a second number of zero, a ZeroDivisionError is raised.     
# If any other error occurs, an Exception is raised.

calculator()