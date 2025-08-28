t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    for i in range(n):
        if T[i] % k == 0:
            T[i] = 0
        elif T[i] > k:
            T[i] = min(T[i] % k, k - T[i] % k)
        else:
            T[i] = min(T[i], k - T[i])

        if S[i] % k == 0:
            S[i] = 0
        elif S[i] > k:
            S[i] = min(S[i] % k, k - S[i] % k)
        else:
            S[i] = min(S[i], k - S[i])

    S = sorted(S)
    T = sorted(T)

    ans = True
    for i in range(n):
        if S[i] != T[i]:
            ans = False
            break

    if True == ans:
        print('YES')
    else:
        print('NO')