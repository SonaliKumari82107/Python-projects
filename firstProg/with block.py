with open("harry.txt") as f:
   a= f.readlines()
   print(a)


f=open("harry.txt","rt")
a= f.readlines()
print(a)
f.close()
