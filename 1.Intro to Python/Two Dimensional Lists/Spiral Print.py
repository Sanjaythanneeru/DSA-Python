For a given two-dimensional integer array/list of size (N x M), print it in a spiral form. That is, you need to print in the order followed for every iteration:
a. First row(left to right)
b. Last column(top to bottom)
c. Last row(right to left)
d. First column(bottom to top)
 Mind that every element will be printed only once
  
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains two integer values, 'N' and 'M', separated by a single space. They represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.

Second line onwards, the next 'N' lines or rows represent the ith row values.

Each of the ith row constitutes 'M' column values separated by a single space.
Output format :
For each test case, print the elements of the two-dimensional array/list in the spiral form in a single line, separated by a single space.

Output for every test case will be printed in a seperate line.
Constraints :
1 <= t <= 10^2
0 <= N <= 10^3
0 <= M <= 10^3
Time Limit: 1sec
Sample Input 1:
1
4 4 
1 2 3 4 
5 6 7 8 
9 10 11 12 
13 14 15 16
Sample Output 1:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 


SOLUTION
=================================
from sys import stdin

def spiralPrint(mat, nRows, mCols):
    max=nRows*mCols
    k=1
    rs,re,cs,ce=0,nRows-1,0,mCols-1
    
    while(k<=max):
        ele=mat[rs]
        for i in range(cs,ce+1):
            print(ele[i], end=" ")
            k=k+1
        rs=rs+1
        if k>max:
            break
        for i in range(rs,re+1):
            j=mat[i]
            print(j[ce], end=" ")
            k=k+1
        ce=ce-1
        if k>max:
            break
        ele=mat[re]
        for i in range(ce,cs-1,-1):
            print(ele[i], end=" ")
            k=k+1
        re=re-1
        if k>max:
            break
        for i in range(re,rs-1,-1):
            j=mat[i]
            print(j[cs], end=" ")
            k=k+1
        cs=cs+1
