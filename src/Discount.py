# Discount calculator 

def calculate_discount(discount: float, price: float) -> float:
    return price - (price * discount / 100)

def get_user_input():
    #  Display greetings
    print("\nPlease input the discount and price to calculate below!")

    while True:
        try:
            # Get user input for number and percentage
            discount = float(input("\nEnter the discount %: ").replace(",", ""))
            price = float(input("Enter the price $: ").replace(",", ""))

        # Handle invalid input to try again    
        except ValueError:
            print("Invalid input! Please try again.")
            continue
        
        # Check for negative input to break the loop and exit
        if discount < 0 or discount > 100 or price < 0:
            print("Invalid input! Discount must be between 0-100 and price or discount must be positive.")
            continue

        return discount, price

if __name__ == "__main__":
    discount, price = get_user_input()
    final_price = calculate_discount(discount, price)
    print(f"\nThe total price after {discount:.1f}% discount is: ${final_price:,.2f}")