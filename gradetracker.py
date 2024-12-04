def get_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def calculate_average(grades):
    return sum(grades) / len(grades)

def add_student():
    name = input("Enter student's name: ")
    num_subjects = int(input("Enter number of subjects: "))
    
    grades = []
    for i in range(num_subjects):
        grade = float(input(f"Enter grade for subject {i+1}: "))
        grades.append(grade)
    
    average = calculate_average(grades)
    letter_grade = get_grade(average)

    print(f"\nStudent: {name}")
    print(f"Grades: {grades}")
    print(f"Average: {average:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print("-" * 30)

def grade_tracker():
    print("Student Grade Tracker")
    while True:
        add_student()
        cont = input("Do you want to add another student? (y/n): ").lower()
        if cont != 'y':
            break
    print("Goodbye!")

if __name__ == "__main__":
    grade_tracker()
