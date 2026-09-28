import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

data = response.json()


def show_all_users(data):
    total=0
    for user in data:
        name=user["name"]
        email=user["email"]
        print(name, " : ",email )
        total+=1
    return total

def search_user_city(data):
    city=input("Enter the city: ")
    total=0
    for user in data:
        if user["address"]["city"]==city:
            print(user["name"]," : ",user["email"])
            total+=1

    if total==0:
        print("user not found")
    return total

def search_user_name(data):
    name=input("Enter the name: ")
    for user in data:
        if user["name"]==name:
            print(user["name"]," : ",user["email"])
            return True
    return False

while True:
    print("\n===== USER DIRECTORY =====")
    print("1. Show all users")
    print("2. Search by city")
    print("3. Search by name")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice=="1":
       user_details=show_all_users(data)
       print(user_details)

    elif choice=="2":
       user_city=search_user_city(data)
       print(user_city)

    elif choice=="3":
       found = search_user_name(data)
       print("Found:", found)

    elif choice=="4":
        print("goodbye")
        break

    else:
        print("Invalid Input")