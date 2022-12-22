Print the following pattern
Pattern for N = 4

*000*000*
0*00*00*0
00*0*0*00
000***000

Input Format :
N (Total no. of rows)
Output Format :
Pattern in N lines

SOLUTION
=====================
from os import *
from sys import *
from collections import *
from math import *

n=int(input())
i=1
while(i<=n):
    j=1
    while(j<=n*2 + 1):
        if(j==i or j==(n+1) or j==(n*2)+2-i):
            print('*', end="")
        else:
            print('0', end="")
        j=j+1
    print()
    i=i+1
