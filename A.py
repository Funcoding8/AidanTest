def grade_score(score):
    grades = ["A", "B", "C", "D", "F"]
    if 90 <= score <= 100:
        return grades[0]
    elif 80 <= score <= 89:
        return grades[1]
    elif 70 <= score <= 79:
        return grades[2]
    elif 60 <= score <= 69:
        return grades[3]
    elif 50 <= score <= 59:
        return grades[4]
    else:
        return "Invalid score"

def main():
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                grade = grade_score(score)
                print("Your grade is:", grade)
                break
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    print("Please put it in numbers")
    main()
    