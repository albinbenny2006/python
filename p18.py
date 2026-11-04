l1 = [1,2,3,4,5,6,7,8,9,10]

i = 0

while i < len(l1):
    if l1[i] % 2 == 0:
        l1.pop(i)
    else:
        i += 1

print(l1)
