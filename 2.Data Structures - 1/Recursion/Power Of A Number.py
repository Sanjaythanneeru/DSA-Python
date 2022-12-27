Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to print the answer.
Note : For this question, you can assume that 0 raised to the power of 0 is 1


Input format :
Two integers x and n (separated by space)
Output Format :
x^n (i.e. x raise to the power n)
Constraints:
0 <= x <= 8 
0 <= n <= 9

SOLUTION
==============================
x, n=input().split()
x=int(x)
n=int(n)

def power(x,n):
    if n==0:
        return 1
    return x*(power(x,n-1))

print(power(x,n))
