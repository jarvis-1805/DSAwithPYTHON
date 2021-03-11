'''
Is node present?

For a given Binary Tree of type integer and a number X, find whether a node exists in the tree with data X or not.

Input Format:
The first and the only line of input will contain the node data, all separated by a single space. Since -1 is used as an indication whether the left or right node data exist for root, it will not be a part of the node data.

Output Format:
The only line of output prints 'true' or 'false'.

Note:
You are not required to print anything explicitly. It has already been taken care of.

Constraints:
1 <= N <= 10^5
Where N is the total number of nodes in the binary tree.

Time Limit: 1 sec

Sample Input 1:
8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
7

Sample Output 1:
true

Sample Input 2:
2 3 4 -1 -1 -1 -1
10

Sample Output 2:
false
'''
from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None




def isNodePresent(root, x) :
	#Your code goes here
    if root is None:
        return
    if root.data == x:
        return True
    leftT = isNodePresent(root.left, x)
    rightT = isNodePresent(root.right, x)
    if leftT:
        return True
    if rightT:
        return True

#Taking level-order input using fast I/O method
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
x = int(stdin.readline().strip())

if isNodePresent(root, x) :
	print("true")

else :
	print("false")