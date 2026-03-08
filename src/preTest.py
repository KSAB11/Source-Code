num = -1

while num <= 0:
    num = int (input("Please enter a positive integer: "))

print("you enetered", num)


password = "1234"
user_input = ""

while user_input != password:
    user_input = input("Enter the password: ")

print("Access granted!")


num_list = [1, 2, 3, 4, 5]

for num in num_list:
    print(num * 2)


names = ["Alice", "Bob", "Charlie"]

for name in names:
    print("Hello, " + name + "!")   


