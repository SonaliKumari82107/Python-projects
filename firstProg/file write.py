# f=open("harry.txt","w")
# a=f.write("harry is a good brother\n")
# print(a)
# f.close()

# f=open("harry2.txt","a")
# a=f.write("harry is a good brother\n")
# print(a)
# f.close()

# Handle read and write both
f=open("harry2.txt","r+")
print(f.read())
f.write("Thank you")