import json
def show_all_students(students):
    if not students:
        print("students not found")
        return
    for student in students:
        print(student["name"] , ":" , student["marks"])
    return
def find_students(students,name):
    for student in students:
        if student["name"]==name:
            print(student)
            return student
    return None
def add_student(students , name , marks):
    students.append({
        "name":name,
        "marks":marks
    })
    print(students)
    return True
def remove_student(students , name):
    for student in students:
        if student["name"]==name:
            students.remove(student)
            print(students)
            return True
    return False
def update_marks(students , name , new_marks):
    for student in students:
        if student["name"]==name:
            student["marks"]=new_marks
            print("Updated marks: ",new_marks)
            return True
    return False
def average_marks(students):
    total = 0

    for student in students:
        total += student["marks"]

    average = total / len(students)

    print("Average:", average)

    return average
def passed_students(students):
    pass_students=[student["name"] for student in students if student["marks"]>=70]
    print("pass students: ",pass_students)
    return pass_students
def highest_scorer(students):
    if not students:
        return None
    highest=students[0]
    for student in students:
        if student["marks"]>highest["marks"]:
            highest=student
    print("highest scorer: ",highest)
    return highest
students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 62},
    {"name": "Charlie", "marks": 91},
    {"name": "David", "marks": 55}
]
while True:
    print("1. show all students: ")
    print("2. find students: ")
    print("3. add students: ")
    print("4. remove students: ")
    print("5. update students: ")
    print("6. average marks: ")
    print("7. passed students: " )
    print("8. highest scorer: " )
    print("9. students to json: " )
    print("10. json to students: ")
    print("11. exit")

    choice=input("Enter the choices: ")

    if choice=="1":
        show_all_students(students)

    elif choice=="2":
        name=input("Enter the name")
        find_students(students,name)
    elif choice=="3":
        name=input("Enter the name")
        marks=int(input("enter marks"))
        add_student(students,name,marks)
    elif choice=="4":
        name=input("Enter the name")
        remove_student(students , name)
    elif choice=="5":
        name=input("Enter the name")
        new_marks=int(input("enter marks"))
        update_marks(students,name,new_marks)
    elif choice=="6":
        average_marks(students)
    elif choice=="7":
        passed_students(students)
    elif choice=="8":
        highest_scorer(students)
    elif choice=="9":
       with open("students.json" , "w") as file:
          json.dump(students , file)
          print("saved successfully")
    elif choice=="10":
       with open("students.json" , "r") as file:
         students=json.load(file)
         print(students)
    elif choice=="11":
        print("goodbye")
        break    


    



    