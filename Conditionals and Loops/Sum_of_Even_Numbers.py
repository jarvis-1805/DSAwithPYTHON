'''
Sum of Even Numbers

Given a number N, print sum of all even numbers from 1 to N.

Input Format :
Integer N

Output Format :
Required Sum 

Sample Input 1 :
6

Sample Output 1 :
12
'''

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
sum = 0
while i<=n:
    if i%2 == 0:
        sum = sum + i
    i = i+1
print(sum)