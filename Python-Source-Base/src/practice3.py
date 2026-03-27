# Factorial number
# Simple terminal like interface
# y = means to use factorial operation again
# n = exits the program
# unlike terminal ask continue? y/n mainly to execute or not a command
# In this program its emphasize as a "y" for another operation and "n" to exit the program

import math

def factorial():
    print("\nFctorial Terminal")

    while True:
        try: 
            # Factorial Interface
            number = int(input("User.Number:~$ "))

            # Factorial using math library
            result = math.factorial(number)
            print(result)

        except ValueError:
                print("Command not found:")
                print("Try: numbers")
                continue
        
        # Loop until y/n is valid
        while True:

            # y/n Interface
            choice = input("Continue? (y/n):~$ ").lower().strip()

            # y/n Logic
            if choice == 'y':
                break # Go back to main to ask number for operation
            elif choice == 'n':
                return # Exit

if __name__ == "__main__":
    factorial()