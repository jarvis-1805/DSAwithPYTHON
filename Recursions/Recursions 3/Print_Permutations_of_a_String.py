'''
Print Permutations of a String

Given a string, find and print all the possible permutations of the input string.

Note : The order of permutations are not important. Just print them in different lines.

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

def printPermutations(string, output):
    #Implement Your Code Here
    if len(string) == 0:
        print(output)
        return
    
    for i in range(len(string)):
        printPermutations(string[0:i] + string[i+1:], output + string[i])

string = input()
printPermutations(string, '')