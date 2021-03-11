for i in range(-4, 0):
    for j in range(0, abs(i)):
        print('*', end = ' ')
    print()

for i in range(0, 4):
    for j in range(-4, i-3):
        print(-j*2, end = ' ')
    print()

for i in range(0, 7):
    for j in range(0, 7):
        if i == 0 or j == 0 or i == 6 or j == 6:
            print('# ', end = '')
        else:
           print(' ', end = ' ')
    print()

for i in range(0, 7):
    for j in range(0, 7):
        if i == 0 or i == 6 or i == j:
            print('# ', end = '')
        else:
            print('  ', end = '')
    print()

for i in range(0, 7):
    for j in range(0, 7):
        if i == 0 or i == 6 or i+j == 6:
            print('# ', end = '')
        else:
            print('  ', end = '')
    print()