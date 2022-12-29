Given an integer array A of size N, check if the input array can be splitted in two parts such that -
- Sum of both parts is equal
- All elements in the input, which are divisible by 5 should be in same group.
- All elements in the input, which are divisible by 3 (but not divisible by 5) should be in other group.
- Elements which are neither divisible by 5 nor by 3, can be put in any group.
Groups can be made with any set of elements, i.e. elements need not to be continuous. And you need to consider each and every element of input array in some group.
Return true, if array can be split according to the above rules, else return false.
Note : You will get marks only if all the test cases are passed.
Input Format :
Line 1 : Integer N (size of array)
Line 2 : Array A elements (separated by space)
Output Format :
true or false
Constraints :
1 <= N <= 50
Sample Input 1 :
2
1 2
Sample Output 1 :
false

SOLUTION
===============================================
def split(arr,start,end,arrSum1,arrSum2):
    if start>end:
        return arrSum1==arrSum2
    if arr[start]%5==0:
        return split(arr,start+1,end,arrSum1+arr[start],arrSum2)
    elif arr[start]%3==0:
        return split(arr,start+1,end,arrSum1,arrSum2+arr[start])
    else:
        return split(arr,start+1,end,arrSum1+arr[start],arrSum2) or split(arr,start+1,end,arrSum1,arrSum2+arr[start])

        
n = int(input())
arr = [int(ele) for ele in input().split()]
ans = split(arr,0,n-1,0,0)
if ans is True:
    print('true')
else:
    print('false')
