Print the following pattern for the given N number of rows.
Pattern for N = 4
1
11
202
3003
Input format :
Integer N (Total no. of rows)
Constraints:
1 <= n <= 50
Output format :
Pattern in N lines

SOLUTION:
-------------------------
from os import *
from sys import *
from collections import *
from math import *

n= int(input())
i=1
while(i<=n):
    j=1
    while(j<=i):
        if i==1 and j==1:
            print("1", end= "")
        else:
            if j==1 or i==j:
                print(i - 1, end= "")
            else:
                print("0", end="")
        j=j+1
    print()
    i=i+1
