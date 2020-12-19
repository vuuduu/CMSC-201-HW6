"""
File:         matching_brackets.py
Author:       Vu Nguyen
Date:         3/11/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This programs return True when there are even number of
              bracket and False when there are uneven number of right
              or left bracket.
"""
EXIT_STRING = 'quit'
LEFT_BRACKET = '{'
RIGHT_BRACKET = '}'


def match_brackets(bracket_string, count=0):

    # THIS IS A BASE CASE
    if not bracket_string:
        if count != 0:
            return False
        else:
            return True

    # THIS IS A RECURSIVE CASE
    # this first condition checks for the left bracket
    elif bracket_string[0] == LEFT_BRACKET:
        return match_brackets(bracket_string[1:], count + 1)

    # this second condition checks for the right bracket
    elif bracket_string[0] == RIGHT_BRACKET:
        return match_brackets(bracket_string[1:], count - 1)

    # this third condition checks for non-bracket string
    else:
        return match_brackets(bracket_string[1:], count)


if __name__ == '__main__':
    user_string_input = input('Enter a string with brackets: ').strip()

    # This loop keeping asking for bracket until the user enter 'quit'
    while user_string_input.lower() != EXIT_STRING:
        print(match_brackets(user_string_input))
        user_string_input = input('Enter a string with brackets: ').strip()
