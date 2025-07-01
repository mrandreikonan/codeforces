t = int(input())
for test in range(t):
    n, s = map(int, input().split())
    x = list(map(int, input().split()))
    if (s <= x[0]):
        ans = x[n-1] - s
    elif (s >= x[n-1]):
        ans = s - x[0]
    else:
        ans = min(s - x[0], x[n-1] - s) + (x[n-1] - x[0])
    print(ans)