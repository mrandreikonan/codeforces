import statistics

t = int(input())

def calc(pos):
    if len(pos) == 0:
        return 0
    
    med_calc = [(val - index) for index, val in enumerate(pos)]
    median_value = statistics.median(med_calc)

    res = 0
    for i in range(len(pos)):
        res += abs(pos[i] - i - median_value)

    return int(res)

for _ in range(t):
    n = int(input())
    s = input()
    a_pos = []
    b_pos = []
    for i, c in enumerate(s):
        if c == 'a':
            a_pos.append(i)
        else:
            b_pos.append(i)
    
    print(min(calc(a_pos), calc(b_pos)))