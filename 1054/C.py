t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)
    d = list(set(a))
    cnt = 0
    fit = 0

    for i in range(n):
        if a[i] == k:
            cnt += 1 
    
    for i in range(len(d)):
        if (d[i] < k):
            fit += 1

    more_to_fit = k - fit
    
    ans = max(more_to_fit, cnt)

    print(ans)