Print the following pattern for the given N number of rows.
Pattern for N = 4
1234
123
12
1
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines

SOLUTION
=============================
from os import *
from sys import *
from collections import *
from math import *

n=int(input())
i=n
while(i>0):
    j=1
    while(j<=i):
        print(j, end="")
        j=j+1
    print()
    i=i-1
