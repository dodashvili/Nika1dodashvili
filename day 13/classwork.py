age = int(input("enter your age:"))
if age >= 0 and age < 18:
    print("you are kid")
elif age > 18 and age < 50:
    print("you are an adult")
else:
    print("you are a child")
    