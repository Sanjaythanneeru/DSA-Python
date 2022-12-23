You have been given two sorted arrays/lists(ARR1 and ARR2) of size N and M respectively, merge them into a third array/list such that the third array is also sorted.
Input Format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the first array/list.

Second line contains 'N' single space separated integers representing the elements of the first array/list.

Third line contains an integer 'M' representing the size of the second array/list.

Fourth line contains 'M' single space separated integers representing the elements of the second array/list.
Output Format :
For each test case, print the sorted array/list(of size N + M) in a single row, separated by a single space.

Output for every test case will be printed in a separate line.
Constraints :
1 <= t <= 10^2
0 <= N <= 10^5
0 <= M <= 10^5
Time Limit: 1 sec 
  
SOLUTION
========================================
from sys import stdin

def merge(arr1, n, arr2, m) :
    i,j=0,0
    arr3=[]
    while (i<=n-1 and j<=m-1):
        if arr1[i]<arr2[j]:
            arr3.append(arr1[i])
            i=i+1
        else:
            arr3.append(arr2[j])
            j=j+1
    if i<=n-1:
        arr3.extend(arr1[i:])
    else:
        arr3.extend(arr2[j:])
    return arr3
