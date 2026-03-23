#

def greet(name):
    g = "Hello " + name + "!"
    return g

def number(num):
    n = "I like the number " + num + " too!"
    return n

def favorite(color):
    c = "Your favorite color is " + color + " That's nice!"
    return c

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))
    num = input("\nEnter your favorite number: ")
    print(number(num))
    color = input("\nEnter your favorite color: ")
    print(favorite(color))

