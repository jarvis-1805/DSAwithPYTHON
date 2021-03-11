'''
Code : Star Pattern

Print the following pattern

Input Format :
N (Total no. of rows)

Output Format :
Pattern in N lines

Constraints :
0 <= N <= 50

Sample Input 1 :
3

Sample Output 1 :
   *
  *** 
 *****

Sample Input 2 :
4

Sample Output 2 :
    *
   *** 
  *****
 *******
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
    while k <= i:
        print('*', end='')
        k += 1
    l = i - 1
    while l >= 1:
        print('*', end='')
        l -= 1
    print()
    i += 1