numbers = input("Enter numbers separated by spaces: ")
numbers = numbers.split()
numbers = [int(i) for i in numbers]

print("Largest:", max(numbers))
print("Smallest:", min(numbers))
