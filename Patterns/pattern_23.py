'''
Code : Mirror Number Pattern

Print the following pattern for the given N number of rows.

Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines

Constraints
0 <= N <= 50

Sample Input 1:
3

Sample Output 1:
      1 
    12
  123

Sample Input 2:
4

Sample Output 2:
      1 
    12
  123
1234
'''

## Read input as specified in the question
## Print the required output in given format
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n - i:
        print(' ', end='')
        j += 1
    k = 1
    while k <= i:
        print(k, end='')
        k += 1
    print()
    i += 1