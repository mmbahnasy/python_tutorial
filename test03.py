
l = [1, 2, 3, 4]
d  = {"Orange": 2, "Apple": 3, "Banana": 4}

# for i in l:
#     print(i)

# print("end")

# for i in range(10):
#     print(i)


# for k, v in d.items():
#     print(k, v)


# for k in d.keys():
#     print(k, d[k])

# for v in d.values():
#     print(v)

s = {1, 2, 3, 3, 3, 4, 4, 5}
for itm in s:
    print(itm)


i = 0
while True:
    print(i)
    i = i + 1
    if i > 10:
        break
print("End While")


while True:
    n = input("Enter a number between 1 and 10:")
    n = int(n)
    if n < 1:
        print("This is a small number")
        continue
    if n > 10:
        print("This is too big.")
        continue
    print("This is a valid number")
    # Do calculation
    break

