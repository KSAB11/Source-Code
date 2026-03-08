# Simple calculator module 

def python_calculator(x, y):

    print("Select operation.")
    print("+. Addition.")
    print("-. Subtraction.")
    print("*. Multiplication.")
    print("/. Division.")
   
    choice = input("\nEnter operation: ")
    # Take input for calculation
    first_number = int(input(": "))
    second_number = int(input(": "))
   
    # Addition
    if choice == "+":
        result = first_number + second_number
        print(f"\n{first_number} + {second_number} = {result}")

    # Subtraction
    elif choice == "-":
        result = first_number - second_number
        print(f"\n{first_number} - {second_number} = {result}")

    # Multiplication
    elif choice == "*":
        result = first_number * second_number   
        print(f"\n{first_number} * {second_number} = {result}")

    # Division
    elif choice == "/":
        result = first_number / second_number
        print(f"\n{first_number} / {second_number} = {result}")
        
    # Syntax Error
    else:
        print("Syntax Error")

if __name__ == "__main__":
    python_calculator(0, 0)
