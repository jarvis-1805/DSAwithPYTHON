'''
Print Subsequences

Given a string (lets say of length n), print all the subsequences of the given string.
Subsequences contain all the strings of length varying from 0 to n. But the order of characters should remain same as in the input string.

Note :
The order of subsequences are not important. Print every subsequence in new line.

Input format
The input only consists of one line which consists of a single string
Output format
The output consists of all subsequences of the input string where each subsequence is printed in a different line. The order of the subsequences doesn't matter

Constraints
1 <= |S| <= 15
where |S| represents the length of the input string

Time limit: 1 sec

Sample Input:
abc

Sample Output:
"" (the double quotes just signifies an empty string, don't worry about the quotes)
c 
b 
bc 
a 
ac 
ab 
abc 
'''

## Read input as specified in the question.
## Print output as specified in the question.
def printSubs(s, o):
    if len(s) == 0:
        print(o)
        return
    
    # Don't include 0th char
    printSubs(s[1:], o)
    
    # Include 0th char
    newOutput = o + s[0]
    printSubs(s[1:], newOutput)

s = input()
printSubs(s, "")