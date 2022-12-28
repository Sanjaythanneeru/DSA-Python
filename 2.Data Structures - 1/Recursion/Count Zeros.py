Given an integer N, count and return the number of zeros that are present in the given integer using recursion.
Input Format :
Integer N
Output Format :
Number of zeros in N
Constraints :
0 <= N <= 10^9


SOLUTION
==============================
from os import *
from sys import *
from collections import *
from math import *

def countZero(n):
    if n==0:
        return 1
    rem=n%10
    count=0
    if rem==0:
        count+=1
    if n//10==0:
        return 0
    return count+countZero(n//10)

n=int(input())
print(countZero(n))
