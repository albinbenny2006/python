words=input("enter words:").split()
longest=words[0]
for word in words:
   if(len(word)>len(longest)):
      longest=word
           
print("longest word",longest)
print("length of word :", len(longest))
