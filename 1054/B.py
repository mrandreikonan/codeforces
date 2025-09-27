t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    ans = 0
    for i in range(n//2):
        v = abs(a[2*i]-a[2*i+1])
        if v > ans:
            ans = v
    print(ans)
