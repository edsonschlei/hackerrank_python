#!/bin/python3

#
# Title: Python If-Else
# URL: https://www.hackerrank.com/challenges/py-if-else/problem
# 

from py_if_else import  weird_or_not_weird

if __name__ == '__main__':
    # n = int(input().strip())
    # print(weird_or_not_weird(n))

    # If  is odd, print Weird
    assert weird_or_not_weird(1) == 'Weird'

    # If  is even and in the inclusive range of  to , print Not Weird
    assert weird_or_not_weird(2) == 'Not Weird'
    assert weird_or_not_weird(4) == 'Not Weird'

    # If  is even and in the inclusive range of  to , print Weird
    assert weird_or_not_weird(6) == 'Weird'
    assert weird_or_not_weird(20) == 'Weird'

    # If  is even and greater than , print Not Weird
    assert weird_or_not_weird(22) == 'Not Weird'

