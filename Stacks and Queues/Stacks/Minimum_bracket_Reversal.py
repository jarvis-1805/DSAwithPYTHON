'''
Minimum bracket Reversal

For a given expression in the form of a string, find the minimum number of brackets that can be reversed in order to make the expression balanced. The expression will only contain curly brackets.
If the expression can't be balanced, return -1.

Example:

Expression: {{{{
If we reverse the second and the fourth opening brackets, the whole expression will get balanced. Since we have to reverse two brackets to make the expression balanced, the expected output will be 2.

Expression: {{{
In this example, even if we reverse the last opening bracket, we would be left with the first opening bracket and hence will not be able to make the expression balanced and the output will be -1.

Input Format :
The first and the only line of input contains a string expression, without any spaces in between.

Output Format :
The only line of output will print the number of reversals required to balance the whole expression. Prints -1, otherwise.

Note:
You don't have to print anything. It has already been taken care of.

Constraints:
0 <= N <= 10^6
Where N is the length of the expression.

Time Limit: 1sec

Sample Input 1:
{{{

Sample Output 1:
-1

Sample Input 2:
{{{{}}

Sample Output 2:
1
'''

from sys import stdin

def countBracketReversals(expr) :
    # Your code goes here
    length = len(expr)
    if length % 2: 
        return -1
    stack = []
    c = 0
    for i in range(length):
        if expr[i] is '{':
            stack.append(expr[i])
        elif expr[i] is '}':
            if not stack:
                stack.append(expr[i])
            elif stack and stack[-1] is '{':
                stack.pop()
            elif stack and stack[-1] is not '{':
                stack.append(expr[i])
    while stack:
        c1 = stack.pop()
        c2 = stack.pop()
        if c1 == c2:
            c += 1
        else:
            c += 2
    return c

#main
print(countBracketReversals(stdin.readline().strip()))