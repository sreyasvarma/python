student_scores={
    "John": 85,
    "Jane": 92,
    "Bob": 75,
    "Alice": 95,
    "Eve": 54
}

def grade(score):
    if score>=91:
        return "Outstanding"
    elif score >=81 and score <=90:
        return "Excellent"
    elif score >=71 and score <=80:
        return "Good"
    else:
        return "Needs Improvement"

name=input("Enter the student name you want to know the grade for: ")
score=student_scores[name]
grade(score)