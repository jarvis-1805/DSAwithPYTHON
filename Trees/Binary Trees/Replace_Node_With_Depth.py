'''
Replace Node With Depth

For a given a Binary Tree of integers, replace each of its data with the depth of the tree.
Root is at depth 0, hence the root data is updated with 0. Replicate the same further going down the in the depth of the given tree.
The modified tree will be printed in the in-order fashion.

Output: 2 1 2 0 2 1 2 (printed in the in-order fashion)

Input Format:
The first and the only line of input will contain the node data, all separated by a single space. Since -1 is used as an indication whether the left or right node data exist for root, it will not be a part of the node data.

Output Format:
The first and the only line of output prints the updated tree in the in-order fashion.

Note:
You are not required to print anything explicitly. It has already been taken care of.

Constraints:
1 <= N <= 10^5
Where N is the total number of nodes in the binary tree.

Time Limit: 1sec

Sample Input 1:
2 35 10 2 3 5 2 -1 -1 -1 -1 -1 -1 -1 -1 

Sample Output 1:
2 1 2 0 2 1 2 

Sample Input 2:
1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1

Sample Output 2:
2 1 2 0 2 1 2 
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




def changeToDepthTree(root, d = 0) :
	#Your code goes here
    if root is None:
        return
    root.data = d
    changeToDepthTree(root.left, d + 1)
    changeToDepthTree(root.right, d + 1)

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


def inOrder(root) :
	if root is None :
		return 

	inOrder(root.left)
	print(root.data, end = " ")
	inOrder(root.right)
	

# Main
root = takeInput()

changeToDepthTree(root)
inOrder(root)