Implement the BST class which includes following functions -
1. insert -
Given an element, insert that element in the BST at the correct position. If element is equal to the data of the node, insert it in the left subtree.
2. search
Given an element, find if that is present in BST or not. Return true or false.
3. delete -
Given an element, remove that element from the BST. If the element which is to be deleted has both children, replace that with the minimum element from right sub-tree.
4. printTree (recursive) -
Print the BST in in the following format -
For printing a node with data N, you need to follow the exact format -
N:L:x,R:y
where, N is data of any node present in the binary tree. x and y are the values of left and right child of node N. Print the children only if it is not null.
There is no space in between.
You need to print all nodes in the recursive format in different lines.


SOLUTION
===================================
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
    
    def printTreeHelper(self, root):
        if root == None:
            return
        print(str(root.data)+":", end="")
        if root.left != None:
            print("L:" + str(root.left.data), end=",")
        if root.right != None:
            print("R:" + str(root.right.data), end=" ")   
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)



    def printTree(self):
        self.printTreeHelper(self.root)
    ##################################
    # PLEASE IMPLEMENT THIS FUNCTION #
    ##################################
    
    def searchHelper(self,root,data):
        if self.root == None:
            return False
        if self.root.data == data:
            return True
        if data > self.root.data:
            self.searchHelper(self.root.right,data)
        elif data < root.data:
            self.searchHelper(self.root.left,data)

    
    def search(self, data):
        return self.searchHelper(self.root,data)
    ##################################
    # PLEASE IMPLEMENT THIS FUNCTION #
    ##################################


    def insertHelper(self,root,data):
        if root == None:
            node = BinaryTreeNode(data)
            return node
        if root.data>=data:
            root.left= self.insertHelper(root.left,data)
        else:
            root.right = self.insertHelper(root.right,data)
        return root

        
    def insert(self, data):
        self.numNodes += 1
        self.root = self.insertHelper(self.root,data)
    

    ##################################
    # PLEASE IMPLEMENT THIS FUNCTION #
    ##################################
    


    def min1(self,root):
        if root == None:
            return 10000
        if root.left == None:
            return root.data


    def deleteHelper(self,root,data):
        if root == None:
            return False, None
        if root.data > data:
            deleted, newRight = self.deleteHelper(root.right,data)
            root.right = newRight
            return deleted, root
        if root.data < data:
            deleted, newLeft = slef.deleteHelper(root.left,data)
            root.left = newLeft
            return deletd, left

        if root.left == None and root.right == None:
            return True, None
        if root.left == None:
            return True, root.right

        if root.right == None:
            return True, root.left

        replace = self.min1(root.right)
        root.data = replace
        deleted, newRight = self.deleteHelper(root.right, replace)
        root.right = newRight
        return True, root
        

    def delete(self, data):
        deleted, newRoot = self.deleteHelper(self.root, data)
        if deleted:
            self.numNodes -= 1
        self.root = newRoot
        return deleted
    
    def count(self):
        return self.numNodes
        
b = BST()
q = int(input())
while (q > 0) :
    li = [int(ele) for ele in input().strip().split()]
    choice = li[0]
    q-=1
    if choice == 1:
        data = li[1]
        b.insert(data)
    elif choice == 2:
        data = li[1]
        b.delete(data)
    elif choice == 3:
        data = li[1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
    else:
        b.printTree()
