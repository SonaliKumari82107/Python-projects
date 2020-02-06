# globle variable
# l=10
# def function1(n):
#     l=5     # locals variable
#     m=8
#     global l
#     l=l+55
#     print(l)
    # print(m)
    # print(n,"I have printed")

# function1("This is me")
# print(l)

def harry():
    x=20
    def rohan():
        global x
        x=88
    print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)
harry()
print(x)

