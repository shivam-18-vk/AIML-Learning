import random
students = ["Rahul", "Aman", "Shivam", "Priya", "Karan"]
marks=[random.randint(1 , 100) for marks in range(5)]
for student,mark in zip(students,marks):
    print(student,"=",mark)
highest_scorer=[student for student, mark in zip(students  , marks) if mark>=80]
print("highest scorer: ", highest_scorer)
passed_students=[student for student, mark in zip(students, marks) if mark>=40]
print("passed_students: ",passed_students)
failed_students=[student for student, mark in zip(students, marks) if mark<40]
print("failed_students: ", failed_students)
average_marks=sum(marks)/len(marks)
print("average: ",average_marks)
highest_mark=max(marks)
print("highest_mark",highest_mark)
