t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    ans = True 
    prev = -1
    for el in a:
        if el == -1:
            continue
        elif (el == prev) or (prev == -1):
            prev = el
            continue
        else:
            ans = False
            break

    if (ans == True) and (prev != 0):
        print('YES')
    else:
        print('NO')