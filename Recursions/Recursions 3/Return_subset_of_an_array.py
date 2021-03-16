'''
Return subset of an array

Given an integer array (of length n), find and return all the subsets of input array.
Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.

Note : The order of subsets are not important.

Input format :

Line 1 : Size of array

Line 2 : Array elements (separated by space)

Sample Input:
3
15 20 12

Sample Output:
[] (this just represents an empty array, don't worry about the square brackets)
12 
20 
20 12 
15 
15 12 
15 20 
15 20 12
'''

## Read input as specified in the question.
## Print output as specified in the question.

from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

def subset(arr):
    if len(arr) == 0:
        return [[]]
    
    temp = subset(arr[1:])
    
    output = []
    
    for i in range(len(temp)):
        output.append([arr[0]])
        for j in range(len(temp[i])):
            output[i].append(temp[i][j])
            
    for i in temp:
        output.append(i)
    
    return output

def takeInput() :
    n = int(input().strip())
    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n

def printAnswer(subsets) :
    subsets.sort()
    for subset in subsets :
        for value in subset :
            print(value, end =" ")
        print()

#   main
arr, n = takeInput()
subsets = subset(arr)
printAnswer(subsets)