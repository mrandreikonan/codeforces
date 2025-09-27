t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = 0
    zero_count = 0
    for ch in s:
        if ch == '0':
            zero_count += 1

    for i in range(zero_count):
        if s[i] == '1':
            ans += 1

    print(ans)