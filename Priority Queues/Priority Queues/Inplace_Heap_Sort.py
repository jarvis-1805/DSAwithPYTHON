'''
Inplace Heap Sort

Given an integer array of size N. Sort this array (in decreasing order) using heap sort.

Note: Space complexity should be O(1).

Input Format:
The first line of input contains an integer, that denotes the value of the size of the array or N.
The following line contains N space separated integers, that denote the value of the elements of the array.

Output Format :
The first and only line of output contains array elements after sorting. The elements of the array in the output are separated by single space.

Constraints :
1 <= n <= 10^6

Time Limit: 1 sec

Sample Input 1:
6 
2 6 8 5 4 3

Sample Output 1:
8 6 5 4 3 2
'''

def down_heapify(arr, i, n):
    parentIndex = i
    leftChildIndex = 2 * parentIndex + 1
    rightChildIndex = 2 * parentIndex + 2
    
    while leftChildIndex < n:
        minIndex = parentIndex
        if arr[minIndex] > arr[leftChildIndex]:
            minIndex = leftChildIndex
        if rightChildIndex < n and arr[minIndex] > arr[rightChildIndex]:
            minIndex = rightChildIndex
            
        if minIndex == parentIndex:
            return
        arr[parentIndex], arr[minIndex] = arr[minIndex], arr[parentIndex]
        parentIndex = minIndex
        leftChildIndex = 2 * parentIndex + 1
        rightChildIndex = 2 * parentIndex + 2

def heapSort(arr):
    ######################
    #PLEASE ADD CODE HERE#
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        down_heapify(arr, i, n)
        
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        down_heapify(arr, 0, i)
    return
    ######################

n = input()
arr = [int(ele) for ele in input().split()]
heapSort(arr)
for ele in arr:
    print(ele,end=' ')