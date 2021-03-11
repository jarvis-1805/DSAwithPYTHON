'''
1        1
12      21
123    321
1234  4321
1234554321
'''
n = int(input())
i = 1
while i<=n:
    j=1
    while j<=i:
        print(j, end='')
        j += 1
    k = 1
    while k <= (n-i)*2:
        print(' ', end='')
        k += 1
    l = i
    while l >= 1:
        print(l, end='')
        l -= 1
    print()
    i += 1