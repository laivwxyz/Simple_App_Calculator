# Dela Cruz, Lailanie E. _ BSCPE 1-4
# Assignment 5
# Programming Exercise

# Adding a design in the program 
from termcolor import colored
from pyfiglet import Figlet

f = Figlet(font = 'isometric3', width = 240)
print(colored(f.renderText('CALCULATOR'), 'cyan'))
print(colored('=' * 140, 'cyan'))
f = Figlet(font = 'serifcap',  width = 240)
print(colored(f.renderText('   Choose one math operation'), 'light_green'))
f = Figlet(font = 'serifcap', justify= "center")
print(colored(f.renderText('              + - x /'),'light_green'))

# ---
def calculator():
    try:
        while True:
            # Ask the user to choose a math operation
            print("\033[96mChoose a math operation:")
            print("\033[0m 1. Addition")
            print("\033[0m 2. Subtraction")
            print("\033[0m 3. Multiplication")
            print("\033[0m 4. Division")
            choose = int(input("\033[92mEnter your choice (1-4):\033[0m "))

            # Check if the choice is valid
            if choose not in [1, 2, 3, 4]:
                raise ValueError("Invalid choice")

            # Ask the user for two numbers
            num_1 = float(input("\033[92mEnter first number:\033[0m "))
            num_2 = float(input("\033[92mEnter second number:\033[0m "))

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
            try_again = input("\033[92mDo you want to try again? (y/n):\033[0m ")
            if try_again.lower() != "y":
                print("\033[96mThank you!")
                print(colored('=' * 140, 'cyan'))
                break
                          
    # If the user enters an invalid input, a ValueError is raised.  
    except ValueError as error:
        # Log the error
        print(f"\033[91mError: \033[0m{error}")
        print("\033[91mPlease enter a valid choice (1-4)")
        calculator()
        
    # If the user chooses division and enters a second number of zero, a ZeroDivisionError is raised.      
    except ZeroDivisionError as error:
        # Log the error
        print(f"\033[91mError: \033[0m{error}")
        print("\033[91mPlease enter a non-zero second number")
        calculator()

    # If any other error occurs, an Exception is raised.    
    except Exception as error:
        # Log any other errors
        print(f"\033[91mError: \033[0m{error}")         
   
calculator()