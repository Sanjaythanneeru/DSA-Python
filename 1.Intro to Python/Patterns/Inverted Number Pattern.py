Print the following pattern for the given N number of rows.
Pattern for N = 4
4444
333
22
1
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines


SOLUTION
===================================
n=int(input())
i=1
while(i<=n):
    j=1
    while(j<=n-i+1):
        print(n-i+1, end="")
        j=j+1
    print()
    i=i+1
