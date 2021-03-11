'''
Sample Input 1:
aabccbaa

Sample Output 1:
abcba

Sample Input 2:
xxyyzxx

Sample Output 2:
xyzx
'''

S = list(input())
n = len(S)

j = 0

for i in range(n):
    if (S[j] != S[i]): 
        j += 1
        S[j] = S[i]  
j += 1
S = S[:j]
print(*S, sep='')