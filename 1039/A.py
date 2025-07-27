import bisect

t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    in_a = list(map(int, input().split()))
    a = sorted(in_a)

    cost = 0

    for i in range(n):
        search_idx = bisect.bisect_right(a, c)
        if search_idx == 0:
            break
        else:
            a = a[0:search_idx-1] + a[search_idx:len(a)]

        for j in range(len(a)):
            a[j] *= 2

    cost += len(a)

    print(cost)