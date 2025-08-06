# Згенеравана ChatGPT — Пераклад аўтарскага рашэння з C++ на Python
# Задача "D. Stay or Mirror" — просты падлік колькасці інверсій
# Для кожнага p[i] лічым колькі большае за яго злева і справа

import sys
input = sys.stdin.read

def solve():
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1

    results = []

    for _ in range(t):
        n = int(data[idx])
        idx += 1
        p = list(map(int, data[idx:idx+n]))
        idx += n

        ans = 0

        for i in range(n):
            left = 0
            right = 0
            # Лічым колькі p[j] > p[i] злева
            for j in range(i):
                if p[j] > p[i]:
                    left += 1
            # І справа
            for j in range(i+1, n):
                if p[j] > p[i]:
                    right += 1
            ans += min(left, right)

        results.append(str(ans))

    print('\n'.join(results))

solve()