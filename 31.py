age= int(input("Enter the age: "))

result =lambda age: "Eligible" if age >= 18 else "Not eligible"

print(result(age))
