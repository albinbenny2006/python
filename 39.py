numbers = list(map(int, input("Enter numbers: ").split()))

numbers = list(set(numbers))
numbers.sort()

print("Second largest element:", numbers[-2])
