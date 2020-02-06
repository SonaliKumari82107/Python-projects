# def addition(x,y):
#   return x+y
# def subtraction(x,y):
#   return x-y
# def mul(x,y):
#   return x*y
# def division(x,y):
#   return x/y
# def module(x,y):
#   return x%y
# def default(x,y):
#  return"default values"
# switcher = {
#     1: addition,
#     2: subtraction,
#     3: mul,
#     4: division,
#     5: module
# }
# def switch(operation, num1, num2):
#   return switcher.get(operation, default)(num1, num2)
# print('''You can perform operation
#  1. Addition
#  2. Subtraction
#  3. Multiplication
#  4. Division
#  5. Module ''')
#
# select = int(input("Select operation from 1,2,3,4,5 : "))
# num1 = int(input("Enter first number: "))
#  if(num1 > 100):
#     print("Please enter the number smaller than100..")
#     num1= int(input("Enter the first number: "))
# num2 = int(input("Enter second number: "))
# if(num2 > 100):
#     print("Please enter the number smaller than 100..")
#     num2= int(input("Enter the second number: "))
# print (switch(select, num1, num2))




####################################################################################




#25+78=114
#25*3=65
#12/3=5
#555-222=331


# def addition(x,y):
#   return x+y
# def subtraction(x,y):
#   return x-y
# def mul(x,y):
#   return x*y
# def division(x,y):
#   return x/y
# def module(x,y):
#   return x%y
# def default(x,y):
#  return"default values"
# switcher = {
#     1: addition,
#     2: subtraction,
#     3: mul,
#     4: division,
#     5: module
# }
# def switch(operation, num1, num2):
#   return switcher.get(operation, default)(num1, num2)
# print('''You can perform operation
#  1. Addition
#  2. Subtraction
#  3. Multiplication
#  4. Division
#  5. Module ''')
# select = int(input("Select operation from 1,2,3,4,5 : "))
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1== 25 and num2==78 and select==1:
#     print(num1, "+", num2, "=","114")
# elif num1==555 and num2==222 and select==2:
#     print(num1, "-", num2, "=","331")
# elif num1== 25 and num2==3 and select==3:
#     print(num1, "*", num2, "=","65")
# elif num1== 12 and num2==3 and select==4:
#     print(num1, "/", num2, "=","5" )
# else:
#     print("result is : ",switch(select, num1, num2))
#


# def func(name):
#     message = "Hii "+name;
#     return message;
# name = input("Enter the name:")
# print(func(name))
# while(1):
#     a=('''What is your hobby:
#     1. Eating
#     2. Sleeping
#     3. Playing to pubg game
#     4. Listening to Music''')
#     print(a)
#     select = input("Select operations form 1, 2, 3, 4:")
#
#     if select == '1':
#         print("You like to Eating")
#
#
#     elif select == '2':
#         print("You like to Sleeping")
#
#     elif select == '3':
#         print("You like to Playing to pubg game")
#
#     elif select == '4':
#         print("You like to Listening to Music")
#     else:
#         print("Invalid valid")
#
#
#     b= input("Do you want to exit? Y/N: ")
#     if(b == "y"):
#         print("BYE!!!!")
#         exit(0)
#     else:
#         continue






def add(x, y):
   return x + y
def subtract(x, y):
   return x - y
def multiply(x, y):
   return x * y
def divide(x, y):
   return x / y
def module(x,y):
  return x%y
while(1):
    print('''You can perform operation
     1. Addition
     2. Subtraction
     3. Multiplication
     4. Division
     5. Module ''')
    choice = int(input("Select operation from 1,2,3,4,5 : "))
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == '5':
        print(num1, "%", num2, "=", module(num1, num2))
    else:
        print("Invalid input")

    b= input("Do you want to exit? Y/N: ")
    if(b == "y"):
         print("BYE!!!!")
         exit(0)
    else:
     continue





