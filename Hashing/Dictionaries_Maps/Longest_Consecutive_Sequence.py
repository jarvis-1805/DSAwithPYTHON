'''
Longest Consecutive Sequence

You are given an array of unique integers that contain numbers in random order. You have to find the longest possible sequence of consecutive numbers using the numbers from given array.
You need to return the output array which contains starting and ending element. If the length of the longest possible sequence is one, then the output array must contain only single element.

Note:
1. Best solution takes O(n) time.
2. If two sequences are of equal length, then return the sequence starting with the number whose occurrence is earlier in the array.

Input format:
The first line of input contains an integer, that denotes the value of the size of the array. Let us denote it with the symbol n.
The following line contains n space separated integers, that denote the value of the elements of the array.

Output format:
The first and only line of output contains starting and ending element of the longest consecutive sequence. If the length of longest consecutive sequence, then just print the starting element.

Constraints :
0 <= n <= 10^6

Time Limit: 1 sec

Sample Input 1 :
13
2 12 9 16 10 5 3 20 25 11 1 8 6 

Sample Output 1 :
8 12 

Sample Input 2 :
7
3 7 2 1 9 8 41

Sample Output 2 :
7 9

Explanation: Sequence should be of consecutive numbers. Here we have 2 sequences with same length i.e. [1, 2, 3] and [7, 8, 9], but we should select [7, 8, 9] because the starting point of [7, 8, 9] comes first in input array and therefore, the output will be 7 9, as we have to print starting and ending element of the longest consecutive sequence.

Sample Input 3 :
7
15 24 23 12 19 11 16

Sample Output 3 :
15 16
'''

from sys import stdin

def longestConsecutiveSubsequence(arr,n): 
    # Write your code here
    d = {}
    for i in arr:
        d[i] = d.get(i, 0)
    
    maxLength = 0
    start = 0
    end = 0
    for i in arr:
        length = 0
        if i in d and d[i] != 1:
            temp = i
            while temp in d:
                length += 1
                d[temp] = 1
                end = temp
                temp += 1
            temp = i-1
            start = i
            while temp in d:
                length += 1
                d[temp] = 1
                start = temp
                temp -= 1
            if length > maxLength:
                maxLength = length
                fStart = start
                fEnd = end
            elif length == maxLength:
                for i in arr:
                    if start == i:
                        fStart = start
                        fEnd = end
                        break
                    elif fStart == i:
                        break
    
    return fStart, fEnd
            


def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

    
# Main 
arr,n=takeInput()
ans = longestConsecutiveSubsequence(arr,n) 
# This ans array contains two numbers, ie, start and end of longest sequence respectively
print(*ans)