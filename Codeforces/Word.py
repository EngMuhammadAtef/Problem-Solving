# Word
word = input()
up_word = word.upper()
countupper, countlower = 0, 0

for i in range(len(word)):
    if word[i] == up_word[i]:
        countupper += 1
    else:
        countlower += 1
if countupper > countlower:
    print(word.upper())
else:
    print(word.lower())