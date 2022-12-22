Print the following pattern for the given N number of rows.
Pattern for N = 3
 A
 BB
 CCC
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines

SOLUTION
===========================
from os import *
from sys import *
from collections import *
from math import *

n=int(input())
i=1
while(i<=n):
    j=1
    while(j<=i):
        print(chr(ord('A') + i - 1), end="")
        j=j+1
    print()
    i=i+1
