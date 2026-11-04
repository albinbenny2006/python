str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

a=list(str1)
b=list(str2)
b[0]=c
c=a[0]
a[0]=b[0]
b[0]=c
str1="".join(a)
str2="".join(b)
print(str1 + " " + str2)
