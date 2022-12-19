Print the following pattern for the given N number of rows.
Pattern for N = 4
*
**
***
****
Note : There are no spaces between the stars (*).
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines

Solution:
=============================
n = int(input())
i=1
while(i<=n):
    j=1
    while(j<=i):
        print("*", end="")
        j=j+1
    print()
    i=i+1
