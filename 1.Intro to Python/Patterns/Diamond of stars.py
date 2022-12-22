Print the following pattern for the given number of rows.
Note: N is always odd.


Pattern for N = 5



The dots represent spaces.



Input format :
N (Total no. of rows and can only be odd)
Output format :
Pattern in N lines
Constraints :
1 <= N <= 49

SOLUTION
================================================
from os import *
from sys import *
from collections import *
from math import *

n=int(input())
i=1
while(i<=n//2 +1):
    #decreasing spaces
    sp = 1
    while(sp <= (n//2)-i +1):
        print(' ', end="")
        sp=sp+1
    #increasing star
    p=1
    while(p<=i):
        print('*', end="")
        p=p+1
    k=1
    while(k<=i-1):
        print('*', end="")
        k=k+1
    print()
    i=i+1
j=1
while(j<=n//2):
    sp = 1
    while(sp<=j):
        print(' ', end="")
        sp=sp+1
    p=1
    while(p<=(n//2)-j+1):
        print('*', end="")
        p=p+1
    k=1
    while(k<=(n//2)-j):
        print('*', end="")
        k=k+1
    print()
    j=j+1
    
    
