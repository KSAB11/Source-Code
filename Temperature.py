# Temperature calculator

def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5/9

def main():
    print("\nTemperature Converter")

    while True:
        try:
            temp = float(input("\nEnter the temperature to convert: "))
            choice = int(input("1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\nEnter: "))

            if choice == 1:
                result = celsius_to_fahrenheit(temp)
                print(f"\n{temp}°C is equal to {result}°F")

            elif choice == 2:
                result = fahrenheit_to_celsius(temp)
                print(f"\n{temp}°F is equal to {result}°C")

            else:
                print("Invalid choice! Please enter 1 or 2.")
                continue

            again = input("\nDo you want to convert another temperature? (y/n): ").lower()
            if again != 'y':
                print("\nThank you!")
                break

        except ValueError:
            print("Invalid input! Please try again.")
            continue
            
if __name__ == "__main__":
    main()