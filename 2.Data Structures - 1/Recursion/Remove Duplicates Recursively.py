Given a string S, remove consecutive duplicates from it recursively.
Input Format :
String S
Output Format :
Output string
Constraints :
1 <= |S| <= 10^3
where |S| represents the length of string

SOLUTION
===================================
def removeConsecutiveDuplicates(string):
    if len(string)==0 or len(string)==1:
        return string
    smallerStringOutput=removeConsecutiveDuplicates(string[1:])
    if string[0]==smallerStringOutput[0]:
        return string[0]+smallerStringOutput[1:]
    else:
        return string[0]+smallerStringOutput
        

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
