def palindroms(word):
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - 1 - i]:
            return False
    return True

word = "kajak"

if palindroms(word) == True:
    print(f"The word {word} is a palindrome.")
else:
    print(f"The word {word} is not a palindrome.")

word_two = "hello"

if palindroms(word_two) == True:
    print(f"The word {word_two} is a palindrome.")
else:
    print(f"The word {word_two} is not a palindrome.")