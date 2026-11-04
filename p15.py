a=input("first list of colours:").split(",")
b=input("second list of colours:").split(",")
print("the colours are:")
for color in a:
    if color not in b:
        print(color)
