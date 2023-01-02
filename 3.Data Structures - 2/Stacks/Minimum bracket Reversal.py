For a given expression in the form of a string, find the minimum number of brackets that can be reversed in order to make the expression balanced. The expression will only contain curly brackets.
If the expression can't be balanced, return -1.
Example:
Expression: {{{{
If we reverse the second and the fourth opening brackets, the whole expression will get balanced. Since we have to reverse two brackets to make the expression balanced, the expected output will be 2.

Expression: {{{
In this example, even if we reverse the last opening bracket, we would be left with the first opening bracket and hence will not be able to make the expression balanced and the output will be -1.
Input Format :
The first and the only line of input contains a string expression, without any spaces in between.
Output Format :
The only line of output will print the number of reversals required to balance the whole expression. Prints -1, otherwise.
Note:
You don't have to print anything. It has already been taken care of.
Constraints:
0 <= N <= 10^6
Where N is the length of the expression.

Time Limit: 1sec
Sample Input 1:
{{{
Sample Output 1:
-1
  
  
SOLUTION
************************************************************************************
  
from sys import stdin

def countBracketReversals(inputString) :
    if len(inputString)%2!=0:
        return -1
    temp =[]
    for i in inputString:
        if i == '{':
             temp.append(i)
        else:
            if len(temp)>0:
                if temp[-1]=='{':
                    temp.pop()
                else:
                    temp.append(i)
            else:
                temp.append(i)
    c = 0
    for i in range(len(temp)-1,-1,-2):
        if temp[i]==temp[i-1]:
            c+=1
        else:
            c+=2
    return c



#main
print(countBracketReversals(stdin.readline().strip()))
