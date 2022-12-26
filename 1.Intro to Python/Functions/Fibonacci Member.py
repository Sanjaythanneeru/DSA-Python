Given a number N, figure out if it is a member of fibonacci series or not. Return true if the number is member of fibonacci series else false.
Fibonacci Series is defined by the recurrence
    F(n) = F(n-1) + F(n-2)
where F(0) = 0 and F(1) = 1


Input Format :
Integer N
Output Format :
true or false
Constraints :
0 <= n <= 10^4


SOLUTION
====================================
def checkMember(n):
    a=0
    b=1
    if n==0:
        return True 
    for i in range(0,n*2):
        c=a+b
        a=b
        b=c
        if c==n:
            return True
    else:
        return False

n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")
