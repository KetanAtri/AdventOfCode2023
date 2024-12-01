file = open('input.txt', 'r')
lines = file.readlines()
total = 0
for line in lines:
    firstDigit = 0
    secondDigit = 0
    for letter in line:
        if (letter.isdigit()):
            firstDigit = int(letter)
            break
    for letter in reversed(line):
        if (letter.isdigit()):
            secondDigit = int(letter)
            break
    total += (firstDigit * 10 + secondDigit)
print(total)
    