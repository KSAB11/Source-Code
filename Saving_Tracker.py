# Savings Goal Tracker 
# Console/simulation program

def Savings_Tracker():

    # Display Greetings
    print("+++++++++++++++++++++++++++++++++++++")
    print("  Welcome to Savings Goal Tracker!   ")
    print("+++++++++++++++++++++++++++++++++++++")

    while True:
        try:
            # Get user input for savings goal and monthly savings
            goal = float(input("\nEnter your savings goal: ").replace(",", ""))
            monthly_savings = float(input("Enter your monthly savings: ").replace(",", ""))

        # Handle invalid input to try again    
        except ValueError:
            print("Invalid input! Please try again.")
            continue
        
        # Check for negative input to break the loop and exit
        if goal <= 0 or monthly_savings <= 0:
            print("Invalid input! Please try again.")
            continue
    
        total = 0
            
        for month in range (1,13): 
            total += monthly_savings
            percent = (total / goal) * 100

            # Display the total saved, remaining amount, and percentage of goal reached
            print(f"\n{month}: Total saved: ${total:,.2f}")
            print(f"remaining: ${goal - total:,.2f} | {percent:.1f}% of your goal")

            # Check if savings if achieve if not display the remaining amount to reach the goal
            if total >= goal:
                month_word = "month" if month == 1 else "months" 
                print(f"\nGoal reached! you saved ${goal:,.2f} in {month} {month_word}!")
                break
            
            else:
                print(f"\nYou need ${goal - total:,.2f} more to reach your goal.")
        
        # Ask user to continue or exit after tracking savings goal
        choice = input("\nPress 1 to track again | Press 2 to exit: ")
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
    Savings_Tracker()
