t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    hikes = 0
    good_strike = 0
    rest = False

    for day in a:
        if rest == True:
            rest = False
            continue

        if day == 0:
            good_strike += 1
        else:
            good_strike = 0

        if good_strike == k:
            hikes +=1
            rest = True
            good_strike = 0

    print(hikes)