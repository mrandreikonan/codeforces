t = int(input())
for _ in range(t):
    l, r = map(int,input().split())

    fd2 = fd3 = fd5 = fd7 = 0
    for i in range(l,r+1):
        if fd2 > 0 and fd3 > 0 and fd5 > 0 and fd7 > 0:
            break
        if i % 2 == 0 and fd2 == 0:
            fd2 = i
        elif i % 3 == 0 and fd3 == 0:
            fd3 = i
        elif i % 5 == 0 and fd5 == 0:
            fd5 = i
        elif i % 7 == 0 and fd7 == 0:
            fd7 = i

    ld2 = ld3 = ld5 = ld7 = 0
    for i in range(r,l-1,-1):
        if ld2 > 0 and ld3 > 0 and ld5 > 0 and ld7 > 0:
            break
        if i % 2 == 0 and ld2 == 0:
            ld2 = i
        elif i % 3 == 0 and ld3 == 0:
            ld3 = i
        elif i % 5 == 0 and ld5 == 0:
            ld5 = i
        elif i % 7 == 0 and ld7 == 0:
            ld7 = i

    minfd = min([fd2, fd3, fd5, fd7])
    maxlf = max([ld2, ld3, ld5, ld7])

    d2 = (ld2-fd2)//2
    d3 = (ld3-fd3)//3
    d5 = (ld5-fd5)//5
    d7 = (ld7-fd7)//7

    d23 = d2 // 3
    d25 = d2 // 5
    d27 = d2 // 7
    d35 = d3 // 5
    d37 = d3 // 7
    d57 = d5 // 7

    d235 = d23 // 5
    d237 = d23 // 7
    d357 = d35 // 7

    d2357 = d235 // 7

    ttl = r - l + 1
    ttl += d23 + d25 + d27
    ttl += d35 + d37
    ttl += d235 + d237 + d357
    ttl += d2357
    ttl -= (minfd - l)
    ttl -= (r - maxlf)
    ttl -= (ld2-fd2)//2
    ttl -= (ld3-fd3)//3
    ttl -= (ld5-fd5)//5
    ttl -= (ld7-fd7)//7

    print(ttl)