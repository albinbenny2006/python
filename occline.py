line = input("enter the line :")

counts = {}

Sentence = line.split()

for word in Sentence :
  
  if word in counts :
     
    counts[word]+=1
  else :
    
    counts[word]=1
    
for k,v in counts.items() :
  
  print(k,v)    
