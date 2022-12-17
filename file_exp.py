
import os

# open(FilePath, 'r/w/a/x/b')

try:
    print("*"*10 + " Opening the file " + "*"*10)
    fd = open("textfile.txt", 'r') # w: write, a: append, x: exlusive open, t: text (default), b: binary
    str = fd.read()
    print(str)
except:
    pass
finally:
    print("*"*10 + " Closing the file " + "*"*10)
    fd.close()


with open("textfile.txt", 'r') as fd:
    fd.seek(100)
    # for line in fd.readlines:
    while True:
        line = fd.readline()
        if line == '': break
        print("cursor at:", fd.tell())
        print(line)
    fd.close()


# with open("file2.txt", 'w') as fd:
#     fd.writelines(["sss\n", "gggg", "ffff"])
#     fd.close()


print(os.getcwd())
# os.rename("textfile.txt", "textfile2.txt")
fileList = os.listdir("./")
# os.chdir("string_func")
os.mkdir("backup")
for file in fileList:
    if file.endswith(".py"):
        with open(file, 'rb') as infile:
            with open("backup/"+file, 'wb') as outfile:
                outfile.write(infile.read())
