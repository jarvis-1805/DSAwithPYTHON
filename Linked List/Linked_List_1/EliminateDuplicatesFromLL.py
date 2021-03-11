'''
Eliminate duplicates from LL

You have been given a singly linked list of integers where the elements are sorted in ascending order. Write a function that removes the consecutive duplicate values such that the given list only contains unique elements and returns the head to the updated list.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
The first and the only line of each test case or query contains the elements(in ascending order) of the singly linked list separated by a single space.

Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element.

Output format :
For each test case/query, print the resulting singly linked list of integers in a row, separated by a single space.
Output for every test case will be printed in a seperate line.

Constraints :
1 <= t <= 10^2
0 <= M <= 10^5

Time Limit: 1sec

Where 'M' is the size of the singly linked list.

Sample Input 1 :
1
1 2 3 3 4 3 4 5 4 5 5 7 -1

Sample Output 1 :
1 2 3 4 3 4 5 4 5 7 

Sample Input 2 :
2
10 20 30 40 50 -1
10 10 10 10 -1

Sample Output 2 :
10 20 30 40 50
10
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

def removeDuplicates(head):
    if head is None or head.next is None:
        return
    temp = head
    temp1 = head.next
    while temp1 is not None:
        if temp.data == temp1.data:
            curr = temp1
            temp1 = curr.next
            temp.next = temp1
            del curr
        else:
            temp = temp1
            temp1 = temp1.next
    return head

head = take_input()
printLL(head)
head = removeDuplicates(head)
printLL(head)