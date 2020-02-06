# f=open("harry.txt","r")
# # tell()-where are  on file pointer
# print(f.tell())
# print(f.readline())
# # seek()-file pointer ko decide krke le aata h waps se
# f.seek(11)
# # print(f.tell())
# print(f.readline())
# # print(f.tell())
#
# f.close
f=open("Eating.txt", "a")
f.write("Bread,Rice")
f.close()