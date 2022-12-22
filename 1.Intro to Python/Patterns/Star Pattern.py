Print the following pattern
Pattern for N = 4
   *
  ***
 *****
*******
The dots represent spaces.



Input Format :
N (Total no. of rows)
Output Format :
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
    space=1
    while(space<=n-i):
        print(' ', end="")
        space=space+1
    increasing=1
    while(increasing<=i):
        print('*', end="")
        increasing= increasing+1
    decreasing= i-1
    while(decreasing>=1):
        print('*', end="")
        decreasing=decreasing-1
    print()
    i=i+1
