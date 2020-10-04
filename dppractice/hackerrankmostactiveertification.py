#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'mostActive' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY customers as parameter.
#

def mostActive(customers):
    dict1=dict()
    for i in customers:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    f=customers_count*(0.05)
    kl=[]
    for i in sorted(dict1.items(), key = lambda kv:(kv[1], kv[0]))[::-1]:
        if i[1]>=f:
            kl.append(i[0])
        else:
            break
    return sorted(kl)
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    customers_count = int(input().strip())

    customers = []

    for _ in range(customers_count):
        customers_item = input()
        customers.append(customers_item)

    result = mostActive(customers)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
