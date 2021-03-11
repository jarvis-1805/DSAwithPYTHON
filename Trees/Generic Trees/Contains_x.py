'''
Contains x

Given a generic tree and an integer x, check if x is present in the given tree or not. Return true if x is present, return false otherwise.

Input format :
The first line of input contains data of the nodes of the tree in level order form. The order is: data for root node, number of children to root node, data of each of child nodes and so on and so forth for each node. The data of the nodes of the tree is separated by space.  
The following line contains an integer, that denotes the value of x.

Output format :
The first and only line of output contains true, if x is present and false, otherwise.

Constraints:
Time Limit: 1 sec

Sample Input 1 :
10 3 20 30 40 2 40 50 0 0 0 0
40 

Sample Output 1 :
true

Sample Input 2 :
10 3 20 30 40 2 40 50 0 0 0 0
4 

Sample Output 2:
false
'''

from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def containsX(root, x):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    if root is None:
        return False
    
    if root.data == x:
        return True
    
    for child in root.children:
        if containsX(child, x):
            return True
    
    return False
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

arr = list(int(x) for x in stdin.readline().strip().split())
x=int(stdin.readline().strip())
tree = createLevelWiseTree(arr)
if containsX(tree,x):
    print('true')
else:
    print('false')