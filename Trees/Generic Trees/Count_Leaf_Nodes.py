'''
Count leaf Nodes

Given a generic tree, count and return the number of leaf nodes present in the given tree.

Input format :
The first line of input contains data of the nodes of the tree in level order form. The order is: data for root node, number of children to root node, data of each of child nodes and so on and so forth for each node. The data of the nodes of the tree is separated by space.  

Output Format :
The first and only line of output prints the count of leaf nodes present in the given tree.
Constraints:
Time Limit: 1 sec

Sample Input 1 :
10 3 20 30 40 2 40 50 0 0 0 0 

Sample Output 1 :
4
'''

import sys
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def leafNodeCount(tree):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    if tree is None:
        return 0
    
    leaves = 0
    
    if len(tree.children) == 0:
        return 1
    
    for child in tree.children:
        leaves += leafNodeCount(child)
    
    return leaves
    #############################

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
sys.setrecursionlimit(10**6)
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(leafNodeCount(tree))