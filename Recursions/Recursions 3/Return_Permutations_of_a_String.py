'''
Return Permutations of a String

Given a string, find and return all the possible permutations of the input string.

Note : The order of permutations are not important.

Sample Input :
abc

Sample Output :
abc
acb
bac
bca
cab
cba
'''

def permutations(string):
    #Implement Your Code Here
    if len(string) == 1:
        return [string]
    
    temp = permutations(string[1:])
    
    output = []
    for i in temp:
        for j in range(len(i)+1):
            smallString = i[:j] + string[0] + i[j:]
            output.append(smallString)
    
    return output


string = input()
ans = permutations(string)
for s in ans:
    print(s)