Print the following pattern for the given number of rows.
Pattern for N = 5
E
DE
CDE
BCDE
ABCDE
Input format :
N (Total no. of rows)
Output format :
Pattern in N lines

solutin:
  ---------------
from os import *
from sys import *
from collections import *
from math import *

n = int(input())
i=1
while(i<=n):
    j=1
    startC = chr(ord('A')+ n - i)
    while(j<=i):
        print(chr(ord(startC)+ j - 1), end="")
        j=j+1
    print()
    i= i + 1
        
