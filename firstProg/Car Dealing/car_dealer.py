# name =?
# if buy: car_name=?   generate a file name+car_name.txt    price =?
# data stored =  datetime  --  buy -- price -- car_name
#
# else sell car_name=?  generate a file name+car_name.txt   price=?
# data stored = datetime -- sell --price  -- car name


import datetime
name=input("What is your name: ")
while(1):
    b = ("""Option:
        1.Sell the Car
        2.Buy the Car""")
    print(b)
    Select = input("Enter the option 1/2: ")
    if Select == "1":
        print("Sell the car")
        car_name = input("Enter the car_name: ")
        price = input("Enter the price: ")
        sell = ("sell")
        f = open(name + "_car_name_price.txt", "a+")
        f.write(f"{datetime.datetime.now()}  -- {sell}--{car_name}----{price}  " + "\n")
        f.close()

    elif Select =="2":
        print("Buy the car")
        car_name = input("Enter the car_name:\n")
        price = input("Enter the price:\n")
        buy = ("buy")
        f = open(name + "_car_name_price.txt", "a+")
        f.write(f"{datetime.datetime.now()}  -- {buy}--{car_name}----{price}  " + "\n")
        print(f.write(f"{datetime.datetime.now()}  -- {buy}--{car_name}----{price}  " + "\n"))
        f.close()


    else:
        print("Invalid valid")

    c = input("Do you want to exit? Y/N: ")
    if (c == "y"):
        print("BYE!!!!")
        exit(0)
    else:
        continue



















