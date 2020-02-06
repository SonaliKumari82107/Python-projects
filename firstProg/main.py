print("WELCOME TO THE GAME")
i=1
user=0
computer =0
print('''
    1.Scissor
    2.Paper
    3.Rock''')

while(i<=10):
    select = input("enter the number 1/2/3:")
    if select == '1':
        print("Scissor")
    elif select == '2':
        print("Paper")
    elif select == '3':
        print("Rock")
    else:
        print("Invalid valid")
        continue

    import random
    l = ["Scissor", "Paper", "Rock"]
    r=random.choice(l)
    print("Computer choose ",r)

    if ((select=='1' and r=='Paper')or (select=='2' and r=='Rock') or (select=='3' and r=='Scissor')):
        print("You wins")
        user+=1
    elif((select=='1' and r=='Scissor') or (select=='2' and r=='Paper')or (select=='3' and r=='Rock')):
        print("Draw")
    else:
        print("You Lost")
        computer+=1

    print(10-i, "chance left\n");
    i = i + 1;

if(user>computer):
    print("HURRAY!!!! YOU DONE IT....")
elif(user==computer):
    print("Draw.....")
else:
    print("OOPS!!!!YOU LOST.....")

print("You Scores: ",user)
print("Computer Scores: ",computer)





 