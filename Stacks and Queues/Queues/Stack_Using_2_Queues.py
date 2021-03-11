'''
Stack Using 2 Queues

Implement a Stack Data Structure specifically to store integer data using two Queues. You have to implement it in such a way that the push operation is done in O(1) time and the pop and top operations are done in O(N) time.
There should be two data members, both being Queues to store the data internally. You may use the inbuilt Queue.

Implement the following public functions :

1. Constructor:
It initialises the data members as required.

2. push(data) :
This function should take one argument of type integer. It pushes the element into the stack and returns nothing.

3. pop() :
It pops the element from the top of the stack and in turn, returns the element being popped or deleted. In case the stack is empty, it returns -1.

4. top :
It returns the element being kept at the top of the stack. In case the stack is empty, it returns -1.

5. size() :
It returns the size of the stack at any given instance of time.

6. isEmpty() :
It returns a boolean value indicating whether the stack is empty or not.
Operations Performed on the Stack:

Query-1(Denoted by an integer 1): Pushes an integer data to the stack.

Query-2(Denoted by an integer 2): Pops the data kept at the top of the stack and returns it to the caller.

Query-3(Denoted by an integer 3): Fetches and returns the data being kept at the top of the stack but doesn't remove it, unlike the pop function.

Query-4(Denoted by an integer 4): Returns the current size of the stack.

Query-5(Denoted by an integer 5): Returns a boolean value denoting whether the stack is empty or not.

Input Format:
The first line contains an integer 'q' which denotes the number of queries to be run against each operation in the stack. 
Then the test cases follow.

Every 'q' lines represent an operation that needs to be performed.

For the push operation, the input line will contain two integers separated by a single space, representing the type of the operation in integer and the integer data being pushed into the stack.

For the rest of the operations on the stack, the input line will contain only one integer value, representing the query being performed on the stack.

Output Format:
For Query-1, you do not need to return anything.
For Query-2, prints the data being popped from the stack.
For Query-3, prints the data kept on the top of the stack.
For Query-4, prints the current size of the stack.
For Query-5, prints 'true' or 'false'(without quotes).

Output for every query will be printed in a separate line.

Note:
You are not required to print anything explicitly. It has already been taken care of. Just implement the function.

Constraints:
1 <= q <= 100
1 <= x <= 5
-2^31 <= data <= 2^31 - 1 and data != -1

Where 'q' is the total number of queries being performed on the stack, 'x' is the range for every query and data represents the integer pushed into the stack. 

Time Limit: 1 second

Sample Input 1:
6
1 13
1 47
4
5
2
3

Sample Output 1:
2
false
47
13

Sample Input 2:
4
5
2
1 10
5

Sample Output 2:
true
-1
false
'''

from sys import stdin

class Stack :

	#Define data members and __init__()
    def __init__(self):
        self.__q1 = []
        self.__q2 = []
        self.__count = 0
    
    def getSize(self) :
        return self.__count
    
    def isEmpty(self) :
		#Implement the isEmpty() function
        return self.getSize() == 0
    
    def push(self, data) :
		#Implement the push(element) function
        self.__count += 1
        self.__q1.append(data)
        
    def pop(self) :
		#Implement the pop() function
        if self.__count <= 0:
            return -1
        for i in range(self.__count - 1):
            self.__q2.append(self.__q1.pop(0))
        temp = self.__q1[0]
        self.__q1 = self.__q2
        self.__q2 = []
        self.__count -= 1
        return temp
    
    def top(self) :
		#Implement the top() function
        if self.__count <= 0:
            return -1
        ans = self.pop()
        self.push(ans)
        return ans
		
#main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0 :

	inputs = stdin.readline().strip().split(" ")
	choice = int(inputs[0])

	if choice == 1 :
		data = int(inputs[1])
		stack.push(data)

	elif choice == 2 :
		print(stack.pop())

	elif choice == 3 :
		print(stack.top())

	elif choice == 4 : 
		print(stack.getSize())

	else :
		if stack.isEmpty() :
			print("true")
		else :
			print("false")

	q -= 1