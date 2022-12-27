Sort an array A using Quick Sort.
Change in the input array itself. So no need to return or print anything.


Input format :
Line 1 : Integer n i.e. Array size
Line 2 : Array elements (separated by space)
Output format :
Array elements in increasing order (separated by space)
Constraints :
1 <= n <= 10^3

SOLUTION
============================
def partition(arr, start, end):
    if start>=end:
        return
    k=arr[start]
    count=0
    for i in range(start,end):
        if arr[i]<k:
            count+=1
    arr[start],arr[start+count]=arr[start+count],arr[start]
    i,j=start,end-1
    while(i<(start+count) and j>(start+count)):
        while(i<(start+count) and arr[i]<arr[start+count]):
            i+=1
        while(j>(start+count) and arr[j]>=arr[start+count]):
            j-=1
        
        arr[i],arr[j]=arr[j],arr[i]
    return start+count


def quickSort(arr, start, end):
    if start>=end:
        return
    index=partition(arr, start, end)
    
    quickSort(arr, start, index)
    quickSort(arr, index+1, end)


n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n)
print(*arr)
