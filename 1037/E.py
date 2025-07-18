import math
from functools import reduce

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    s = list(map(int, input().split()))

    a = [0]*n
    for i in range(n):
        a[i] = math.lcm(p[i], s[i])
    
    ans = True

    # pre compute prefix and suffix
    prefix = [0] * n
    suffix = [0] * n

    prefix[0] = a[0]
    for i in range(1,n):
        prefix[i] = math.gcd(prefix[i-1],a[i])
    
    suffix[-1] = a[-1]
    for i in range(n-2, -1, -1):
        suffix[i] = math.gcd(suffix[i+1], a[i]) 

    # verify prefixes and suffixes
    for i in range(n):
        if (prefix[i] == p[i]) and (suffix[i] == s[i]):
            continue
        else:
            ans = False
            break

    if False == ans:
        print('NO')
    else:
        print('YES')