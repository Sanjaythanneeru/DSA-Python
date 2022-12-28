Suppose you have a string, S, made up of only 'a's and 'b's. Write a recursive function that checks if the string was generated using the following rules:
a. The string begins with an 'a'
b. Each 'a' is followed by nothing or an 'a' or "bb"
c. Each "bb" is followed by nothing or an 'a'
If all the rules are followed by the given string, return true otherwise return false.
Input format :
String S
Output format :
'true' or 'false'
Constraints :
1 <= |S| <= 1000
where |S| represents length of string S.


SOLUTION
==========================================
from os import *
from sys import *
from collections import *
from math import *

def check_ab(str):
    if (len(str)==0):
        return True
    if (str[0] == 'a'):
        if (len(str[1:])>1 and str[1:3] == 'bb'):
            return check_ab(str[3:])
        else:
            return check_ab(str[1:])
    else:
        return False
    

str = input()
if (check_ab(str)):
    print("true")
else:
    print("false")
    
    
 
