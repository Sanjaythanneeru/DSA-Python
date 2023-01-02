For a given a string expression containing only round brackets or parentheses, check if they are balanced or not. Brackets are said to be balanced if the bracket which opens last, closes first.
Example:
Expression: (()())
Since all the opening brackets have their corresponding closing brackets, we say it is balanced and hence the output will be, 'true'.
You need to return a boolean value indicating whether the expression is balanced or not.
Note:
The input expression will not contain spaces in between.
Input Format:
The first and the only line of input contains a string expression without any spaces in between.
 Output Format:
The only line of output prints 'true' or 'false'.
Note:
You don't have to print anything explicitly. It has been taken care of. Just implement the function. 
Constraints:
1 <= N <= 10^7
 Where N is the length of the expression.

Time Limit: 1sec
Sample Input 1 :
(()()())
Sample Output 1 :
true

SOLUTION
===================================

from sys import stdin


def isBalanced(expression) :

	arr = []

	for i in expression:
		if i == '(':
			arr.append('(')
		elif i == ')':
			if len(arr) ==0:
				return False
			elif arr[len(arr) -1] == '(':
				arr.pop()
			else:
				return False 
	if len(arr) == 0:	
		return True 
	else:
		return False

#main
expression = stdin.readline().strip()

if isBalanced(expression) :
	print("true")

else :
	print("false")
