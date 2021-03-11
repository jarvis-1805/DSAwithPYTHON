'''
BST Class

Implement the BST class which includes following functions -

1. search
Given an element, find if that is present in BST or not. Return true or false.

2. insert -
Given an element, insert that element in the BST at the correct position. If element is equal to the data of the node, insert it in the left subtree.

3. delete -
Given an element, remove that element from the BST. If the element which is to be deleted has both children, replace that with the minimum element from right sub-tree.

4. printTree (recursive) -
Print the BST in ithe following format -
For printing a node with data N, you need to follow the exact format -
N:L:x,R:y
wherer, N is data of any node present in the binary tree. x and y are the values of left and right child of node N. Print the children only if it is not null.
There is no space in between.
You need to print all nodes in the recursive format in different lines.

Sample Input:
8
1 4
1 4
1 4
1 4
4
3 4
2 4
4

Sample Output:
4:L:4,
4:L:4,
4:L:4,
4:
true
4:L:4,
4:L:4,
4:
'''

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
        if root is None:
            return
        
        print(root.data, end = ":")
        
        if root.left is not None:
            print("L:", end='')
            print(root.left.data, end=',')
        
        if root.right is not None:
            print("R:", end='')
            print(root.right.data, end='')
        print()
        
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)
    
    def printTree(self):
        self.printTreeHelper(self.root)
    
    
    def isPresentHelper(self, root, data):
        if root is None:
            return False
        
        if root.data == data:
            return True
        
        if root.data > data:
            #call on left
            return self.isPresentHelper(root.left, data)
        else:
            #call on right
            return self.isPresentHelper(root.right, data)
    
    def search(self, data):
        return self.isPresentHelper(self.root, data)

        
    def insertHelper(self, root, data):
        if root is None:
            node = BinaryTreeNode(data)
            return node
        
        if root.data >= data:
            root.left = self.insertHelper(root.left, data)
            return root
        else:
            root.right = self.insertHelper(root.right, data)
            return root
    
    def insert(self, data):
        self.numNodes += 1
        self.root = self.insertHelper(self.root, data)
    
      
    def min(self, root):
        if root is None:
            return 10000
        
        if root.left is None:
            return root.data
        
        return self.min(root.left)
    
    def deleteDataHelper(self, root, data):
        if root is None:
            return False, None
        
        if root.data < data:
            deleted, newRightNode = self.deleteDataHelper(root.right, data)
            root.right = newRightNode
            return deleted, root
        
        if root.data > data:
            deleted, newLeftNode = self.deleteDataHelper(root.left, data)
            root.left = newLeftNode
            return deleted, root
        
        #root is leaf
        if root.left is None and root.right is None:
            return True, None
        
        #root has one child
        if root.left is None:
            return True, root.right
        
        if root.right is None:
            return True, root.left
        
        #root has two children
        replacement = self.min(root.right)
        root.data = replacement
        deleted, newRightNode = self.deleteDataHelper(root.right, replacement)
        root.right = newRightNode
        return True, root
    
    def delete(self, data):
        deleted, newRoot = self.deleteDataHelper(self.root, data)
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