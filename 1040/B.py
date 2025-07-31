t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    count = [0, 0, 0]
    sm = 0
    for el in a:
        count[el] += 1
        sm += el

    if s < sm:
        for i in range(n):
            print(a[i], end="")
            print(' ', end="")
        print('')
    elif s == sm:
        print('-1')
    else:
        # s > sm
        # Only possible case to solve is plus one preventable and s - sum == 1
        if (s == sm + 1):
            for i in range(count[0]):
                print('0 ', end="")
            for i in range(count[2]):
                print('2 ', end="")
            for i in range(count[1]):
                print('1 ', end="")
            print('')
        else:
            print('-1')