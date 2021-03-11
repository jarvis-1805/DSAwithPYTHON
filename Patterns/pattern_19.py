'''
Number Pattern 3

Print the following pattern for the given N number of rows.
Pattern for N = 4
1
11
121
1221

Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines

Sample Input :
5

Sample Output :
1
11
121
1221
12221
'''

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
if n:
    print(i)
while i < n:
    j = 1
    print(1, end='')
    while j < i:
        print(2, end='')
        j += 1
    print(1)
    i += 1