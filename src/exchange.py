# Peso to US Dollar currency exchange 
# Convert currency between peso and USD using a fixed exchange rate.

EXCHANGE_RATE = 57.4

def peso_to_dollar(peso):
    return peso / EXCHANGE_RATE

def dollar_to_peso(dollar):
    return dollar * EXCHANGE_RATE

def get_user_input():
    print("\nPeso and US Dollar currency exchange")

    while True:
        try:
            # Get user input for conversion choice and amount
            choice = int(input("\n1. Peso to Dollar\n2. Dollar to Peso\nEnter your choice (1 or 2): "))
            if choice not in [1, 2]:
                print("Invalid choice! Please enter 1 or 2.")
                continue

            amount = float(input("Enter the amount to convert: ").replace(",", ""))
            if amount < 0:
                print("Invalid input! Amount must be positive.")
                continue

            return choice, amount

        except ValueError:
            print("Invalid input! Please try again.")
            continue
            

def convert_currency(choice, amount):
   
    if choice == 1:
        converted_amount = peso_to_dollar(amount)
        return f"\n{amount:,.2f} Pesos is equal to ${converted_amount:,.2f} Dollars."
    else:
        converted_amount = dollar_to_peso(amount)
        return f"\n${amount:,.2f} Dollars is equal to {converted_amount:,.2f} Pesos."

def main():
    choice, amount = get_user_input()
    result = convert_currency(choice, amount)
    return result

if __name__ == "__main__":
    print(main())