'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

n = int(input())
i = 0
while i < (n//2) + 1:
    j = 1
    while j <= (n//2) - i:
        print(' ', end='')
        j += 1
    k = 0
    while k <= i:
        print('*', end='')
        k += 1
    l = i
    while l >= 1:
        print('*', end='')
        l -= 1
    print()
    i += 1
i = 0
while i < (n//2):
    j = 0
    while j <= i:
        print(' ', end='')
        j += 1
    k = 1
    while k <= (n//2) - i:
        print('*', end='')
        k += 1
    l = 0
    while l < (n//2) - i - 1:
        print('*', end='')
        l += 1
    print()
    i += 1