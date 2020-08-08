#!/bin/python3

#
# Title: Python If-Else
# URL: https://www.hackerrank.com/challenges/py-if-else/problem
# 

import math
import os
import random
import re
import sys

def weird_or_not_weird(n):
    if n % 2 == 1:
        return 'Weird'
    elif n in list(range(2,6)):
        return 'Not Weird'
    elif n in list(range(6,21)):
        return 'Weird'
    return 'Not Weird'


if __name__ == '__main__':
    n = int(input().strip())
    print(weird_or_not_weird(n))
