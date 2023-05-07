# Simple Calculator #
# Create a Simple App Calculator
# 1. The application will ask the user to choose one of the four math operations (Addition, Subtraction, Multiplication and Division)
# 2. The application will ask the user for two numbers
# 3. Display the result
# 4. The application will ask if the user wants to try again or not.
# 5. If yes, repeat Step 1.
# 6. If no, Display “Thank you!” and the program will exit
# 7. Use Python Function and appropriate Exceptions to capture errors during runtime.
import time

def AnimatedSimpleCalculator():
    while True:
        # Use defined python functions and exceptions to fix errors
        try:
            # Ask user to use what arithmetic operation to use via input
            arithmetic_operation = str(input(
                "\nType the symbol of the arithmetic operation you would like to use\n( + , - , * , / )\n: "))
            if arithmetic_operation == '+':
                print("\nYou chose addition")
                operation='Addition'
            elif arithmetic_operation == '-':
                print("\nYou chose subtraction")
                operation='Subtraction'
            elif arithmetic_operation == '*':
                print("\nYou chose multiplication")
                operation='Multiplication'
            elif arithmetic_operation == '/':
                print("\nYou chose division")
                operation='Division'
            else:
                print("Invalid.\n")
                continue

            # Ask user to input two numbers to conduct the arithmetic operation
            firstN = float(input("\nWhat is your first number?\n"))
            secondN = float(input("\nWhat is your second number?\n"))

            # Computes the two numbers using the operation specified
            if arithmetic_operation == '+':
                result = firstN+secondN
            elif arithmetic_operation == '-':
                result = firstN-secondN
            elif arithmetic_operation == '*':
                result = firstN*secondN
            elif arithmetic_operation == '/':
                result = firstN/secondN

            print('\nOperation')
            time.sleep(1)
            print(f': {operation}')
            time.sleep(1.5)
            print(f"Numbers to be computed")
            time.sleep(1)
            print(f': {firstN, secondN}')
            animation='...'
            for i in range(len(animation)):
                print(animation[i], end='', flush=True)
                time.sleep(1.5)
            # Print the Result
            print(f"\n\nHere is your result\n:{result}")

            # Ask user whether to try again or not
            restart = str(
                input("\nWould you like to try again? (y or n only.)\n:"))
            while True:
                # End if no
                if restart.lower() == 'n':
                    return
                # Repeat if yes
                elif restart.lower() == 'y':
                    break
                else:
                    print("\nInvalid.\nTry again? (y/n)\n:")

        except ZeroDivisionError:
            print("Sorry! You can't divide by zero.")
        except ValueError:
            print("Sorry! Numbers only.")
        finally:
            # Displays 'Thank you!' whether if the user wants to exit or try again
            print("\nThank you!")

def SimpleCalculator():
    while True:
        # Use defined python functions and exceptions to fix errors
        try:
            # Ask user to use what arithmetic operation to use via input
            arithmetic_operation = str(input("\nType the symbol of the arithmetic operation you would like to use\n( + , - , * , / )\n: "))
            if arithmetic_operation == '+':
                print("\nYou chose addition")
                operation='Addition'
            elif arithmetic_operation == '-':
                print("\nYou chose subtraction")
                operation='Subtraction'
            elif arithmetic_operation == '*':
                print("\nYou chose multiplication")
                operation='Multiplication'
            elif arithmetic_operation == '/':
                print("\nYou chose division")
                operation='Division'
            else:
                print("Invalid.\n")
                continue

            # Ask user to input two numbers to conduct the arithmetic operation
            firstN = float(input("\nWhat is your first number?\n"))
            secondN = float(input("\nWhat is your second number?\n"))

            # Computes the two numbers using the operation specified
            if arithmetic_operation == '+':
                result = firstN+secondN
            elif arithmetic_operation == '-':
                result = firstN-secondN
            elif arithmetic_operation == '*':
                result = firstN*secondN
            elif arithmetic_operation == '/':
                result = firstN/secondN

            print('\nOperation')
            print(f': {operation}')
            print(f"Numbers to be computed")
            print(f': {firstN, secondN}')
            # Print the Result
            print(f"\n\nHere is your result\n:{result}")

            # Ask user whether to try again or not
            restart = str(
                input("\nWould you like to try again? (y or n only.)\n:"))
            while True:
                # End if no
                if restart.lower() == 'n':
                    return
                # Repeat if yes
                elif restart.lower() == 'y':
                    break
                else:
                    print("\nInvalid.\nTry again? (y/n)\n:")

        except ZeroDivisionError:
            print("Sorry! You can't divide by zero.")
        except ValueError:
            print("Sorry! Numbers only.")
        finally:
            # Displays 'Thank you!' whether if the user wants to exit or try again
            print("\nThank you!")
                  
while True:
    animated=str(input("Would you like to have animations? (y/n)\n: "))    
    if animated.lower()=='y':
        AnimatedSimpleCalculator()
        exit()
    elif animated.lower()=='n':
        SimpleCalculator()
        exit()
    else:
        print("Invalid.\n")

#HONTIVEROS JEROME ANDREI O.
#BSCPE 1-5