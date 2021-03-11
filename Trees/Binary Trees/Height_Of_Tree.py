'''
Height Of Tree

For a given Binary Tree of integers, find and return the height of the tree.
Example:
                        10
                      /    \
                    20      30
                   /    \
                 40    50

Height of the given tree is 3. 

Height is defined as the total number of nodes along the longest path from the root to any of the leaf node.

Input Format:
The first and the only line of input will contain the node data, all separated by a single space. Since -1 is used as an indication whether the left or right node data exist for root, it will not be a part of the node data.

Output Format:
The first and the only line of output prints the height of the given binary tree.

Note:
You are not required to print anything explicitly. It has already been taken care of.

Constraints:
0 <= N <= 10^5
Where N is the total number of nodes in the binary tree.

Time Limit: 1 sec

Sample Input 1:
10 20 30 40 50 -1 -1 -1 -1 -1 -1

Sample Output 1:
3

Sample Input 2:
3 -1 -1

Sample Output 2:
1
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



def height(root) :
	#Your code goes here
    if root is None:
        return 0
    leftH = height(root.left)
    rightH = height(root.right)
    return 1 + max(leftH, rightH)
    
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

h = height(root)
print(h)