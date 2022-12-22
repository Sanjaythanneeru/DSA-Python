Print the following pattern for the given number of rows.
Pattern for N = 4
   1
  212
 32123
4321234
Input format : N (Total no. of rows)

Output format : Pattern in N lines
  
SOLUTION
==============================
from os import *
from sys import *
from collections import *
from math import *

n=int(input())
i=1
while(i<=n):
    space=1
    while(space<=n-i):
        print(' ', end="")
        space=space+1
    p=i
    while(p>=1):
        print(p, end="")
        p=p-1
    j=1
    k=2
    while(j<=i-1):
        print(k, end="")
        k=k+1
        j=j+1
    print()
    i=i+1
