import sys

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    r = []
    ans = 0

    for i in range(n):
        r.append((a[i],b[i]))
        ans += abs(a[i]-b[i])

    rs = sorted(r)

    best_min_dif = sys.maxsize
    best_i = -1
    best_j = -1

    for i in range(n):
        for j in range(i+1,n):
            dif = abs( abs(r[i][0]-r[i][1]) + abs(r[j][0]-r[j][1]) - max([abs(r[i][0]-r[j][0]) + abs(r[i][1]-r[j][1]),
                           abs(r[i][0]-r[i][1]) + abs(r[j][0]-r[j][1]),
                           abs(r[i][0]-r[j][1]) + abs(r[j][0]-r[i][1])]))
            if dif < best_min_dif:
                best_min_dif = dif
                best_i = i
                best_j = j
    
    ans += best_min_dif

    print(ans)