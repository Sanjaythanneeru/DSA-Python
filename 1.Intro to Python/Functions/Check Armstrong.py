Write a Program to determine if the given number is Armstrong number or not. Print true if number is armstrong, otherwise print false.
An Armstrong number is a number (with digits n) such that the sum of its digits raised to nth power is equal to the number itself.
For example,
371, as 3^3 + 7^3 + 1^3 = 371
1634, as 1^4 + 6^4 + 3^4 + 4^4 = 1634
Input Format :
Integer n
Output Format :
true or false

SOLUTION
====================================
from os import *
from sys import *
from collections import *
from math import *

def count(num):
    count=0
    while(num!=0):
        count=count+1
        num=num//10
    return count
def isPalindrome(num):
    k=count(num)
    temp=num
    sum=0
    while(num!=0):
        rem=num%10
        sum=sum+(rem**k)
        num=num//10
    if sum==temp:
        return True
    else:
        return False

    

n=int(input())
isPal= isPalindrome(n)
if isPal:
    print("true")
else:
    print("false")
    
    
    
