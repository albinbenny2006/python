list1=['aravind','aparna']
print("the orginal list:\n" +str(list1))
res=[ord(ele) for sub in list1 for ele in sub]
print("The AscII list is :\n" +str(res))
