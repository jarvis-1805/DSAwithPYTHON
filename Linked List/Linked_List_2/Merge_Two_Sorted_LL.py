'''
Code : Merge two sorted LL

You have been given two sorted(in ascending order) singly linked lists of integers.
Write a function to merge them in such a way that the resulting singly linked list is also sorted(in ascending order) and return the new head to the list.

Note :
Try solving this in O(1) auxiliary space.
No need to print the list, it has already been taken care.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
The first line of each test case or query contains the elements of the first sorted singly linked list separated by a single space. 
The second line of the input contains the elements of the second sorted singly linked list separated by a single space. 

Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element

Output :
For each test case/query, print the resulting sorted singly linked list, separated by a single space.
Output for every test case will be printed in a seperate line.

Constraints :
1 <= t = 10^2
0 <= N <= 10 ^ 4
0 <= M <= 10 ^ 4
Where N and M denote the sizes of the singly linked lists. 

Time Limit: 1sec

Sample Input 1 :
1
2 5 8 12 -1
3 6 9 -1

Sample Output 1 :
2 3 5 6 8 9 12 

Sample Input 2 :
2
2 5 8 12 -1
3 6 9 -1
10 40 60 60 80 -1
10 20 30 40 50 60 90 100 -1

Sample Output 2 :
2 3 5 6 8 9 12 
10 10 20 30 40 40 50 60 60 60 80 90 100
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

def merge1(head1, head2):
    if head1 is None and head2 is None:
        return None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    head = None
    tail = None
    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            if head is None:
                head = head1
                tail = head1
            else:
                tail.next = head1
                tail = tail.next
            head1 = head1.next
        elif head2.data < head1.data:
            if head is None:
                head = head2
                tail = head2
            else:
                tail.next = head2
                tail = tail.next
            head2 = head2.next
            
    if head1 is not None:
        tail.next = head1
    if head2 is not None:
        tail.next = head2
    return head

def merge2(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    # create dummy node to avoid additional checks in loop
    s = t = Node(0) 
    while not (head1 is None or head2 is None):
        if head1.data < head2.data:
            # remember current low-node
            c = head1
            # follow ->next
            head1 = head1.next
        else:
            # remember current low-node
            c = head2
            # follow ->next
            head2 = head2.next

        # only mutate the node AFTER we have followed ->next
        t.next = c          
        # and make sure we also advance the temp
        t = t.next

    t.next = head1 or head2

    # return tail of dummy node
    return s.next

head1 = take_input()
head2 = take_input()
printLL(head1)
printLL(head2)
head = merg1(head1, head2)
printLL(head)