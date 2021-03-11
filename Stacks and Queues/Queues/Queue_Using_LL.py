'''
Queue Using LL

Implement a Queue Data Structure specifically to store integer data using a Singly Linked List.
The data members should be private.

You need to implement the following public functions :

1. Constructor:
It initialises the data members as required.

2. enqueue(data) :
This function should take one argument of type integer. It enqueues the element into the queue and returns nothing.

3. dequeue() :
It dequeues/removes the element from the front of the queue and in turn, returns the element being dequeued or removed. In case the queue is empty, it returns -1.

4. front() :
It returns the element being kept at the front of the queue. In case the queue is empty, it returns -1.

5. getSize() :
It returns the size of the queue at any given instance of time.

6. isEmpty() :
It returns a boolean value indicating whether the queue is empty or not.

Operations Performed on the Stack:

Query-1(Denoted by an integer 1): Enqueues an integer data to the queue.

Query-2(Denoted by an integer 2): Dequeues the data kept at the front of the queue and returns it to the caller.

Query-3(Denoted by an integer 3): Fetches and returns the data being kept at the front of the queue but doesn't remove it, unlike the dequeue function.

Query-4(Denoted by an integer 4): Returns the current size of the queue.

Query-5(Denoted by an integer 5): Returns a boolean value denoting whether the queue is empty or not.

Input Format:
The first line contains an integer 'q' which denotes the number of queries to be run against each operation on the queue. 
Then the test cases follow.

Every 'q' lines represent an operation that needs to be performed.

For the enqueue operation, the input line will contain two integers separated by a single space, representing the type of the operation in integer and the integer data being enqueued into the queue.

For the rest of the operations on the queue, the input line will contain only one integer value, representing the query being performed on the queue.

Output Format:
For Query-1, you do not need to return anything.
For Query-2, prints the data being dequeued from the queue.
For Query-3, prints the data kept on the front of the queue.
For Query-4, prints the current size of the queue.
For Query-5, prints 'true' or 'false'(without quotes).

Output for every query will be printed in a separate line.

Note:
You are not required to print anything explicitly. It has already been taken care of. Just implement the functions.

Constraints:
1 <= q <= 10^5
1 <= x <= 5
-2^31 <= data <= 2^31 - 1 and data != -1

Where 'q' is the total number of queries being performed on the queue, 'x' is the range for every query and data represents the integer pushed into the queue. 

Time Limit: 1 second

Sample Input 1:
7
1 17
1 23
1 11
2
2
2
2

Sample Output 1:
17
23
11
-1

Sample Input 2:
3
2
1 10
4

Sample Output 2:
-1 
1
'''

from sys import stdin


#Following is the structure of the node class for a Singly Linked List
class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None


class Queue :

    #Define data members and __init__()
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0




    '''----------------- Public Functions of Stack -----------------'''

    def getSize(self) :
        #Implement the getSize() function
        return self.__count



    def isEmpty(self) :
        #Implement the isEmpty() function
        return self.getSize() == 0



    def enqueue(self, data) :
        #Implement the enqueue(element) function
        newNode = Node(data)
        if self.__head is None:
            self.__head = newNode
        else:
            self.__tail.next = newNode
        self.__tail = newNode
        self.__count += 1



    def dequeue(self) :
        #Implement the dequeue() function
        if self.__head is None:
            return -1
        data = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1
        return data



    def front(self) :
        #Implement the front() function
        if self.__head is None:
            return -1
        data = self.__head.data
        return data
        




#main
q = int(stdin.readline().strip())

queue = Queue()

while q > 0 :

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1 :
        data = int(inputs[1])
        queue.enqueue(data)

    elif choice == 2 :
        print(queue.dequeue())

    elif choice == 3 :
        print(queue.front())

    elif choice == 4 : 
        print(queue.getSize())

    else :
        if queue.isEmpty() :
            print("true")
        else :
            print("false")

    q -= 1