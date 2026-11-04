def vote(age):
    if age >= 18:
        print("Eligible")
    else:
        print("Not eligible")

age = int(input("Enter the age: "))

vote(age)
