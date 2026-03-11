# Student score recorder

def students_score():
    print("Mathematics, Science, English, History, Art\n")

    students = {
        "Alice": (85, 90, 89, 78, 80),
        "Bob": (92, 85, 88, 91, 87),
        "Charlie": (78, 82, 85, 80, 79),
        "David": (89, 88, 92, 91, 89),
        "Eve": (88, 90, 85, 87, 86)
    }

    for students, scores in students.items():
        print(f"{students}: {scores}")

def main():
    students_score()
    print("\nStudent's scores from each categories")

if __name__ == "__main__":
    main()
