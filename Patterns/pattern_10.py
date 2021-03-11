'''
Pattern for N = 5
 1    2   3    4   5
 11   12  13   14  15
 21   22  23   24  25
 16   17  18   19  20
 6    7    8   9   10

Pattern for N = 4
 1  2  3  4
 9 10 11 12
13 14 15 16
 5  6  7  8
'''
n = int(input())
i = 1
x = 1
for i in range(1, n+1):
    for j in range(x, x+n, 1):
        print(j, end=' ')
    print()
    if(i==((n+1)//2)):
        if((n%2) != 0):
            x = n*(n-2)+1
        else:
            x = n*(n-1)+1
    elif((i>(n+1)//2)):
        x = x - 2*n
    else:
        x = x + 2*n