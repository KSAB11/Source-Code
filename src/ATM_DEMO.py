# Simple ATM system

def main():

    # Virtual database 
    balance = 10000
    password = "1234"
    user_input = ""
    chance = 3
    Attempts = 0

    # Ask user for pin
    while chance > Attempts:
        user_input = input("Enter your PIN: ")

    # login PIN 3 attempts max  
        if user_input == password:
            print("\nLogin successful!")
            break
      
        Attempts += 1
        print(f"Incorrect PIN! {chance - Attempts} attempts left.\n")
    else:
        print("Account is locked!")
        return
         
    while True:
    
    # Menu display
        print("\n+++ATM MENU+++")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Check balance")
        print("4. Exit")

    # Ask for user's input
        choice = int(input("\nPlease select from 1-4: "))

    # Process and output
        match choice:
            case 1:
                amount = int(input("Enter amount to withdraw: "))
                if balance < amount:
                    print("\nInsufficient balance!")
                else:
                    balance -= amount
                    print(f"\nWithdraw Successful! New balance: {balance}")
            case 2:
                amount = int(input("Enter amount to deposit: "))
                balance += amount
                print(f"\nDeposit Sucessful! New balance: {balance}")
            case 3:
                print(f"\nTotal balance: {balance}")
            case 4:
                print("\nThankyou!")
                break
            case _:
                print("\nInvalid! please try again.")

if __name__ == "__main__":
    main()