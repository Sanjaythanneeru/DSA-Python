Two random integer arrays/lists have been given as ARR1 and ARR2 of size N and M respectively. Both the arrays/lists contain numbers from 0 to 9(i.e. single digit integer is present at every index). The idea here is to represent each array/list as an integer in itself of digits N and M.
You need to find the sum of both the input arrays/list treating them as two integers and put the result in another array/list i.e. output array/list will also contain only single digit at every index.
Note:
The sizes N and M can be different. 

Output array/list(of all 0s) has been provided as a function argument. Its size will always be one more than the size of the bigger array/list. Place 0 at the 0th index if there is no carry. 

No need to print the elements of the output array/list.
Using the function "sumOfTwoArrays", write the solution to the problem and store the answer inside this output array/list. The main code will handle the printing of the output on its own.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the first array/list.

Second line contains 'N' single space separated integers representing the elements of the first array/list.

Third line contains an integer 'M' representing the size of the second array/list.

Fourth line contains 'M' single space separated integers representing the elements of the second array/list.
Output Format :
For each test case, print the required sum of the arrays/list in a row, separated by a single space.

Output for every test case will be printed in a separate line.
Constraints :
1 <= t <= 10^2
0 <= N <= 10^5
0 <= M <= 10^5
Time Limit: 1 sec 
  
  
SOLUTION
=====================================================
from sys import stdin

def sumOfTwoArrays(arr1, n, arr2, m, output) :
    if n>m:
        for i in range(n-m):
            arr2.insert(0,0)
    elif m>n:
        for i in range(m-n):
            arr1.insert(0,0)
    carry=0
    for i in range(len(arr1)-1,-1,-1):
        if arr1[i]+arr2[i]+carry >= 10:
            output.insert(0,(arr1[i]+arr2[i]+carry)%10)
            carry=1
        else:
            output.insert(0, arr1[i]+arr2[i]+carry)
            carry=0
    if carry==1:
        output.insert(0,1)
    else:
        output.insert(0,0)
