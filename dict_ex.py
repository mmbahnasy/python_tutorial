
str = input("Enter string:")
wordList = str.split(" ")

wordDict = {}

for word in wordList:
    # if word not in wordDict:
    #     wordDict[word] = 0
    # wordDict[word] += 1
    wordDict[word] = wordDict.get(word, 0) + 1

print(wordDict)