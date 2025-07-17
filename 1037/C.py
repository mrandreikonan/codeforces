
import bisect

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    start_h = a[k-1]
    h = sorted(set(a))
    max_h = h[len(h)-1]
    index = bisect.bisect_right(h, start_h) - 1
    water_level = 1
    ans = False

    while True:
        if h[index] == max_h:
            ans = True
            break

        if (h[index+1] - h[index] - 1 > h[index] - water_level):
            ans = False
            break
        else:
            water_level += h[index+1] - h[index]
            index += 1

    if True == ans:
        print('YES')
    else:
        print('NO')