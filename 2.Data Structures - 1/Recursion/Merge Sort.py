Sort an array A using Merge Sort.
Change in the input array itself. So no need to return or print anything.
Input format :
Line 1 : Integer n i.e. Array size
Line 2 : Array elements (separated by space)
Output format :
Array elements in increasing order (separated by space)
Constraints :
1 <= n <= 10^3

SOLUTION
====================================
def mergeSort(arr, start, end):
    if len(arr)==0 or len(arr)==1:
        return
    mid=(start+end)//2
    larray=arr[:mid]
    rarray=arr[mid:]
    mergeSort(larray, 0, len(larray))
    mergeSort(rarray, 0, len(rarray))
    i,j,k=0,0,0
    while(i<len(larray) and j<len(rarray)):
        if larray[i]<=rarray[j]:
            arr[k]=larray[i]
            i=i+1
            k=k+1
        else:
            arr[k]=rarray[j]
            j=j+1
            k=k+1
    while i<len(larray):
        arr[k]=larray[i]
        i=i+1
        k=k+1
    while j<len(rarray):
        arr[k]=rarray[j]
        j=j+1
        k=k+1


# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr, 0, n)
print(*arr)
