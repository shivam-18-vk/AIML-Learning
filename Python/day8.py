import requests
url ="https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
print(response.status_code)
data=response.json()

total=0

for user in data:

        name=user["name"]
        email=user["email"]
        print(name , " : ", email )
        total+=1

if total == 0:
    print("No users found")
else:
    print("Total:", total)

  
   

     



