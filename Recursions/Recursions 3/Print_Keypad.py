'''
Print Keypad

Given an integer n, using phone keypad find out and print all the possible strings that can be made using digits of input n.

Note : The order of strings are not important. Just print different strings in new lines.

Input Format :
Integer n

Output Format :
All possible strings in different lines

Constraints :
1 <= n <= 10^6

Sample Input:
23

Sample Output:
ad
ae
af
bd
be
bf
cd
ce
cf
'''

## Read input as specified in the question.
## Print output as specified in the question.
def getString(d):
    if d == 2:
        return "abc"
    if d == 3:
        return "def"
    if d == 4:
        return "ghi"
    if d == 5:
        return "jkl"
    if d == 6:
        return "mno"
    if d == 7:
        return "pqrs"
    if d == 8:
        return "tuv"
    if d == 9:
        return "wxyz"

def printKeypad(n, outputSoFar):
    if n == 0:
        print(outputSoFar)
        return
    smallNumber = n // 10
    lastDigit = n % 10
    
    optionsForLastDigit = getString(lastDigit)
    for c in optionsForLastDigit:
        newOutput = c + outputSoFar
        printKeypad(smallNumber, newOutput)
        
n = int(input())
printKeypad(n, "")