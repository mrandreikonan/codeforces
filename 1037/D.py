import heapq
from collections import deque


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = []
    heap = []
    for i in range(n):
        l, r, real = map(int, input().split())
        if (l <= k) and (k <= r):
            heapq.heappush(heap, (-real, l, r))
        else:
            a.append((l, r, real))

    casino = deque(sorted(a))

    ans = k

    while True:
        if len(heap) == 0:
            break
        
        best_next = heapq.heappop(heap)

        if abs(best_next[0]) <= ans:
            break
        else:
            ans = abs(best_next[0])

        heap = []

        cnt = len(casino)
        for i in range(cnt):
            c = casino.popleft()
            if (c[0] <= ans) and (ans <= c[1]):
                heapq.heappush(heap, (-c[2], c[0], c[1]))
            else:
                casino.append(c)
    
    print(ans)