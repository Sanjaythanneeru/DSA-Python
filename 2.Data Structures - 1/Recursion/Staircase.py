A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up to the stairs. You need to return number of possible ways W.
Input format :
Integer N
Output Format :
Integer W
Constraints :
1 <= N <= 30

SOLUTION
==============================
from os import *
from sys import *
from collections import *
from math import *

def stairCase(n):
    if n<0:
        return 0
    if n==0 or n==1:
        return 1
    x=stairCase(n-1)
    y=stairCase(n-2)
    z=stairCase(n-3)
    
    return x+y+z

n=int(input())
print(stairCase(n))
