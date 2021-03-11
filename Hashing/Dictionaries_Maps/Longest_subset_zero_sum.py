'''
Longest subset zero sum

Given an array consisting of positive and negative integers, find the length of the longest subarray whose sum is zero.

Input Format:
The first line of input contains an integer, that denotes the value of the size of the array. Let us denote it with the symbol N.
The following line contains N space separated integers, that denote the value of the elements of the array.

Output Format
The first and only line of output contains length of the longest subarray whose sum is zero.

Constraints:
0 <= N <= 10^8

Time Limit: 1 sec

Sample Input 1:
10 
95 -97 -387 -435 -5 -70 897 127 23 284

Sample Output 1:
5

Explanation:
The five elements that form the longest subarray that sum up to zero are: -387, -435, -5, -70, 897 
'''

def subsetSum(l):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    sum = 0
    i = -1
    d = {sum: i}
    maxLength = -9999
    while i < len(l)-1:
        i += 1
        sum += l[i]
        if sum in d:
            lengthSubset = i - d[sum]
            if lengthSubset > maxLength:
                maxLength = lengthSubset
        else:
            d[sum] = i
    return maxLength
    #############################


# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(subsetSum(l))