'''
Check Armstrong

Write a Program to determine if the given number is Armstrong number or not. Print true if number is armstrong, otherwise print false.
An Armstrong number is a number (with digits n) such that the sum of its digits raised to nth power is equal to the number itself.

For example,
371, as 3^3 + 7^3 + 1^3 = 371
1634, as 1^4 + 6^4 + 3^4 + 4^4 = 1634

Input Format :
Integer n

Output Format :
true or false

Sample Input 1 :
1

Sample Output 1 :
true

Sample Input 2 :
103

Sample Output 2 :
false
'''

## Read input as specified in the question.
## Print output as specified in the question.
def power(x, y):
    if y == 0: 
        return 1
    if y % 2 == 0: 
        return power(x, y // 2) * power(x, y // 2) 

    return x * power(x, y // 2) * power(x, y // 2) 
  
def order(x): 
    n = 0
    while (x != 0): 
        n = n + 1
        x = x // 10
          
    return n 
  
def isArmstrong(x): 
      
    n = order(x) 
    temp = x 
    sum1 = 0
      
    while (temp != 0): 
        r = temp % 10
        sum1 = sum1 + power(r, n) 
        temp = temp // 10
    return (sum1 == x) 

x=int(input())
if(isArmstrong(x)):
	print('true')
else:
	print('false')
