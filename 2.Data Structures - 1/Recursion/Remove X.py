Given a string, compute recursively a new string where all 'x' chars have been removed.
Input format :
String S
Output format :
Modified String
Constraints :
1 <= |S| <= 10^3
where |S| represents the length of string S. 


SOLUTION
=======================================
def removeX(string): 
    if len(string)==0:
        return string
    smallerString=removeX(string[1:])
    if string[0]=='x':
        return smallerString
    else:
        return string[0]+smallerString


# Main
string = input()
print(removeX(string))
