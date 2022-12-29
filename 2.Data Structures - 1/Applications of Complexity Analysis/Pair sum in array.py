You have been given an integer array/list(ARR) and a number 'num'. Find and return the total number of pairs in the array/list which sum to 'num'.
Note:
Given array/list can contain duplicate elements. 
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the first array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.

Third line contains an integer 'num'.
Output format :
For each test case, print the total number of pairs present in the array/list.

Output for every test case will be printed in a separate line.
Constraints :
1 <= t <= 10^2
0 <= N <= 10^4
0 <= num <= 10^9

Time Limit: 1 sec
Sample Input 1:
1
9
1 3 6 2 5 4 3 2 4
7
Sample Output 1:
7

SOLUTION
================================================
from sys import stdin

def pairSum(arr, n, num) :
    ans=0
    arr.sort()
    i=0
    j=n-1
    while (i<j):
        if(arr[i]+arr[j]<num):
            i=i+1
        elif(arr[i]+arr[j]>num):
            j=j-1
        else:
            initialLeftElement=arr[i]
            initialLeftIndex=i
            while(i<j and arr[i]==initialLeftElement):
                i=i+1
            initialRightElement=arr[j]
            initialRightIndex=j
            while(j>=i and arr[j]==initialRightElement):
                j=j-1
            if(initialLeftElement==initialRightElement):
                equalnumbers=(i-initialLeftIndex)+(initialRightIndex-j)-1
                ans=ans+(equalnumbers*(equalnumbers+1))//2
            else:
                ans=ans+((i-initialLeftIndex)*(initialRightIndex-j))
    return ans

#taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    num = int(stdin.readline().strip())
    print(pairSum(arr, n, num))

    t -= 1
