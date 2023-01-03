For a given queue containing all integer data, reverse the first K elements.
You have been required to make the desired change in the input queue itself.
Input Format :
The first line of input would contain two integers N and K, separated by a single space. They denote the total number of elements in the queue and the count with which the elements need to be reversed respectively.

The second line of input contains N integers separated by a single space, representing the order in which the elements are enqueued into the queue.
Output Format:
The only line of output prints the updated order in which the queue elements are dequeued, all of them separated by a single space. 
Note:
You are not required to print the expected output explicitly, it has already been taken care of. Just make the changes in the input queue itself.
Constraints :
1 <= N <= 10^6
1 <= K <= N
-2^31 <= data <= 2^31 - 1

 Time Limit: 1sec
Sample Input 1:
5 3
1 2 3 4 5
Sample Output 1:
3 2 1 4 5

SOLUTION
=========================================================

from sys import stdin
import queue

def reverseKElements(inputQueue, k) :
    if inputQueue.empty() or (k>inputQueue.qsize()):
        return inputQueue
    if k<=0:
        return inputQueue
    temp=list()
    for i in range(k):
        temp.append(inputQueue.get())

    while not isEmpty(temp):
        inputQueue.put(temp.pop())
    for i in range(inputQueue.qsize()-k):
        inputQueue.put(inputQueue.get())
    return inputQueue



'''-------------- Utility Functions --------------'''


#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


def top(stack) :
    #assuming the stack is never empty
    return stack[len(stack) - 1]



def takeInput():
    n_k = list(map(int, stdin.readline().strip().split(" ")))
    n = n_k[0]
    k = n_k[1]

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return k, qu


#main
k, qu = takeInput()

qu = reverseKElements(qu, k)

while not qu.empty() :
    print(qu.get(), end = " ")
