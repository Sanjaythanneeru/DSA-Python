Given two integers M & N, calculate and return their multiplication using recursion. You can only use subtraction and addition for your calculation. No other operators are allowed.
Input format :
Line 1 : Integer M
Line 2 : Integer N
Output format :
M x N
Constraints :
0 <= M <= 1000
0 <= N <= 1000

SOLUTION
====================================
from os import *
from sys import *
from collections import *
from math import *


from sys import setrecursionlimit
setrecursionlimit(10**6) 


def mulRecursive(m,n):
    if m>=0 and n>=0:
        if m==0 or n==0:
            return 0       
        smallOutput=mulRecursive(m,n-1)
        return m+smallOutput



m=int(input())
n=int(input())
print(mulRecursive(m,n))

