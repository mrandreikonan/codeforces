t = int(input())
for _ in range(t):
    s = input()
    nF = nT = nN = 0
    res = ''
    for ch in s:
        if ch == 'N':
            nN += 1
        elif ch == 'F':
            nF += 1
        elif ch == 'T':
            nT +=1
        else:
            res += ch

    non_dif = ''
    # Add FTFTFT
    minFT = min(nF,nT)
    for i in range(minFT):
        non_dif += 'FT'
    nF -= minFT
    nT -= minFT
    # Add TNTNTN
    minNT = min(nN,nT)
    for i in range(minNT):
        non_dif += 'TN'
    nN -= minNT
    nT -= minNT

    sN = 'N'*nN
    sF = 'F'*nF
    sT = 'T'*nT

    print(sT + sN + non_dif + sF + res)

    