'''
Pairs with difference K

You are given with an array of integers and an integer K. You have to find and print the count of all such pairs which have difference K.
Note: Take absolute difference between the elements of the array.

Input Format:
The first line of input contains an integer, that denotes the value of the size of the array. Let us denote it with the symbol n.
The following line contains n space separated integers, that denote the value of the elements of the array.
The following line contains an integer, that denotes the value of K.

Output format :
The first and only line of output contains count of all such pairs which have an absolute difference of K. 

Constraints :
0 <= n <= 10^4

Time Limit: 1 sec

Sample Input 1 :
4 
5 1 2 4
3

Sample Output 1 :
2

Sample Input 2 :
4
4 4 4 4 
0

Sample Output 2 :
6
'''

def printPairDiffK(l, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    d = {}
    for i in l:
        d[i] = d.get(i, 0) + 1

    
    count = 0
    import sympy
    if k == 0:
        return sympy.binomial(d[l[0]], 2)
    else:
        for i in l:
            if i in d and i+k in d:
                count += d[i] * d[i+k]
            if i in d and i-k in d:
                count += d[i] * d[i-k]
            if i in d:
                del d[i]
    return count
    #############################
    
# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
print(printPairDiffK(l, k))