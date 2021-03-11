'''
You have been given a random integer array/list(ARR) of size N. You are required to find and return the second largest element present in the array/list.
If N <= 1 or all the elements are same in the array/list then return -2147483648 or -2 ^ 31(It is the smallest value for the range of Integer)

Sample Input 1:
1
7
2 13 4 1 3 6 28

Sample Output 1:
13

Sample Input 2:
1
5
9 3 6 2 9

Sample Output 2:
6

Sample Input 3:
2
2
6 6
4
90 8 90 5

Sample Output 3:
-2147483648
8
'''
from sys import stdin


def rotate(arr, n):
    l = -999
    s = -999
    for i in range(len(arr)):
        if arr[i] > l:
            s = l
            l = arr[i]
        if arr[i] > s and arr[i] < l:
            s = arr[i]
    if s != -999:
        return s
    else:
        return -2147483648
        
#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list 
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()
    print(rotate(arr, n))
    
    t -= 1