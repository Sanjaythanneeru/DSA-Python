Print the following pattern for the given N number of rows.
Pattern for N = 4

   1
  12
 123
1234
The dots represent spaces.


Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines


SOLUTION
=============================
n=int(input())
i=1
while(i<=n):
    space = 1
    while(space<=n-i):
        print(' ', end="")
        space=space+1
    num=1
    while(num<=i):
        print(num, end="")
        num=num+1
    print()
    i=i+1
