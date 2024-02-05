
from math import pi
from itertools import permutations

def sphere_volume(radius):
    return (4 / 3) * pi * radius**3

def print_permutations(input_string):
    all_permutations = permutations(input_string)
    for perm in all_permutations:
        print(''.join(perm))

def is_palindrome(word):
    cleaned_word = ''.join(word.split()).lower()
    return cleaned_word == cleaned_word[::-1]

def histogram(values):
    for value in values:
        print('*' * value)

def guess_the_number():
    import random

    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

# Example usage:
if __name__ == "__main__":
    print("Volume of a sphere with radius 3:", sphere_volume(3))

    print("Permutations of 'abc':")
    print_permutations("abc")

    print("Is 'madam' a palindrome?", is_palindrome("madam"))

    print("Histogram for values [4, 9, 7]:")
    histogram([4, 9, 7])

    print("Let's play the Guess the Number game:")
    guess_the_number()
