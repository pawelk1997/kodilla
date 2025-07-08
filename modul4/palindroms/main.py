def palindroms(word):
    """
    Checks if the given word is a palindrome.

    Arguments:
    word: The string to be checked.

    Returns:
    True: If the word is a palindrome (reads the same forwards and backward).
    False: If the word is not a palindrome.
    """
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