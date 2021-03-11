'''
Sample Input 1:
aabccbaa
a

Sample Output 1:
bccb

Sample Input 2:
xxyyzxx
y

Sample Output 2:
xxzxx
'''

from sys import stdin


def removeAllOccurrencesOfChar(string, ch) :
	# Your code goes here
    st = ''
    for i in string:
        if ch == i:
            pass
        else:
            st += i
    return st

#main
string = stdin.readline().strip()
ch = stdin.readline().strip()[0]

ans = removeAllOccurrencesOfChar(string, ch)

print(ans)