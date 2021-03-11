'''
Code : Triangle of Numbers

Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines

Constraints :
0 <= N <= 50
Sample Input 1:
5
Sample Output 1:
           1
         232
       34543
     4567654
   567898765
Sample Input 2:
4
Sample Output 2:
           1
         232
       34543
     4567654
'''

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n - i:
        print(' ', end='')
        j += 1
    k = 1
    p = i
    while k <= i:
        print(p, end='')
        k += 1
        p += 1
    l = i - 1
    q = p - 2
    while l >= 1:
        print(q, end='')
        l -= 1
        q -= 1
    print()
    i += 1