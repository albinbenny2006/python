numbers = list(map(int, input("Enter numbers: ").split()))

result = []

for i in numbers:
    if i not in result:
        result.append(i)

print("List after removing duplicates:", result)
