t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    m = int(input())
    b = input()
    c = input()

    for idx in range(m):
        if c[idx] == 'V':
            a = b[idx] + a
        else:
            a = a + b[idx]

    print(a)