'''
Sample Input 1:
Welcome to Coding Ninjas

Sample Output 1:
emocleW ot gnidoC sajniN

Sample Input 2:
Always indent your code

Sample Output 2:
syawlA tnedni ruoy edoc
'''

from sys import stdin


def reverseEachWord(Sentence) :
	# Your code goes here
    words = Sentence.split(" ") 
      
    newWords = [word[::-1] for word in words] 
    
    newSentence = " ".join(newWords) 
  
    return newSentence 

#main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)