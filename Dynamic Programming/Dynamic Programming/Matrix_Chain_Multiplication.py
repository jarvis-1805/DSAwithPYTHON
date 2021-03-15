'''
Matrix Chain Multiplication

Given a chain of matrices A1, A2, A3,.....An, you have to figure out the most efficient way to multiply these matrices. In other words, determine where to place parentheses to minimize the number of multiplications.
You will be given an array p[] of size n + 1. Dimension of matrix Ai is p[i - 1]*p[i]. You need to find minimum number of multiplications needed to multiply the chain.

Input Format:
The first line of input contains an integer, that denotes the value of n. The following line contains n+1 integers, that denote the value of elements of array p[].

Output Format:
The first and only line of output prints the minimum number of multiplication needed.

Constraints :
1 <= n <= 100

Time limit: 1 second

Sample Input 1:
3
10 15 20 25

Sample Output 1:
8000

Sample Output Explanation:
There are two ways to multiply the chain - A1*(A2*A3) or (A1*A2)*A3.
If we multiply in order- A1*(A2*A3), then number of multiplications required are 15000.
If we multiply in order- (A1*A2)*A3, then number of multiplications required are 8000.
Thus minimum number of multiplications required are 8000. 
'''

import sys
from sys import stdin
def mcm(p,i,j,dp):
    if i == j:
        return 0
    
    min_value = sys.maxsize
    for k in range(i,j):
        if dp[i][k] == -1:
            ans1 = mcm(p,i,k,dp)
            dp[i][k] = ans1
        else:
            ans1 = dp[i][k]
        
        if dp[k+1][j] == -1:
            ans2 = mcm(p,k+1,j,dp)
            dp[k+1][j] = ans2
        else:
            ans2 = dp[k+1][j]
        
        mCost = p[i-1]*p[k]*p[j]
        curr_value = ans1 + ans2 + mCost
        min_value = min(min_value,curr_value)
    
    return min_value


n=int(stdin.readline().strip())
p=[int(i) for i in stdin.readline().strip().split()]
dp = [[-1 for j in range(n+1)] for i in range(n+1)]
print(mcm(p,1,n,dp))