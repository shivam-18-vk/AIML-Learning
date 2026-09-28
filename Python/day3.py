import json

student = {
"name": "Shivam",
"age": 20,
"marks": 85
}
with open("student.json" , "w") as file:
   json.dump(student , file)
with open("student.json" , "r") as file:
    data=json.load(file)
    print(data)
data["marks"]=input("enter the number")
with open("student.json" , "w") as file:
   json.dump(data , file)
with open("student.json" , "r") as file:
    new_data=json.load(file)
    print(new_data)
