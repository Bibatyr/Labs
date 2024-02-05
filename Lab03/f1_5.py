from itertools import permutations

def print_permutation(input_string):
    all_permutations = permutations(input_string)

    for perm in all_permutations:
        print(''.join(perm))