
#!/usr/bin/python3

while True:
    str = input(">>")
    if str == "q" or str == "quit":
        exit()
    str = str.replace(" ", "")
    str = str.replace("+", " + ")
    str = str.replace("-", " - ")
    str = str.replace("*", " * ")
    str = str.replace("/", " / ")
    # print(str)
    strTockens = str.split(" ")
    # print(strTockens)
    while len(strTockens) > 1:
        op = strTockens[1]
        if op =='+':
            tmp = int(strTockens[0]) + int(strTockens[2])
        elif op =='-':
            tmp = int(strTockens[0]) - int(strTockens[2])
        elif op =='*':
            tmp = int(strTockens[0]) * int(strTockens[2])
        elif op =='/':
            tmp = int(strTockens[0]) / int(strTockens[2])
        del strTockens[2]
        del strTockens[1]
        strTockens[0] = tmp
        # print(strTockens)
    print(strTockens[0])

