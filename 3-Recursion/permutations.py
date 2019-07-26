"""
permutations of a string with unique characters

Approach 1:
          permutation(S) = first_char + permutations(S[1:])
                           now add first char at every possible index in the string received from recursive calls
                           Example:
                                permuatations("cat") = c + permurations("at")
                                                           perumtations("at") = a + permurations("t")
                                                                                    returns t (base case)
                                                                                return (at, ta) (by putting at at every possible index)
                                                        returns
                                                        cat, act, atc (by putting c at every index of at)
                                                        cta, tca, tac (by putting c at every index of ta)




Approach 2: Similar to approach 1 but implemented differently
            State (current_idx, str_so_far) -> current_idx in the string and which combination of the string is chosen so far called str_so_far
            Transition -> insert char at current_idx at all possible locations in the str_so_far and recursively call for new str_so_far


            As an example, for string 'taco' -> let say we have chosen 'ta' and we are at 'c', so we'll add 'c' at each index in 'ta' and call it recursively
            permurations('cta'), permurations('tca'), permutations('tac') each of this call will do the same thing with char 'o'


Approach 3: Pick one character and put it at every possible index, try doing it recursively

            for string 'taco', we have characters 't', 'a', 'c', 'o'
            we first picked 't' which can be placed as 't' _ _ _ or _ 't' _ _ or _ _ 't' _ or _ _ _ 't'
            we then call it recursivly on each of these combination with remaining characters in the bag

            Now let's cal the same function on first string permutations('t _ _ _') and remaining chars ('a', 'c', 'o')
            possible options are 't' 'a' _ _ or 't' _ 'a' _ or 't' _ _ 'a' and call recursively on each of these

            State (remaining_characters, str_so_far) -> remaining characters in the bag and which combination of the string is chosen so far
            Transition -> pick one of the remaining character and put at every empty location


Approach 4: Bag of characters

            for string 'taco', we have characters 't', 'a', 'c', 'o'
            We can choose each character in first try 't', 'a', 'c', 'o'
            once a character is taken, we can only pick from remaining characters, if we picked 't', we can only pick from 'a', 'c', 'o'

            State(remaining_chars, str_so_far)
            Transition -> pick one character from remaining characters in the bag and call recursively
"""

import random
import string
import itertools


def __permurations_4(s, current_idx, str_so_far, taken, result):

    if current_idx == len(s):
        result.append(str_so_far[:])
        return

    for idx in range(len(s)):
        if not taken[idx]:
            char = s[idx]
            taken[idx] = True
            str_so_far.append(char)
            __permurations_4(s, current_idx+1, str_so_far, taken, result)
            taken[idx] = False
            str_so_far.remove(char)

    return

def permutations_4(s):
    result = []
    str_so_far = []
    taken = [False] * len(s)
    __permurations_4(s, 0, str_so_far, taken, result)
    return result

def __permutations_3(s, current_idx, str_so_far, result):
    if current_idx == len(s):
        result.append(str_so_far[:])

    for idx in range(len(s)):
        if not str_so_far[idx]:
            str_so_far[idx] = s[current_idx]
            __permutations_3(s, current_idx + 1, str_so_far, result)
            str_so_far[idx] = None


def permutations_3(s):
    result = []
    str_so_far = [None] * len(s)
    __permutations_3(s, 0, str_so_far, result)
    return result

def __permutations_2(s, current_idx, str_so_far, result):
    if current_idx == len(s):
        result.append(str_so_far[:])
        return

    for idx in range(len(str_so_far) + 1):
        current_char = s[current_idx]
        str_so_far.insert(idx, current_char)
        __permutations_2(s, current_idx + 1, str_so_far, result)
        str_so_far.remove(current_char)

    return

def permutations_2(s):
    result = []
    __permutations_2(s, 0, [], result)
    return result


def permutations_1(s):
    if len(s) == 1:
        return [[s]]

    first_char = s[0]
    remaining_permutations = permutations_1(s[1:])
    # put first_char at every possible index of remaining permutations
    result = []
    for perm in remaining_permutations:
        for idx in range(len(perm) + 1):
            new_perm = perm[:]
            new_perm.insert(idx, first_char)
            result.append(new_perm)
    return result

def random_str(length=5):
    # return "taco"
    letters = string.ascii_lowercase
    return ''.join(set(random.choice(letters) for i in range(length)))

def main():
    s = random_str()
    expected = [list(perm) for perm in itertools.permutations(s)]
    actual_1 = permutations_1(s)
    assert sorted(expected) == sorted(actual_1)

    actual_2 = permutations_2(s)
    assert sorted(expected) == sorted(actual_2)

    actual_3 = permutations_3(s)
    assert sorted(expected) == sorted(actual_3)

    actual_4 = permutations_4(s)
    assert sorted(expected) == sorted(actual_4)


if __name__ == '__main__':
    main()