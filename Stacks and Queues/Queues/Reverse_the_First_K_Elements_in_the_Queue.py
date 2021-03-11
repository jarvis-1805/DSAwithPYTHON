'''
Reverse the First K Elements in the Queue

For a given queue containing all integer data, reverse the first K elements.
You have been required to make the desired change in the input queue itself.

Input Format :
The first line of input would contain two integers N and K, separated by a single space. They denote the total number of elements in the queue and the count with which the elements need to be reversed respectively.

The second line of input contains N integers separated by a single space, representing the order in which the elements are enqueued into the queue.

Output Format:
The only line of output prints the updated order in which the queue elements are dequeued, all of them separated by a single space. 

Note:
You are not required to print the expected output explicitly, it has already been taken care of. Just make the changes in the input queue itself.

Contraints :
1 <= N <= 10^6
1 <= K <= N
-2^31 <= data <= 2^31 - 1

Time Limit: 1sec

Sample Input 1:
5 3
1 2 3 4 5

Sample Output 1:
3 2 1 4 5

Sample Input 2:
7 7
3 4 2 5 6 7 8

Sample Output 2:
8 7 6 5 2 4 3
'''

from sys import stdin
import queue

def reverseKElements(Queue, k) :
    #Your code goes here
    if (Queue.empty() == True or
             k > Queue.qsize()): 
        return
    if (k <= 0): 
        return
 
    Stack = []
    for i in range(k):
        Stack.append(Queue.queue[0]) 
        Queue.get()
    while (len(Stack) != 0 ): 
        Queue.put(Stack[-1]) 
        Stack.pop()
    for i in range(Queue.qsize() - k):
        Queue.put(Queue.queue[0]) 
        Queue.get()
    return Queue


'''-------------- Utility Functions --------------'''


#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


#Takes a list as a stack and returns the element at the top
def top(stack) :
    #assuming the stack is never empty
    return stack[len(stack) - 1]



def takeInput():
    n_k = list(map(int, stdin.readline().strip().split(" ")))
    n = n_k[0]
    k = n_k[1]

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return k, qu


#main
k, qu = takeInput()

qu = reverseKElements(qu, k)

while not qu.empty() :
    print(qu.get(), end = " ")