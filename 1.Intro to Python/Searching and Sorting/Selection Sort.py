Provided with a random integer array/list(ARR) of size N, you have been required to sort this array using 'Selection Sort'.
 Note:
Change in the input array/list itself. You don't need to return or print the elements.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.
Output format :
For each test case, print the elements of the array/list in sorted order separated by a single space.

Output for every test case will be printed in a separate line.
Constraints :
1 <= t <= 10^2
0 <= N <= 10^3
Time Limit: 1 sec
  
SOLUTION
=====================================================
from sys import stdin

def selectionSort(arr, n) :
    if n!=0: 
        for i in range(0,n):
            min =i
            for j in range(i+1, n):
                if arr[j]<arr[min]:
                    arr[min], arr[j] = arr[j], arr[min]
