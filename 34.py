import math

start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

result = []

for num in range(start, end + 1):
    if 1000 <= num <= 9999:
        root = math.isqrt(num)

        if root * root == num:
            digits = str(num)

            if all(int(digit) % 2 == 0 for digit in digits):
                result.append(num)

print("Numbers are:", result)
