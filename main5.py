# EduGrade - functions
def calculate_average(mark1, mark2, mark3):
    return (mark1 + mark2 + mark3) / 3

def find_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "Needs Improvement"

name = input("Student name: ")
m1 = float(input("Mark 1: "))
m2 = float(input("Mark 2: "))
m3 = float(input("Mark 3: "))
average = calculate_average(m1, m2, m3)
print("\nStudent:", name)
print("Average:", round(average, 2))
print("Grade:", find_grade(average))
print("Result:", "PASS" if average >= 40 else "FAIL")
