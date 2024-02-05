def is_palindrome(word):
    cleaned_word = ''.join(word.split()).lower()

    return cleaned_word == cleaned_word[::-1]