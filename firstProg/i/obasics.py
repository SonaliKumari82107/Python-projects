#   f = open("sona.txt","w+")
#   f.write("hii this is ")
#   f.seek(0)
#   print(f.read())
#   print(f.tell())
#   f.close()


#    import datetime
#    print(datetime.datetime.now())

#   0. name will be asked
#   1. option- read the file or write the file.
#   2. if read:  option- movie or eating history
#   3. else write: option - movie or eating
#   4. Do u want to exit.

#   hint- datetime module
#   '\n' character should be used
#   'a' will be used
#   sara code while(1) k ander hoga


#   input - name, read or write
#   for eg. name_movie.txt or name_eat.txt
#   ritik_movie.txt, ritik_eat.txt


import datetime

k= 9
def sll(x, y):
    return x+y
#
# if __name__ == '__main__':
#
#         Name=input("What is Your Name?\n")
#         while(1):
#          b=("""OPTION :-
#            1.Read the file,
#            2.Write the file""")
#          print(b)
#
#          Select=input("Enter the option 1/2 :\n")
#
#          if Select=="1":
#             print("Read the file")
#             z = ("""OPTION :-
#                1.Movie,
#                2.Eating""")
#             print(z)
#             choice = input("Enter the option 1/2 :")
#             if choice=="1":
#                 f = open(Name+"_Movie.txt", "r")
#                 f.seek(0)
#                 print(f.read())
#                 f.close()
#
#             elif choice=="2" :
#                 f = open(Name+"_food.txt", "r")
#                 f.seek(0)
#                 print(f.read())
#                 f.close()
#             else:
#                 print("Invalid valid")
#          elif Select=="2" :
#             print("Write the file")
#             r=("""OPTION :-
#                1.Movie,
#                2.Eating""")
#             print(r)
#             choice = input("Enter the option 1/2 :")
#             if choice == "1":
#                 Movie_name=input("Enter the Movie_name:\n")
#                 f=open(Name+"_Movie.txt","a+")
#                 f.write(Movie_name)
#                 f.close()
#             elif choice == "2":
#                 food_name = input("Enter the food_name:\n")
#                 f = open(Name+"_food.txt", "a+")
#                 f.write(f"{datetime.datetime.now()}  -- {food_name}  "+"\n")
#                 f.close()
#             else:
#                 print("Invalid valid")
#          else:
#             print("Invalid valid")
#          c= input("Do you want to exit? Y/N: ")
#          if(c== "y"):
#             print("BYE!!!!")
#             exit(0)
#          else:
#              continue
#
#

