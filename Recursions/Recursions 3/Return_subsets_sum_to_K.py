'''
Return subsets sum to K

Given an array A of size n and an integer K, return all subsets of A which sum to K.
Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.

Note : The order of subsets are not important.

Input format :
Line 1 : Integer n, Size of input array
Line 2 : Array elements separated by space
Line 3 : K 

Constraints :
1 <= n <= 20

Sample Input :
9 
5 12 3 17 1 18 15 3 17 
6

Sample Output :
3 3
5 1
'''

from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

def findSubsetsThatSumToKHelper(arr, k, idx, output):

    if(idx == len(arr)) :
        if k == 0 :
            return [[]]
        else:
            return output

    temp1 = findSubsetsThatSumToKHelper(arr, k, idx + 1, output)
    
    temp2 = findSubsetsThatSumToKHelper(arr, k - arr[idx], idx + 1, output)
    
    output = []
    
    for i in range(len(temp2)):
        output.append([arr[idx]])
        for j in range(len(temp2[i])):
            output[i].append(temp2[i][j])
    
    for i in temp1:
        output.append(i)
    
    return output




def findSubsetsThatSumToK(arr, k) :

    output = findSubsetsThatSumToKHelper(arr, k, 0, [])
    return output

def takeInput() :
    n = int(input().strip())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    k = int(input().strip())

    return arr, n, k

def printAnswer(subsets) :
    subsets.sort()
    for subset in subsets :
        for value in subset :
            print(value, end =" ")
        print()

#   main
arr, n, k= takeInput()
subsets = findSubsetsThatSumToK(arr, k)
printAnswer(subsets)
