# sum and average 

def sum_and_average(): 
    numbers = [10,20,30,40] # List of numbers 

    total = sum(numbers) # Combine all numbers and sum = 100
    average = total / len(numbers) # Divide the total by number of elements to get avg
    return total, average # Logic

def square(number):    
    return number * number # Logic

def cube(number):
    return number * number * number # Logic
    
# Main/UI
def main():

    print("Simple practice code:)")

    total, average = sum_and_average() # Sum and average
    print("Sum:", total) 
    print("Average: ", average)

    number = int(input("\nNumber to square: ")) # Square
    squared = square(number)
    print(f"Square of {number} is {squared}")

    number = int(input("\nNumber to cube: ")) # Cube
    cubed = cube(number)
    print(f"Cube of {number} is {cubed}")

# Call main to execute program
if __name__ == "__main__":
    main()