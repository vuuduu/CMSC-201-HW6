"""
File:         the_third_degree.py
Author:       Vu Nguyen
Date:         10/31/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  A recursive function that takes in n as an argument
              and return the n^th term in the sequence.
"""


def the_third_degree(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n == 2:
        return 5
    else:
        # This equation follow the formula by adding/multiply the previous sum to the 3, 2, [last value].
        sum_of_sequence = (3 * the_third_degree(n-1)) + (2 * the_third_degree(n - 2)) + the_third_degree(n - 3)
        return sum_of_sequence


if __name__ == '__main__':
    for i in range(10):
        print(the_third_degree(i))
