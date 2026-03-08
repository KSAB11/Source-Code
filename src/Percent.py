# This program calulates the percentage of a number

def Percentage():

    #  Display greetings
    print("\nPlease input the number and the percentage you want to calculate below!")

    while True:
        try:
            # Get user input for number and percentage
            number = float(input("\nEnter the number: ").replace(",", ""))
            percentage = float(input("Enter the percentage: ").replace(",", ""))

        # Handle invalid input to try again    
        except ValueError:
            print("Invalid input! Please try again.")
            continue
        
        # Check for negative input to break the loop and exit
        if number < 0 or percentage < 0:
            print("Invalid input! Please try again.")
            continue

        #Calculation and the formula
        result = (number * percentage) / 100

        # Display the result
        print(f"\n{percentage}% of {number:,.2f} is {result:,.2f}")

         # Ask user to continue or exit after calculating the percentage
        choice = input("\nPress 1 to calculate percentage again | Press 2 to exit: ")
        match choice:
            case "1":
                continue
            case "2":
                print("\nThank you!")
                return
            case _:
                print("\nInvalid input! Please try again.")
                continue

if __name__ == "__main__":
    Percentage()