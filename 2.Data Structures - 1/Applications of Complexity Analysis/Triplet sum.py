You have been given a random integer array/list(ARR) and a number X. Find and return the triplet(s) in the array/list which sum to X.
Note :
Given array/list can contain duplicate elements.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the first array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.

Third line contains an integer 'X'.
Output format :
For each test case, print the total number of triplets present in the array/list.

Output for every test case will be printed in a separate line.
Constraints :
1 <= t <= 10^2
0 <= N <= 10^3
0 <= X <= 10^9

Time Limit: 1 sec
Sample Input 1:
1
7
1 2 3 4 5 6 7 
12
Sample Output 1:
5


SOLUTION
==================================================
from sys import stdin

def tripletSum(arr, n, num) :
    arr.sort()
    numtriplets=0
    for i in range(n):
        pairsumfor=num-arr[i]
        numpairs=pairsum(arr,(i+1),(n-1),pairsumfor)
        numtriplets += numpairs
    return numtriplets
def pairsum(arr,startindex,endindex,num):
    numpair=0
    while startindex<endindex:
        if arr[startindex]+arr[endindex]<num:
            startindex=startindex+1
        elif arr[startindex]+arr[endindex]>num:
            endindex=endindex-1
        else:
            elementatstart=arr[startindex]
            elementatend=arr[endindex]
            if elementatstart==elementatend:
                totalelementsfromstarttoend=(endindex-startindex)+1
                numpair=numpair+ (totalelementsfromstarttoend*(totalelementsfromstarttoend-1)//2)
                return numpair
            tempstartindex=startindex+1
            tempendindex=endindex-1
            while (tempstartindex <= tempendindex) and (arr[tempstartindex]==elementatstart):
                tempstartindex=tempstartindex+1
            while (tempendindex >= tempstartindex) and (arr[tempendindex]==elementatend):
                tempendindex=tempendindex-1
            totalelementsfromstart=(tempstartindex-startindex)
            totalelementsfromend=(endindex-tempendindex)
            numpair=numpair+(totalelementsfromstart*totalelementsfromend)
            startindex=tempstartindex
            endindex=tempendindex
    return numpair

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
    print(tripletSum(arr, n, num))

    t -= 1
