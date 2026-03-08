# Number guessing game simulation
def guessing_game():
    
    chance = 3
    attempts = 0

    import random
    number_to_guess = random.randint(1, 10)

    while chance > attempts:
        user_guess = int(input("Guess a number between 1 and 10: "))

        if user_guess == number_to_guess: 
             print("\nCongratulations! You won the game!")
             break
            
        attempts += 1
        print(f"Nice try! {chance - attempts} chances left.\n")
    else:
        print("\nBetter luck next time!")
        return

        
if __name__ == "__main__":
     guessing_game()