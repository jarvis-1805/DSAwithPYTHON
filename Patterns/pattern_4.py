'''
    1
   212
  32123
 4321234
543212345
'''
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n - i:
        print(' ', end='')
        j += 1
    k = i
    while k >= 1:
        print(k, end='')
        k -= 1
    l = k+2
    while l <= i:
        print(l, end='')
        l += 1
    print()
    i += 1