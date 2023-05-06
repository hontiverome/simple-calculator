# Simple Calculator #
# Create a Simple App Calculator
# 1. The application will ask the user to choose one of the four math operations (Addition, Subtraction, Multiplication and Division)
# 2. The application will ask the user for two numbers
# 3. Display the result
# 4. The application will ask if the user wants to try again or not.
# 5. If yes, repeat Step 1.
# 6. If no, Display “Thank you!” and the program will exit 
# 7. Use Python Function and appropriate Exceptions to capture errors during runtime.

# Ask user to use what arithmetic operation to use via input
def SimpleCalculator():
    while True:
        # Use defined python functions and exceptions to fix errors
        try:
            # Ask user to input two numbers to conduct the arithmetic operation
            arithmetic_operation=str(input("\nType the symbol of the arithmetic operation you would like to use\n( + , - , * , / )\n: "))
            if arithmetic_operation=='+':
                print("You chose addition")
            elif arithmetic_operation=='-':
                print("You chose subtraction")
            elif arithmetic_operation=='*':
                print("You chose multiplication")
            elif arithmetic_operation=='/':
                print("You chose division")
            else:
                print("Invalid.\n")
                continue
            
            firstN=int(input("\nWhat is your first number?\n"))
            secondN=int(input("\nWhat is your second number?\n"))
            
            if arithmetic_operation=='+':
                result=firstN+secondN
            elif arithmetic_operation=='-':
                result=firstN-secondN
            elif arithmetic_operation=='*':
                result=firstN*secondN
            elif arithmetic_operation=='/':
                result=firstN/secondN
            
            # Print the Result
            print(f"\nHere is your result\n:{result}")
            
            # Ask user whether to try again or not
            restart=str(input("\nWould you like to try again? (y or n only.)\n:"))
            while True:
                # End if no
                if restart.lower()=='n':
                    return
                # Repeat if yes
                elif restart.lower()=='y':
                    break
                else:
                    print("\nInvalid.\nTry again? (y/n)\n:")
                    
        except ZeroDivisionError:
            print("Sorry! You can't divide by zero.")
        except ValueError:
            print("Sorry! Numbers only.")
        finally:
            # End with Thank you!
            print("\nThank you!")

SimpleCalculator()
    





