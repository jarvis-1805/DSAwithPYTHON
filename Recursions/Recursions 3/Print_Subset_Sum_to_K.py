'''
Print Subset Sum to K

Given an array A and an integer K, print all subsets of A which sum to K.
Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.

Note : The order of subsets are not important. Just print them in different lines.

Input format :
Line 1 : Size of input array
Line 2 : Array elements separated by space
Line 3 : K 

Sample Input:
9 
5 12 3 17 1 18 15 3 17 
6

Sample Output:
3 3
5 1
'''

## Read input as specified in the question.
## Print output as specified in the question.
from sys import stdin

def printAllSubsetsRec(arr, n, v, k):
    if (k == 0):
        for value in v:
            print(value, end=" ")
        print()
        return

    if (n == 0):
        return
    
    printAllSubsetsRec(arr, n - 1, v, k)
    v1 = []
    v1.append(arr[n - 1])
    v1 += v
    printAllSubsetsRec(arr, n - 1, v1, k - arr[n - 1])

def printAllSubsets(arr, n, k):
    v = []
    printAllSubsetsRec(arr, n, v, k)

def takeInput() :
    n = int(input().strip())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    k = int(input().strip())

    return arr, n, k

arr, n, k = takeInput()
printAllSubsets(arr, n, k)