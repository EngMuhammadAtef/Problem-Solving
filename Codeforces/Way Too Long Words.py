# Way Too Long Words
for i in range(int(input())):
    word = input()
    print(f"{word[0]}{len(word)-2}{word[-1]}") if len(word) > 10 else print(f"{word}")
