Given k, find the geometric sum i.e.
1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k) 
using recursion.
Input format :
Integer k
Output format :
Geometric sum (upto 5 decimal places)
Constraints :
0 <= k <= 1000


SOLUTION
=======================================
from os import *
from sys import *
from collections import *
from math import *

def geometricSum(n):
    if n==0:
        return 1
    k=1/(2**n)
    return k+geometricSum(n-1)

n=int(input())
print("{:.5f}".format(geometricSum(n)))
