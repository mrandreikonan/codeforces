from sortedcontainers import SortedList

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    min_left = SortedList()
    max_right = SortedList()

    for i in range(1,n):
        min_left.ad
        heapq.heappush(max_right_heap,-a[i])

    for i in range(n):
        if (i == 0) or (i == n-1):
            print('1', end='')
        else:
            if (a[i] > min_left_heap[0]) and (a[i] < max_right_heap[0]):
                print('0', end='')
            else:
                print('1', end='')

        heapq.heappop(max_right_heap)

        heapq.heappush(min_left_heap, a[i])
    print()
        
#TODO