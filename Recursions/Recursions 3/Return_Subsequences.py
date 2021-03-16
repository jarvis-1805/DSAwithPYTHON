'''
Return Subsequences

Given a string (lets say of length n), return all the subsequences of the given string.
Subsequences contain all the strings of length varying from 0 to n. But the order of characters should remain same as in the input string.

Note : The order of subsequences are not important.

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

def subsequences(s):
    #Implement Your Code Here
    if len(s) == 0:
        output = []
        output.append("")
        return output
    
    smallerString = s[1:]
    smallerOutput = subsequences(smallerString)
    
    output = []
    for sub in smallerOutput:
        output.append(sub)
        
    for sub in smallerOutput:
        subs_with_zeroth_char = s[0] + sub
        output.append(subs_with_zeroth_char)
    
    return output


string = input()
ans = subsequences(string)
for ele in ans:
    print(ele)