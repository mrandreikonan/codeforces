t = int(input())
for _ in range(t):
    ans = 10
    x = int(input())
    while x > 0:
        d = x % 10
        if d < ans:
            ans = d
        x = x // 10
    print(ans)