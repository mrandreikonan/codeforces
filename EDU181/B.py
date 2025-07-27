import math

t = int(input())
for _ in range(t):
    a, b, k = map(int, input().split())
    gcd_ab = math.gcd(a,b)

    if (a <= k) and (b <= k):
        print('1')
    elif (gcd_ab > 1) and (a / gcd_ab <= k) and (b / gcd_ab <= k):
        print('1')
    else:
        print('2')