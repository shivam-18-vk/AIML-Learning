class Student:
    def __init__(self , name , marks):
        self.name=name
        self.marks=marks

    def display(self):
        print("Name: ",self.name)
        print("marks : ",self.marks)
    def is_passed(self):
        if self.marks>=70:
            return True
        else:
            return False
    def grade(self):
        if self.marks>=90:
            return "A"
        elif self.marks>=80:
            return "B"
        elif self.marks>=70:
             return "C"
        elif self.marks<70:
             return "F"
    def compare_marks(self , other_student):
        if self.marks>other_student.marks:
            return self.name +" is higher than " + other_student.name
        elif self.marks<other_student.marks:
            return self.name+" is lower than "+other_student.name
        else:
            return "both have equal scores"
    def report(self):
        name=self.name
        marks=self.marks
        passed=self.is_passed()
        grade=self.grade()
        scholarship=self.scholarship_eligible()
        return f"Name: {name},\n Marks: {marks},\n Passed: {passed},\n Grade: {grade} , \n Scholarship: {scholarship}"
    def scholarship_eligible(self):
        if self.marks>=90:
            return self.name +" is eligible" 
        else:
            return self.name+" is not eligible"
        
        
      

student1=Student("Shivam" , 90)
student2=Student("aman" , 87)
student3=Student("niraj" , 80)

while True:
  
  print("1. student1 detail: ")
  print("2. student2 detail: ")
  print("3. student3 detail: ")
  print("4. students comparison: ")
  print("5. students report: ")
  print("6. schlorship eligibility: ")
  print("7. exit")

  choice=input("Enter your choice(1-7): ")

  if choice=="1":
    student1.display()
    print("result: ",student1.is_passed())
    print(student1.grade())

  elif choice=="2":
    student2.display()
    print("result: ",student2.is_passed())
    print(student2.grade())

  elif choice=="3":
    student3.display()
    print("result: ",student3.is_passed())
    print(student3.grade())

  elif choice=="4":
    print(student1.compare_marks(student2))
    print(student2.compare_marks(student3))
    print(student3.compare_marks(student2))

  elif choice=="5":
      print(student1.report())
      print(student2.report())
      print(student3.report())

  elif choice=="6":
    print("scholarship=",student1.scholarship_eligible())
    print("scholarship=",student2.scholarship_eligible())
    print("scholarship=",student3.scholarship_eligible())

  elif choice=="7":
      print("Goodbye")
      break




