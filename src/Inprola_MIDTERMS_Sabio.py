print("----------------------------------------------------------------------")
print(">>>GRADE CLASSIFICATION<<<")
#Ask user for input
grade = int(input("Enter your numeric grade (0-100): "))

#Process and output for grade classification
if grade >= 90:
    print("your grade is: A")
elif grade >= 80:
    print("your grade is: B")
elif grade >= 70:
    print("your grade is: C")
elif grade >= 60:
    print("your grade is: D")
else:
    print("your grade is: F")
print("----------------------------------------------------------------------")
print(">>>POSITIVE,NEGATIVE, OR ZERO<<<")
#Ask user for input
num = int(input("Enter a number:"))
#Process and output for positive, negative and zero
if num > 0:
    print(num, "is positive")
elif num < 0:
    print(num, "is negative")
else:
    print(num, "is zero")
print("----------------------------------------------------------------------")
print(">>> SIMPLE PAYROLL SYSTEM<<<")
#Ask user for input
hours = float(input("Enter hours worked:"))
rate = float(input("Enter rate per hour: "))

#Process and output for payroll system
if hours <= 40:
    total = hours * rate
    print("Gross pay: " ,total)
elif hours > 40:
    overtime = (hours - 40) * rate * 1.5
    grossing = (40 * rate) + overtime 
    print("Gross pay: " , grossing)
print("----------------------------------------------------------------------")
print(">>>ELECTRICITY BILL CALCULATOR<<<")
#Ask user for input
units = float(input("Enter units consumed: "))

#Process and output for electricity bill calculator
if units <= 100:
    bill = (units * 5)
    print("Total bill: ", bill)
elif units <= 200: 
    bill = 100 * 5 + (units - 100) * 7
    print("Total bill:" , bill)
elif units > 200:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    print("Total bill: " , bill)
print("----------------------------------------------------------------------")
print("=== End of Exam ===")
