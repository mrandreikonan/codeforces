t = int(input())
for _ in range(t):
    n, x = map(int,input().split())
    x -= 1
    s = input()
    fwl = fwr = -1
    walls = 0
    for idx in range(len(s)):
        if (idx < x) and (s[idx] == '#'):
            fwl = idx
        if (fwr == -1) and (idx > x) and (s[idx] == '#'):
            fwr = idx
        if (s[idx] == '#'):
            walls += 1

    if (x == 0) or (x == n-1) or (walls == 0):
        print('1')
    elif (s[x-1] == '#') or (s[x+1] == '#'):
        print(min(x,n-1-x)+1)
    else:
        if fwl == -1:
            print(min(x,n-fwr) + 1)
        elif fwr == -1:
            print(min(n-1-x,fwl+1) + 1)
        else:
            print(max(min(x,n-fwr),min(n-1-x,fwl+1))+1)