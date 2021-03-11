'''
Sum Of Nodes

For a given Binary Tree of integers, find and return the sum of all the nodes data.
Example:
                        10
                      /      \
                    20      30
                   /    \
                 40    50

When we sum up all the nodes data together, [10, 20, 30, 40 50] we get 150. Hence, the output will be 150.

Input Format:
The first and the only line of input will contain the nodes data, all separated by a single space. Since -1 is used as an indication whether the left or right node data exist for root, it will not be a part of the node data.

Output Format:
The first and the only line of output prints the sum of all the nodes data present in the binary tree.

Note:
You are not required to print anything explicitly. It has already been taken care of.

Constraints:
1 <= N <= 10^6
Where N is the total number of nodes in the binary tree.

Time Limit: 1 sec

Sample Input 1:
2 3 4 6 -1 -1 -1 -1 -1

Sample Output 1:
15

Sample Input 2:
1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1

Sample Output 2:
28
'''
from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

#Following the structure used for Binary Tree
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None




def getSum(root):
	#Your code goes here
    if root is None:
        return 0
    return root.data + getSum(root.left) + getSum(root.right)

#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

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
print(getSum(root))