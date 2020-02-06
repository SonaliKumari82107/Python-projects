# import os
#print os name:
# print(os.name)

#print current directory
# print(os.getcwd())

#change the directory
# os.chdir("D:\\kartik")
# print(os.getcwd())

#print list of files in that particular folder
# r=(os.listdir())
# print(r)

#rename a file
# os.rename("1.txt", "r.txt")

#replace a file
# os.replace("sona.txt", "ram.bmp")

#tmko ek func bnana hai jo three parameters lega
#1- path , 2- filename , 3-extension
#2- uska pehla letter capital m aana chahiye
#3- extension ki sari files 1-2-3-4-5-6-......
def ring(path,filename,extension):
    import os
    os.chdir(path)
    path= (os.listdir())
    print(path)

    k=1
    for i in path:
        if(i.endswith(extension)):
            os.replace(i, str(k)+extension)
            k+=1
        else:
            continue

    os.replace(filename,filename.capitalize())

ring("D://kartik", "pen.bmp", ".txt")





