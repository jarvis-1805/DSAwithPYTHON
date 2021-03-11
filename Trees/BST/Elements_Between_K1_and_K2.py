'''
Elements Between K1 and K2

Given a Binary Search Tree and two integers k1 and k2, find and print the elements which are in range k1 and k2 (both inclusive).
Print the elements in increasing order.

Input format:
The first line of input contains data of the nodes of the tree in level order form. The data of the nodes of the tree is separated by space. If any node does not have left or right child, take -1 in its place. Since -1 is used as an indication whether the left or right nodes exist, therefore, it will not be a part of the data of any node.
The following line contains two integers, that denote the value of k1 and k2.

Output Format:
The first and only line of output prints the elements which are in range k1 and k2 (both inclusive). Print the elements in increasing order.

Constraints:
Time Limit: 1 second

Sample Input 1:
8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
6 10

Sample Output 1:
6 7 8 10
'''

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printBetweenK1K2(root, k1, k2, l):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    if root is None:
        return
    if root.data > k2:
        printBetweenK1K2(root.left, k1, k2, l)
    elif root.data < k1:
        printBetweenK1K2(root.right, k1, k2, l)
    else:
        l.append(root.data)
        printBetweenK1K2(root.left, k1, k2, l)
        printBetweenK1K2(root.right, k1, k2, l)
    return l
    #############################

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
k1, k2 = (int(i) for i in input().strip().split())
l = printBetweenK1K2(root, k1, k2, [])
if l is not None:
    l.sort()
    for i in l:
    	print(i, end=' ')