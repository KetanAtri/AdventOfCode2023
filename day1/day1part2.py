words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def getFirstAndLast(line, searchFor):
    gFirstIndex = 1000
    gLastIndex = -1
    leftDigit = 0
    rightDigit = 0
    isWord = True if searchFor[0] == 'one' else False
    for x in searchFor:
        firstIndex = line.find(x)
        if (firstIndex != -1 and firstIndex < gFirstIndex):
            gFirstIndex = firstIndex
            leftDigit = int(nums[words.index(x)]) if isWord else int(x)
        lastIndex = line.rfind(x)
        if (lastIndex > gLastIndex):
            gLastIndex = lastIndex
            rightDigit = int(nums[words.index(x)]) if isWord else int(x)
    return gFirstIndex, gLastIndex, leftDigit, rightDigit

file = open('input.txt', 'r')
lines = file.readlines()
total = 0
for line in lines:
    wordFirstIndex, wordLastIndex, firstWord, lastWord = getFirstAndLast(line, words)
    numFirstIndex, numLastIndex, firstNum, lastNum = getFirstAndLast(line, nums)
    leftDigit = firstWord if wordFirstIndex < numFirstIndex else firstNum
    rightDigit = lastWord if wordLastIndex > numLastIndex else lastNum
    total += (leftDigit * 10 + rightDigit)
print(total)