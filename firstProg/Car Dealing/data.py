# from i import obasics
# import i.obasics
#
# l = obasics.sll(6,6)
# print(l)

import i.obasics as ob
#
# l = ob.sll(6,6)
# print(l)
# k=8
# print(k)
# print(ob.k)
# l = dir(ob)
# print(l)


import time;
from datetime import datetime as dt
#converted datetime.datetime as dt........

#returns the formatted time
# print(time.asctime(time.localtime(time.time())))
# for i in range (1,4):
#     print(i)
#     time.sleep(5)


# for i in range(3):
#     print(datetime.datetime.now())
#     time.sleep(5)

# print(dt.now().year)
# print(dt.now().day)
# print(dt.now().month)



#Compares the time. If the time is in between 8AM and 4PM, then it prints working hours otherwise it prints fun hours
if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,17):
    print("Working hours....")
else:
    print("fun hours")

# from i import obasics
# import i.obasics
#
# l = obasics.sll(6,6)
# print(l)

import i.obasics as ob
#
# l = ob.sll(6,6)
# print(l)
# k=8
# print(k)
# print(ob.k)
# l = dir(ob)
# print(l)


import time;
from datetime import datetime as dt
#converted datetime.datetime as dt........

#returns the formatted time
# print(time.asctime(time.localtime(time.time())))
# for i in range (1,4):
#     print(i)
#     time.sleep(5)


# for i in range(3):
#     print(datetime.datetime.now())
#     time.sleep(5)

# print(dt.now().year)
# print(dt.now().day)
# print(dt.now().month)


from datetime import datetime as dt
#Compares the time. If the time is in between 8AM and 4PM, then it prints working hours otherwise it prints fun hours
if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,17):
    print("Working hours....")
else:
    print("fun hours")


