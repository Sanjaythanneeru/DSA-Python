Print the following pattern for the given number of rows.
Pattern for N = 4
   1
  232
 34543
4567654
The dots represent spaces.



Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints :
0 <= N <= 50

SOLUTION
================================
from os import *
from sys import *
from collections import *
from math import *

n=int(input())
i=1
while(i<=n):
    #spaces
    space=1
    while(space<=n-i):
        print(' ', end="")
        space=space+1
    #increasing
    inc =i
    j=1
    while(j<=i):
        print(inc, end="")
        j=j+1
        inc=inc+1
    #decreasing
    dec = (i*2) - 2
    while(dec>=i):
        print(dec, end="")
        dec=dec-1
    print()
    i=i+1
