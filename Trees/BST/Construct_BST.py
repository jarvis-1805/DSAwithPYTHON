'''
Construct BST

Given a sorted integer array A of size n, which contains all unique elements. You need to construct a balanced BST from this input array. Return the root of constructed BST.

Note: If array size is even, take first mid as root.

Input format:
The first line of input contains an integer, which denotes the value of n. The following line contains n space separated integers, that denote the values of array.

Output Format:
The first and only line of output contains values of BST nodes, printed in pre order traversal.

Constraints:
Time Limit: 1 second

Sample Input 1:
7
1 2 3 4 5 6 7

Sample Output 1:
4 2 1 3 6 5 7
'''

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructBST(lst, start, end):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    if start > end: return None
    mid = (start+end)//2
    root = BinaryTreeNode(lst[mid])
    left = constructBST(lst, start, mid - 1)
    right = constructBST(lst, mid + 1, end)
    root.left = left
    root.right = right
    return root
    #############################
    

def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
n=int(input())
if(n>0):
    lst=[int(i) for i in input().strip().split()]
else:
    lst=[]
root=constructBST(lst, 0, len(lst)-1)
preOrder(root)