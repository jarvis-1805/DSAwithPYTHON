'''
Pyramid Number Pattern

Print the following pattern for the given number of rows.
Pattern for N = 4
   1
  212
 32123
4321234

Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :
5

Sample Output :
        1
      212
    32123
  4321234
543212345
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
    k = i
    while k >= 1:
        print(k, end='')
        k -= 1
    l = k+2
    while l <= i:
        print(l, end='')
        l += 1
    print()
    i += 1