# Python loops, For loops and while loops / List printing sample.

# Fruit class and functions
class Fruits:
    def __init__(self, name):
        self.name = name

def fruits_forLoop():
    fruit_list = [Fruits("Apple"), Fruits("Banana"), Fruits("Cherry"), Fruits("Date"), Fruits("Mango")]

    for fruit in fruit_list:
        print("I love " + fruit.name)
    
    print() # Space for readability

def fruits_while_Loop():
    fruit_list = [Fruits("Apple"), Fruits("Banana"), Fruits("Cherry"), Fruits("Date"), Fruits("Mango")]
    
    i = 0
    while i < len(fruit_list):
        print("I love " + fruit_list[i].name)
        i += 1
    
    print() # Space for readability

# Car class and functions
class Cars:
    def __init__(self, name):
        self.name = name

def cars_forLoop(): # By car brand
    car_list = [Cars("Toyota"), Cars("Honda"), Cars("Ford"), Cars("BMW"), Cars("Mercedes")]

    for car in car_list:
        print(car.name)
    
    print() # Space for readability

def cars_while_Loop(): # By car speed
    car_list = [Cars("130mph"), Cars("134mph"), Cars("120mph"), Cars("150mph"), Cars("140mph")]
    
    i = 0
    while i < len(car_list):
        print(car_list[i].name)
        i += 1

    print() # Space for readability

# Country class and functions
class Countries:
    def __init__(self, name):
        self.name = name

def countries_forLoop(): # By nation
    country_list = [Countries("USA"), Countries("Japan"), Countries("Germany"), Countries("France"), Countries("Italy")]

    print(country_list[3].name) 
    
    print() # Space for readability

def countries_while_Loop(): # By capital
    country_list = [Countries("Washington D.C."), Countries("Tokyo"), Countries("Berlin"), Countries("Paris"), Countries("Rome")]
    
    print(country_list[3].name)
        
# Main to call all function
def main():
    fruits_forLoop()
    fruits_while_Loop()
    cars_forLoop()
    cars_while_Loop()
    countries_forLoop()
    countries_while_Loop()

if __name__ == "__main__":
    main()