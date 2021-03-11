'''
Delete node (recursive)

Given a singly linked list of integers and position 'i', delete the node present at the 'i-th' position in the linked list recursively.

Note :
Assume that the Indexing for the linked list always starts from 0.
No need to print the list, it has already been taken care. Only return the new head to the list.

input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
The first line of each test case or query contains the elements of the singly linked list separated by a single space.
The second line of input contains a single integer depicting the value of 'i'.

Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element

Output format :
For each test case/query, print the elements of the updated singly linked list.
Output for every test case will be printed in a seperate line.

Constraints :
1 <= t <= 10^2
0 <= M <= 10^5
Where M is the size of the singly linked list.
0 <= i < M

Time Limit:  1sec

Sample Input 1 :
1
3 4 5 2 6 1 9 -1
3

Sample Output 1 :
3 4 5 6 1 9

Sample Input 2 :
2
30 -1
0
10 20 30 50 60 -1
4

Sample Output 2 :
10 20 30 50 
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def take_input():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
            
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
        
    return head

def printLL(head):
    while head is not None:
        print(str(head.data) + ' -> ', end = '')
        head = head.next
    print('None')
    
    return

def deleteNodeRec(head, i) :
    if i<0:
        return head
    
    if head is None:
        return None
    
    if i == 0:
        curr = head
        head = head.next
        del curr
        return head
    
    smallHead = deleteNodeRec(head.next, i-1)
    head.next = smallHead
    return head

head = take_input()
printLL(head)
head = deleteNodeRec(head, 3)
printLL(head)