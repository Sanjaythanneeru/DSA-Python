Note: each line consist of equal number of characters + spaces. Suppose you are printing xth line for N=n. You need to print 1..x followed by (n-x) spaces, again (n-x) spaces followed by x..1
For eg. N = 5

1        1
12      21
123    321
1234  4321
1234554321


SOLUTION
===================
n=int(input())
i=1
while(i<=n):
    k=1
    l=1
    while(k<=i):
        print(l, end="")
        k=k+1
        l=l+1
    space=1
    while(space<=(n*2)-(i*2)):
        print(" ", end="")
        space=space+1
    h=i
    while(h>=1):
        print(h, end="")
        h=h-1
    print()
    i=i+1
