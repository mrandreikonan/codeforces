t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    negNum = 0
    ans = 0
    for i in range(n):
        if a[i] == 0:
            ans += 1
        elif a[i] == -1:
            negNum +=1
    
    if (negNum % 2) != 0:
        ans += 2
    
    print(ans)