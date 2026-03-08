total = 0
while True:
    
    print("===MENU===")
    print("1. Burger - 120")
    print("2. Pizza - 250")
    print("3. Fries - 80")
    print("4. Exit")
    
    choice = int(input("Enter your order: "))
    match choice:
        case 1:
            itm = int(input("Enter quantity: "))
            total += (120 * itm)
            print("Added burger")
    
        case 2:
            itm = int(input("Enter quantity: "))  
            total += (250 * itm) 
            print("Added pizza")
    
        case 3:
            itm = int(input("Enter quantity"))
            total += (80 * itm) 
    
        case 4:
            print("Exit")
            print("order summary: ")
            print("Total bill: " ,total)
            print("Thankyou!")
            break

        case _:
            print("Invalid!")
    
