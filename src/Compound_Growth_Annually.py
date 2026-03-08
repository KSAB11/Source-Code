# Compound Growth Annually Console
# Calculate compound growth after years

# principal = initial money
# rate = interest per year
# time = number of years

# Function to calculate/formula for compound growth
def compound_growth(principal, rate, time):
    return principal * (1 + rate / 100) ** time

# Function to get user input
def get_user_input():
    while True:
        try:
            print("\n++++++++++++++++++++++++++++++++++++")
            print("     Compound Growth Calculator     ")
            print("++++++++++++++++++++++++++++++++++++")
            
            principal = float(input("\nEnter the initial amount: $").replace(",", ""))    
            rate = float(input("Enter the annual interest rate: "))
            time = float(input("Enter the time in years: "))

        except ValueError:
            print("\nInvalid input! Please try again.")
            continue

        if principal < 0 or rate < 0 or time < 0:
            print("\nInvalid input! Please try again.")
            continue
    
        return principal, rate, time
    
if __name__ == "__main__":
    principal, rate, time = get_user_input()
    Growth = compound_growth(principal, rate, time)
    print(f"\nTotal investment: ${Growth:,.2f}")
