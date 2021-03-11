'''
Sample Input 1:
abdefgbabfba

Sample Output 1:
b

Sample Input 2:
xy

Sample Output 2:
x
'''

from sys import stdin


def highestOccuringChar(str) :
	#Your code goes here
    count = [0] * 256 
  
    # Utility variables 
    max = -1
    c = '' 
  
    # Traversing through the string and maintaining the count of 
    # each character 
    for i in str: 
        count[ord(i)]+=1; 
  
    for i in str: 
        if max < count[ord(i)]: 
            max = count[ord(i)] 
            c = i 
  
    return c

#main
string = stdin.readline().strip();
ans = highestOccuringChar(string)

print(ans)