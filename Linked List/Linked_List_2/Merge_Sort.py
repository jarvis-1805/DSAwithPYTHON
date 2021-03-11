'''
Code : Merge Sort

Given a singly linked list of integers, sort it using 'Merge Sort.'

Note :
No need to print the list, it has already been taken care. Only return the new head to the list.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
The first and the only line of each test case or query contains the elements of the singly linked list separated by a single space.
Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element

Output format :
For each test case/query, print the elements of the sorted singly linked list.
Output for every test case will be printed in a seperate line.

Constraints :
1 <= t <= 10^2
0 <= M <= 10^5
Where M is the size of the singly linked list.

Time Limit: 1sec

Sample Input 1 :
1
10 9 8 7 6 5 4 3 -1

Sample Output 1 :
3 4 5 6 7 8 9 10 

Sample Output 2 :
2
-1
10 -5 9 90 5 67 1 89 -1

Sample Output 2 :
-5 1 5 9 10 67 89 90 
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

def merge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    s = t = Node(0) 
    while not (head1 is None or head2 is None):
        if head1.data < head2.data:
            c = head1
            head1 = head1.next
        else:
            c = head2
            head2 = head2.next

        t.next = c
        t = t.next

    t.next = head1 or head2

    return s.next

def mergeSort(head) :
    if head == None or head.next == None: 
            return head
  
    middle = getMiddle(head) 
    nexttomiddle = middle.next

    middle.next = None

    left = mergeSort(head) 

    right = mergeSort(nexttomiddle) 

    sortedlist = merge(left, right) 
    return sortedlist 
      
def getMiddle(head): 
    if (head == None): 
        return head 

    slow = head 
    fast = head 

    while (fast.next != None and 
           fast.next.next != None): 
        slow = slow.next
        fast = fast.next.next

    return slow

head1 = take_input()
head2 = take_input()
printLL(head1)
printLL(head2)
head = mergeSort(head1, head2)
printLL(head)