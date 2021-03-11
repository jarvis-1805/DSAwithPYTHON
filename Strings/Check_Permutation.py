'''
Check Permutation
Send Feedback
For a given two strings, 'str1' and 'str2', check whether they are a permutation of each other or not.
Permutations of each other
Two strings are said to be a permutation of each other when either of the string's characters can be rearranged so that it becomes identical to the other one.

Example: 
str1= "sinrtg" 
str2 = "string"

The character of the first string(str1) can be rearranged to form str2 and hence we can say that the given strings are a permutation of each other.
Input Format:
The first line of input contains a string without any leading and trailing spaces, representing the first string 'str1'.

The second line of input contains a string without any leading and trailing spaces, representing the second string 'str2'.
Note:
All the characters in the input strings would be in lower case.
Output Format:
The only line of output prints either 'true' or 'false', denoting whether the two strings are a permutation of each other or not.

You are not required to print anything. It has already been taken care of. Just implement the function. 
Constraints:
0 <= N <= 10^6
Where N is the length of the input string.

Time Limit: 1 second
Sample Input 1:
abcde
baedc
Sample Output 1:
true
Sample Input 2:
abc
cbd
Sample Output 2:
false
'''

## Read input as specified in the question.
## Print output as specified in the question.
s1 = input()
s2 = input()
dic = {}
if len(s1) == len(s2):
    for i in s1:
        if i in dic:
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1
    for i in s2:
        if i in dic:
            dic[i] = dic[i] - 1
    for i in dic:
        if dic[i] == 0:
            pass
        else:
            print('false')
            break
    else:
        print('true')
else:
    print('false')