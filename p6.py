S = input("Enter a string: ")

char = S[0]

S = S.replace(char, '$')

S = char + S[1:]

print(S)
