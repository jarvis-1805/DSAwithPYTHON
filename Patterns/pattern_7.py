'''
11111
0000
111
00
1
'''
n = int(input())
for i in range(0, n, 1):
    for j in range(0, n-i, 1):
        if i%2 == 0:
            print(1, end='')
        else:
            print(0, end='')
    print()