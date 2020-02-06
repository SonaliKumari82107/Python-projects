import os

print(os.getcwd())


# r = os.listdir()
# print(r)
def first(path, ext, filename):
    r = os.chdir(path)
    r1 = os.listdir()
    j = 1
    for file in r1:
        if file.endswith(ext):
            os.rename(file, (str(j) + ".txt"))
            j = int(j + 1)
    if (filename in r1):
        r2 = filename.capitalize()
        os.replace(filename, r2)

    else:
        print("No such file is present")


first("D:\\kartik", ".txt", "ram.bmp")



