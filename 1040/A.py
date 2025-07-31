t = int(input())
for _ in range(t):

    n = int(input())
    s = list(map(int, input().split()))

    ans = 0
    zeroes = 0
    ones = 0

    for el in s:
        if el == 0:
            zeroes += 1
        elif el == 1:
            ones += 1
        else:
            ans += el
    
    ans += min(zeroes, ones) * 2
    ans += abs(zeroes - ones)

    print(ans)