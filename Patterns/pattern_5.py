'''
* 
 * * 
  * * * 
   * * * * 
  * * * 
 * * 
* 
'''
n = int(input())
i = 0
while i <= (n//2)+1:
    k = i
    while k > 1:
        print(' ', end='')
        k -= 1
    j = 0
    while j < i:
        print('*', end=' ')
        j += 1
    print()
    i += 1
i = 0
while i < n//2:
    k = i
    while k < (n//2) - 1:
        print(' ', end='')
        k += 1
    j = 0
    while j < (n//2)-i:
        print('*', end=' ')
        j += 1
    print()
    i += 1