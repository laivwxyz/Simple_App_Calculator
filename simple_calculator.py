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
            choose = int(input("Enter your choice (1-4): "))

            # Check if the choice is valid
            if choose not in [1, 2, 3, 4]:
                raise ValueError("Invalid choice")

            # Ask the user for two numbers
            num_1 = float(input("Enter first number: "))
            num_2 = float(input("Enter second number: "))

            # Perform the chosen operation and display the result
            # if the user choose addition,
            if choose == 1:
                result = num_1 + num_2
                print(f"{num_1} + {num_2} = {result}")
            # if the user choose subtraction,
            elif choose == 2:
                result = num_1 - num_2
                print(f"{num_1} - {num_2} = {result}")
            # if the user choose multiplication,
            elif choose == 3:
                result = num_1 * num_2
                print(f"{num_1} * {num_2} = {result}")
            # if the user choose division,
            elif choose == 4:
                if num_2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                result = num_1 / num_2
                print(f"{num_1} / {num_2} = {result}")

            # Ask the user if they want to try again
            try_again = input("Do you want to try again? (y/n): ")
            if try_again.lower() != "y":
                print("Thank you!")
                break
                          
    # If the user enters an invalid input, a ValueError is raised.  
    except ValueError as error:
        # Log the error
        print(f"Error: {error}")
        print("Please enter a valid choice (1-4)")
        calculator()
        
    # If the user chooses division and enters a second number of zero, a ZeroDivisionError is raised.      
    except ZeroDivisionError as error:
        # Log the error
        print(f"Error: {error}")
        print("Please enter a non-zero second number")
        calculator()

    # If any other error occurs, an Exception is raised.    
    except Exception as error:
        # Log any other errors
        print(f"Error: {error}")         
   
calculator()