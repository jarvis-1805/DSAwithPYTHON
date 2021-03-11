'''
123456
 23456
  3456
   456
    56
     6
    56
   456
  3456
 23456
123456
'''
n = int(input())
for i in range(0, n, 1):
    if i != 0:
        for j in range(0, i, 1):
            print(' ', end='')
    for k in range(i+1, n+1, 1):
        print(k, end='')
    print()

for i in range(n-1, 0, -1):
    for j in range(i-1, 0, -1):
        print(' ', end='')
    for k in range(i, n+1, 1):
        print(k, end='')
    print()