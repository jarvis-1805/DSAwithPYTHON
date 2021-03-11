'''
Sample Input 1:
aaabbccdsa

Sample Output 1:
a3b2c2dsa

Sample Input 2:
aaabbcddeeeee

Sample Output 2:
a3b2cd2e5
'''


from sys import stdin


def getCompressedString(message) :
	# Your code goes here
    encoded_message = "" 
    i = 0
   
    while (i <= len(message)-1): 
        count = 1
        ch = message[i] 
        j = i 
        while (j < len(message)-1): 
            if (message[j] == message[j+1]): 
                count = count+1
                j = j+1
            else: 
                break
        if count == 1:
            encoded_message=encoded_message+ch
        else:
            encoded_message=encoded_message+ch+str(count)
        i = j+1
    return encoded_message 

#main
string = stdin.readline().strip();
ans = getCompressedString(string)

print(ans)