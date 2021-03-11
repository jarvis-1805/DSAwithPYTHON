'''
Palindrome LinkedList

You have been given a head to a singly linked list of integers. Write a function check to whether the list given is a 'Palindrome' or not.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
First and the only line of each test case or query contains the the elements of the singly linked list separated by a single space.

Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element.

Output format :
For each test case, the only line of output that print 'true' if the list is Palindrome or 'false' otherwise.

Constraints :
1 <= t <= 10^2
0 <= M <= 10^5

Time Limit: 1sec

Where 'M' is the size of the singly linked list.

Sample Input 1 :
1
9 2 3 3 2 9 -1

Sample Output 1 :
true

Sample Input 2 :
2
0 2 3 2 5 -1
-1

Sample Output 2 :
false
true

Explanation for the Sample Input 2 :
For the first query, it is pretty intuitive that the the given list is not a palindrome, hence the output is 'false'.

For the second query, the list is empty. An empty list is always a palindrome , hence the output is 'true'.
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

def length(head):
    ctr = 0
    while head is not None:
        ctr += 1
        head = head.next
    return ctr

def isPalindrome(head) :
    #Your code goes here
    if head is None or head.next is None:
        return True
    l = length(head)
    l1 = l//2
    h1 = head
    temp = head
    temp1 = None
    for i in range(l1):
        temp1 = temp
        temp = temp.next
    temp1.next = None
    h2 = temp
    t1 = h2
    t2 = h2.next
    while t2 is not None:
        curr = t2
        t2 = t2.next
        curr.next = t1
        t1 = curr
    h2 = t1
    while h1 is not None:
        if h1.data != h2.data:
            return False
        h1 = h1.next
        h2 = h2.next
    else:
        return True

head = take_input()
printLL(head)
print(isPalindrome(head))