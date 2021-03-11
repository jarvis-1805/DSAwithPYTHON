'''
Remove Duplicates Recursively

Given a string S, remove consecutive duplicates from it recursively.

Input Format :
String S

Output Format :
Output string

Constraints :
1 <= |S| <= 10^3
where |S| represents the length of string

Sample Input 1 :
aabccba

Sample Output 1 :
abcba


Sample Input 2 :
xxxyyyzwwzzz

Sample Output 2 :
xyzwz
'''

# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(s):
    # Please add your code here
    if len(s) == 0 or len(s) == 1:
        return s
    if s[0] == s[1]:
        smallOutput = removeConsecutiveDuplicates(s[1:])
        return smallOutput
    else:
        smallOutput = removeConsecutiveDuplicates(s[1:])
        return s[0] + smallOutput

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
