import bisect

t = int(input())
for _ in range(t):
    n = int(input)
    p = list(map(int,input().split()))
    a = []
    l = []
    r = sorted(p)
    for i in range(n):
        inv_curr = (len(l) - bisect.bisect_left(l, p[i])) + bisect.bisect_right(r,p[i])
        inv_op   = (len(l) - bisect.bisect_left(l, 2*n - p[i])) + bisect.bisect_right(r,2*n - p[i])

        val = 0

        if inv_op < inv_curr:
            val = 2*n-p[i]
        else:
            val = p[i]
        
        a.append(val)
        ins_idx = bisect.insort(l,val)
        
        