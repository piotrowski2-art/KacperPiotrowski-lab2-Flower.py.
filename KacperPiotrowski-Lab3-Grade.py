def getGrade(score):
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    elif score >= 0 and score < 60:
        return "F"
    else:
        print("Error: Score must be between 0 and 100.")
        
        return ""

score = int(input("Enter the exam score: "))

grade = getGrade(score)

print("The letter grade is:", grade)