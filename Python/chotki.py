def show_all_students(students):
    for student in students:
        print(student["name"],":",student["marks"])
    return students
def get_passed_students(students):
    passed_students=[student["name"] for student in students if student["marks"] >= 70]
    return passed_students
def get_failed_students(students):
    failed_students=[student["name"] for student in students if student["marks"] < 70]
    return failed_students
def highest_scorer_student(students):
    if not students:
        return None
    highest_score=students[0]
    for student in students:
        if student["marks"] > highest_score["marks"]:
            highest_score=student
    return highest_score
def average_marks(students):
    if not students:
        return 0
    total_marks=0
    for student in students:
        total_marks+=student["marks"]
    average=total_marks/len(students)
    return average
def add_student(students, name, marks):
    students.append({"name": name, "marks": marks})
    return students
def remove_student(students, name):
    for student in students:
        if student["name"]==name:
            students.remove(student)
            print(f"Student {name} removed successfully.")
            return students
    print("Student not found.")
    return students

students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 62},
    {"name": "Charlie", "marks": 91},
    {"name": "David", "marks": 55},
    {"name": "Eva", "marks": 78}
]
while True:
    print("1. Show all students")
    print("2. Show passed students")
    print("3. Show failed students")
    print("4. Show highest scorer")
    print("5. Show average marks")
    print("6. Add a new student")
    print("7. Remove a student")
    print("8. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        show_all_students(students)
    elif choice == "2":
        passed_students = get_passed_students(students)
        print("Passed Students:", passed_students)
    elif choice == "3":
        failed_students = get_failed_students(students)
        print("Failed Students:", failed_students)
    elif choice == "4":
        highest_scorer = highest_scorer_student(students)
        if highest_scorer is None:
            print("highest scorer is not available")
        else:    
            print("Highest Scorer:", highest_scorer["name"], "with marks:", highest_scorer["marks"])
    elif choice == "5":
        avg_marks = average_marks(students)
        print("Average Marks:", avg_marks)
    elif choice == "6":
        name = input("Enter student name: ")
        while True:
         try:
            marks = int(input("Enter student marks: "))
            break
         except ValueError:
            print("Invalid ,enter a number") 
         else:       
            add_student(students, name, marks)
            print("new list:",students)
    elif choice == "7":
        name = input("Enter student name to remove: ")
        remove_student(students, name)
    elif choice == "8":
        break
    else:
        print("Invalid choice. Please try again.")