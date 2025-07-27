
from collections import deque

def checkBad(a):
    if a[0] > a[1] and a[1] > a[2] and a[2] > a[3] and a[3] > a[4]:
        return True
    elif a[0] < a[1] and a[1] < a[2] and a[2] < a[3] and a[3] < a[4]:
        return True
    
    return False

def solve(dq, ans, n, last_selected):
    last_popped = deque([last_selected])
    for i in range(n-4):
        # Generate next 16 combinations
        last_comb = 0
        good_found = False
        for j in range(16):
            cand = []
            last_comb = j
            l = r = 0
            for k in range(4):
                next = j & (1 << k)
                if next == 0:
                    cand.append(dq[0 + l])
                    l += 1
                else:
                    cand.append(dq[len(dq) - r - 1])
                    r += 1
            
            if last_selected > cand[0] and cand[0] > cand[1] and cand[1] > cand[2] and cand[2] > cand[3]:
               continue
            elif last_selected < cand[0] and cand[0] < cand[1] and cand[1] < cand[2] and cand[2] < cand[3]:
               continue
            elif True == checkBad(list(last_popped) + cand):
                continue
            else:
                if j & 1 == 0:
                   last_selected = dq.popleft()
                   ans.append('L')
                   last_popped.append(last_selected)
                   if len(last_popped) > 4:
                       last_popped.popleft()
                   good_found = True
                else:
                   last_selected = dq.pop()
                   ans.append('R')
                   last_popped.append(last_selected)
                   if len(last_popped) > 4:
                       last_popped.popleft()
                   good_found = True

            if good_found == True:
                break

        if good_found == False:
            return False

    # add last 3
    last_comb >> 1
    for k in range(3):
        next = last_comb & (1 << k)
        if next == 0:
            dq.popleft()
            ans.append('L')
        else:
            dq.pop()
            ans.append('R')

    print(''.join(ans))

    return True

t = int(input())
for i in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    dq = deque(p)
    ans = ['L']
    last_selected = dq.popleft()
    if False == solve(dq, ans, n, last_selected):
        dq = deque(p)
        ans = ['R']
        last_selected = dq.pop()
        if False == solve(dq, ans, n, last_selected):
            exit(1)