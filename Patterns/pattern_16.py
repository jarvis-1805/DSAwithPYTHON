'''
Code : Interesting Alphabets

Print the following pattern for the given number of rows.
Pattern for N = 5
E
DE
CDE
BCDE
ABCDE

Input format :
N (Total no. of rows)

Output format :
Pattern in N lines

Constraints
0 <= N <= 26

Sample Input 1:
8

Sample Output 1:
H
GH
FGH
EFGH
DEFGH
CDEFGH
BCDEFGH
ABCDEFGH

Sample Input 2:
7

Sample Output 2:
G
FG
EFG
DEFG
CDEFG
BCDEFG
ABCDEFG
'''

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
x = chr(ord('A') + n -1)
while i <= n:
    j = 1
    sc = chr(ord(x) - i + 1)
    while j <= i:
        c = chr(ord(sc) + j - 1)
        print(c, end='')
        j += 1
    print()
    i += 1