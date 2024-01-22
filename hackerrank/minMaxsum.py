#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    max_val = max(arr)
    min_val = min(arr)
    total = sum(arr)
    print(total- max_val, total - min_val)



 




if __name__ == "__main__":

    arr = [1, 2, 3, 4, 5]

    miniMaxSum(arr)