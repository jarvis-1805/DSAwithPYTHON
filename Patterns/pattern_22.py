'''
Code : Inverted Number Pattern

Print the following pattern for the given N number of rows.
Pattern for N = 4
4444
333
22
1

Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines

Constraints :
0 <= N <= 50

Sample Input 1:
5

Sample Output 1:
55555 
4444
333
22
1

Sample Input 2:
6

Sample Output 2:
666666
55555 
4444
333
22
1
'''

## Read input as specified in the question
## Print the required output in given format
n = int(input())
i = n
while i > 0:
    j = 1
    while j <= i:
        print(i, end='')
        j += 1
    print()
    i -= 1