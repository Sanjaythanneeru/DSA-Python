Print the following pattern for the given N number of rows.
Pattern for N = 4
1
21
321
4321
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines

Solution:
  --------------
n=int(input())
i=1
while(i<=n):
    j=1
    k=i
    while(j<=i):
        print(k, end="")
        k = k - 1
        j = j + 1
    print()
    i = i + 1
