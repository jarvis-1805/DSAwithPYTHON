'''
Number Pattern 2
Send Feedback
Print the following pattern for the given N number of rows.
Pattern for N = 4
1
11
202
3003
Input format :
Integer N (Total no. of rows)
Contraints:
1 <= n <= 50
Output format :
Pattern in N lines
Sample Input :
5
Sample Output :
1
11
202
3003
40004
'''

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
print(i)
while i < n:
    j = 1
    print(i, end='')
    while j < i:
        print(0, end='')
        j += 1
    print(i)
    i += 1