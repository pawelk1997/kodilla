def palindroms(word):
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - 1 - i]:
            return False
    return True

word = "kajak"

if palindroms(word) == True:
    print("Słowo jest palindromem")
else:
    print("Słowo nie jest palindromem")