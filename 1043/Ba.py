MAX_DIGIT = 18
t = int(input())
for _ in range(t):
    n = int(input())
    ans = []
    for i in range(1, MAX_DIGIT):
        if (n % (pow(10, i) + 1)) == 0:
            ans.append(n // (pow(10, i) + 1))

    print(len(ans))
    ans = sorted(ans)
    for an in ans:
        print(str(an) + ' ', end='')
    print()