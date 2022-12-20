Print the following pattern for the given N number of rows.
Pattern for N = 4
A
BC
CDE
DEFG
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines

Solution:
  ------------
n=int(input())
i=1
while(i<=n):
    j=1
    startC = chr(ord('A') + i - 1)
    while(j<=i):
        charP = chr(ord(startC) + j - 1)
        print(charP, end="")
        j=j+1
    print()
    i=i+1
