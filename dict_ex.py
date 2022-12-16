
str = input("Enter String>>")
wordList = str.split(" ")

wordDict = {} # Key is the word: value number of repetition
for word in wordList:
    # if word not in wordDict:
    #     wordDict[word] = 0
    # wordDict[word] += 1
    wordDict[word] = wordDict.get(word, 0) + 1

print(wordDict)
