l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l2 = [[12, 23, 45], [45, 23, -1], [2, 3, 4]]

res = []
for rowIndex in range(len(l1)):
    res.append([])
    for colIndex in range(len(l1[0])):
        s = l1[rowIndex][colIndex] + l2[rowIndex][colIndex]
        res[rowIndex].append(s)

print(res)
