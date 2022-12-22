Print the following pattern for the given number of rows.
Assume N is always odd.
Note : There is space after every star.
Pattern for N = 7
*
 * *
   * * *
     * * * *
   * * *
 * *
*
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines

SOLUTION
===========================
n=int(input())
i=1
while(i<=n//2+1):
    space=1
    while(space<=i-1):
        print(" ", end="")
        space=space+1
    star=1
    while(star<=i):
        print("*", end="")
        star=star+1
        print(' ', end="")
    print()
    i=i+1
j=1
while(j<=n//2):
    space=1
    while(space<=n//2-j):
        print(" ", end="")
        space=space+1
    star=1
    while(star<=n//2+1-j):
        print("*", end="")
        star=star+1
        print(" ", end="");
    print()
    j=j+1
