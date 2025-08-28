t = int(input())
for _ in range(t):
    n = int(input())
    if n == 2:
        print('-1 2')
    elif n == 3:
        print('-1 3 -1')
    elif n % 2 == 0:
        for i in range(n-1):
            if i % 2 == 0:
                print('-1 ', end='')
            else:
                print('3 ', end='')
        print('2')
    else:
        for i in range(n-1):
            if i % 2 == 0:
                print('-1 ', end='')
            else:
                print('3 ', end='')
        print('-1')