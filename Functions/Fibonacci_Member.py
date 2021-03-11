'''
Fibonacci Member

Given a number N, figure out if it is a member of fibonacci series or not. Return true if the number is member of fibonacci series else false.
Fibonacci Series is defined by the recurrence
    F(n) = F(n-1) + F(n-2)
where F(0) = 0 and F(1) = 1

Input Format :
Integer N

Output Format :
true or false

Constraints :
0 <= n <= 10^4

Sample Input 1 :
5

Sample Output 1 :
true

Sample Input 2 :
14

Sample Output 2 :
false    
'''


def checkMember(n):
    if n==0:
        return True
    x1=5*n*n + 4
    x2=5*n*n - 4
    s1 = int(x1**0.5)
    s2 = int(x2**0.5)
    if s1*s1 == x1 or s2*s2 == x2:
        return True
    else:
        return False

n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")