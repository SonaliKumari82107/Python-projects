# pattern printing
"""
 Input=Integer n
 Boolean =True or False
 true
 *
 **
 ***
 ****
 False
 ****
 ***
 **
 *
"""
# n=int(input("enter a number:"))
# a=int(input("enter your boolean number:"))
# if(bool(a)):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print("*",end="")
#
# else:
#     for i in range(1,n+1):
#         for j in range(1,n+2-i):
#             print("*",end="")
#         print()

i = 0;
while 1:
    print(i," ",end=""),
    i=i+1;
    if i == 10:
        break;
print("came out of while loop");