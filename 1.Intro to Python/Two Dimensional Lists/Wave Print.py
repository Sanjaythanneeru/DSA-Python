For a given two-dimensional integer array/list of size (N x M), print the array/list in a sine wave order, i.e, print the first column top to bottom, next column bottom to top and so on.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains two integer values, 'N' and 'M', separated by a single space. They represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.

Second line onwards, the next 'N' lines or rows represent the ith row values.

Each of the ith row constitutes 'M' column values separated by a single space.
Output format :
For each test case, print the elements of the two-dimensional array/list in the sine wave order in a single line, separated by a single space.

Output for every test case will be printed in a seperate line.
Constraints :
1 <= t <= 10^2
0 <= N <= 10^3
0 <= M <= 10^3
Time Limit: 1sec
  
  
SOLUTION
=============================
from sys import stdin

def wavePrint(mat, nRows, mCols):
    j=0
    k=True
    while(j<mCols):
        if k:
            for i in mat:
                print(i[j], end=" ")
            j+=1
            k=False
        else:
            for i in mat[-1::-1]:
                print(i[j], end=" ")
            j+=1
            k=True
    
