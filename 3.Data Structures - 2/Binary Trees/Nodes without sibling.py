For a given Binary Tree of type integer, print all the nodes without any siblings.
Input Format:
The first and the only line of input will contain the node data, all separated by a single space. Since -1 is used as an indication whether the left or right node data exist for root, it will not be a part of the node data.
Output Format:
The only line of output prints the node data in a top to down fashion with reference to the root. 
Node data in the left subtree will be printed first and then the right subtree.
A single space will separate them all.
 Constraints:
1 <= N <= 10^5
Where N is the total number of nodes in the binary tree.

Time Limit: 1 second
Sample Input 1:
5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
Sample Output 1:
9    


SOLUTION
===============================
from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def printNodesWithoutSibling(root) :
    if root is None:
        return
    
    if root.left is None:
        if root.right is not None:
            print(root.right.data, end=" ")
    else:
        if root.right is None:
            print(root.left.data, end = " ")
    
    printNodesWithoutSibling(root.left)
    printNodesWithoutSibling(root.right)

def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    
    length = len(levelOrder)

    if length == 1 :
        return None
    
    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root

	

# Main
root = takeInput()
printNodesWithoutSibling(root)
