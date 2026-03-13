# Quiz game using boolean expressions

class Quiz:
    def questions(self):
        print("\n++++++++++++Welcome to the Quiz Game!++++++++++++")
        print("Rules: Must answer using T or F.")
        
        # Questions
        q1 = input("\n1. Java and Python are just the same (T/F): ").upper()
        q2 = input("\n2. Python is a programming language. (T/F): ").upper()
        q3 = input("\n3. Boolean value can be only True or False. (T/F): ").upper()
        q4 = input("\n4. Git is a operating system. (T/F): ").upper()
        q5 = input("\n5. Python uses indentation to define code blocks. (T/F): ").upper()
        q6 = input("\n6. A loop is used to repeat a block of code. (T/F): ").upper()
        q7 = input("\n7. Data structure and algorithms are important in programming. (T/F): ").upper()
        q8 = input("\n8. A variable is used to store data in a program. (T/F): ").upper()
        q9 = input("\n9. Mathematics is considered a language. (T/F): ").upper()
        q10 = input("\n10. Python was created by Guido van Rossum. (T/F): ").upper()
        
        self.calculate_score(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10)

    def calculate_score(self, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
        score = 0

        # Calculate overall score
        if q1 == "T":
            score += 1
        if q2 == "T":
            score += 1          
        if q3 == "T":
            score += 1
        if q4 == "F":
            score += 1
        if q5 == "T":
            score += 1
        if q6 == "T":
            score += 1
        if q7 == "T":
            score += 1
        if q8 == "T":
            score += 1
        if q9 == "T":
            score += 1
        if q10 == "T":
            score += 1

        print(f"\nYour score is: {score}/10")
        self.calculate_passed(score)

    # Passed or failed indicator
    def calculate_passed(self, score):
        if score >= 7:
            print("You passed the quiz!")
        else:
            print("Better luck next time.")

# Main function to run the quiz
if __name__ == "__main__":
    quiz = Quiz()
    quiz.questions()

    # Ask user if they want to take the quiz again.
    while True:
        play_again = input("\nTry again? (Y/N): ").upper()
        if play_again == "Y":
            quiz = Quiz()
            quiz.questions()
        elif play_again == "N":
            print("...")
            break
        else:
            print("Invalid input! Please enter Y or N.")
    