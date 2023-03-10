Check whether a given String S is a palindrome using recursion. Return true or false.
Input Format :
String S
Output Format :
'true' or 'false'
Constraints :
0 <= |S| <= 1000
where |S| represents length of string S.

SOLUTION
======================================
from os import *
from sys import *
from collections import *
from math import *


def palindrome(string):
    if len(string)==1:
        return string
    smallerStr=palindrome(string[1:])
    return smallerStr+string[0]

string=input()
if(palindrome(string)==string):
    print("true")
else:
    print("false")
