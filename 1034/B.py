import bisect

t = int(input())
for _ in range(t):
    n, j, k = map(int, input().split())
    a = list(map(int, input().split()))
    j_w = a[j-1]
    a.sort()

    weaker_or_same_inclusive_count = bisect.bisect_right(a, j_w)
    stronger_count = n - weaker_or_same_inclusive_count
    
    jth_can_last = 0
    jth_can_last += weaker_or_same_inclusive_count - 1 # win all weaker or same
    if stronger_count > 0:
        jth_can_last += stronger_count - 1             # wait for strong fight between themselves before losing to them

    if k >= n - jth_can_last:
        print('YES')
    else:
        print('NO')