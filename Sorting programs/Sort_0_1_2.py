'''
You are given an integer array/list(ARR) of size N. It contains only 0s, 1s and 2s. Write a solution to sort this array/list in a 'single scan'.
'Single Scan' refers to iterating over the array/list just once or to put it in other words, you will be visiting each element in the array/list just once.

Sample Input 1:
1
7
0 1 2 0 2 0 1

Sample Output 1:
0 0 0 1 1 2 2 

Sample Input 2:
2
5
2 2 0 1 1
7
0 1 2 0 1 2 0

Sample Output 2:
0 1 1 2 2 
0 0 0 1 1 2 2
'''
from sys import stdin 

def sort012(arr, n) :
    i = 0
    nz = 0
    n2 = n-1
    while i <= n2:
        if arr[i] == 0:
            arr[nz], arr[i] = arr[i], arr[nz]
            nz += 1
            i += 1
        elif arr[i] == 2:
            arr[n2], arr[i] = arr[i], arr[n2]
            n2 -= 1
        else:
            i += 1

#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0 :
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

    sort012(arr, n)
    printList(arr, n)
    
    t -= 1