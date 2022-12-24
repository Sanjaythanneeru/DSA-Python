For a given two-dimensional integer array/list of size (N x M), you need to find out which row or column has the largest sum(sum of all the elements in a row/column) amongst all the rows and columns.
Note :
If there are more than one rows/columns with maximum sum, consider the row/column that comes first. And if ith row and jth column has the same largest sum, consider the ith row as answer.
Input Format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains two integer values, 'N' and 'M', separated by a single space. They represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.

Second line onwards, the next 'N' lines or rows represent the ith row values.

Each of the ith row constitutes 'M' column values separated by a single space.
Output Format :
For each test case, If row sum is maximum, then print: "row" <row_index> <row_sum>
OR
If column sum is maximum, then print: "column" <col_index> <col_sum>
It will be printed in a single line separated by a single space between each piece of information.

Output for every test case will be printed in a seperate line.
 Consider :
If there doesn't exist a sum at all then print "row 0 -2147483648", where -2147483648 or -2^31 is the smallest value for the range of Integer.
Constraints :
1 <= t <= 10^2
0 <= N <= 10^3
0 <= M <= 10^3
Time Limit: 1sec
  
 
SOLUTION
==========================================
from sys import stdin

def findLargest(arr, nRows, mCols):
    max_rowsum, max_colsum = -2147483648, -2147483648
    max_row, max_column = 0, 0
    if mCols!=0 and nRows!=0:
        #to find the row having max sum
        for i in range(nRows):
            temp=0
            for ele in arr[i]:
                temp+=ele
            if temp>max_rowsum:
                max_rowsum=temp
                max_row=i
        #to find the column having max sum
        for j  in range(mCols):
            temp=0
            for ele in arr:
                temp+=ele[j]
            if temp>max_colsum:
                max_colsum=temp
                max_column=j
		#to find if row or column having max sum
        if max_rowsum>=max_colsum:
            print("row" + " " + str(max_row)+ " " + str(max_rowsum))
        else:
            print("column" + " " + str(max_column)+ " " + str(max_colsum))
    else:
        print("row" + " " + str(max_row) + " " + str(max_rowsum))
        #Your code goes here




#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1
