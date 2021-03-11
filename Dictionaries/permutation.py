'''
Given two strings, S and T, check if they are permutations of each other.
Return true or false.
Permutation means - length of both the strings should same and
should contain same set of characters.
Order of characters doesn't matter.

Sample Input 1 :
abcde
baedc

Sample Output 1 :
true

Sample Input 2 :
abc
cbd

Sample Output 2 :
false
'''
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