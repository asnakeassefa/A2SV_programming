#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    length = len(a)
    count = 0
    for rowidx in range(length):
        for colidx in range(length - 1):
            if a[colidx] > a[colidx + 1]:
                count += 1
                a[colidx],a[colidx + 1] = a[colidx + 1],a[colidx]
    print(f"Array is sorted in {count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
