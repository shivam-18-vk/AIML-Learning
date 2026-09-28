def get_number():
    while True:
        try:
            number=int(input("Enter the number"))
        except ValueError:
            print("Invalid input")
        else:
            return number
def add(a,b):
    add=a+b
    return add
def sub(a,b):
    sub=a-b
    return sub
def multi(a,b):
    multy=a*b
    return multy
def divide(a,b):
  while True:
    try:
        divide=a/b
    except ZeroDivisionError:
        return "cannot divide by 0"
    else:
        return divide

a=get_number()
b=get_number()
while True:
    print("1. ADD")
    print("2. SUB")
    print("3. MULTI")
    print("4. DIVIDE")
    print("5. exit")
    choice=input("enter choice(1-5): ")
    if choice=="1":
        result=add(a,b)
        print("Addition: ",result)
    elif choice=="2":
        answer=sub(a,b)
        print("subtraction: ",answer)
    elif choice=="3":
        multy=multi(a,b)
        print("Multiplication: ",multy)
    elif choice=="4":
        division=divide(a,b)
        print("Division: ",division)
    elif choice=="5":
        print("goodbye")
        break
    else:
        print("Invlaid choice")





    