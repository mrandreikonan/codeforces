import sys

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0

    for i in range(n):
        if a[i] > b[i]:
            t = a[i]
            a[i] = b[i]
            b[i] = t
        ans += b[i]-a[i]

    order = [i for i in range(n)]
    order = sorted(order, key=lambda i: a[i])

    mn = sys.maxsize
    for i in range(n-1):
        diff = a[order[i+1]]-b[order[i]]
        if (diff < mn):
            mn = diff
    mn = max(0,mn)

    ans += 2*mn

    print(ans)