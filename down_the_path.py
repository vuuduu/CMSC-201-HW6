"""
File:         down_the_path.py
Author:       Vu Nguyen
Date:         11/3/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This program contain a recursive function that
              reset the count whenever the number is divisible
              by 15, 5, 3.
"""


def down_the_path(n):
    """
    :param n: an integer
    :return: the number of times that down the path runs
    """
    # THIS IS A BASE CASE
    if n <= 0:
        return 0

    # THESE ARE THE RECURSIVE CASE
    elif n % 15 == 0:
        return 1 + down_the_path(n / 15)
    elif n % 5 == 0:
        return 1 + down_the_path(n / 5)
    elif n % 3 == 0:
        return 1 + down_the_path(n / 3)
    else:
        return 1 + down_the_path(n - 1)


"""
THIS IS THE FUNCTION.
def count_down(count):
    if count <= 0:
        return 0
    else:
        return 1 + count_down(count - 1)
"""

if __name__ == '__main__':
    for i in range(20):
        print(i, down_the_path(i))
