# ChatGPT Рашэнне задачы "Double Perspective" з выкарыстаннем DSU (Disjoint Set Union)
# Мэта: выбраць набор пар так, каб граф быў лесам (без цыклаў), а пакрыццё інтэрвалаў было максімальным.

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = []

    for _ in range(t):
        n = int(data[index])
        index += 1
        pairs = []
        max_val = 0
        for _ in range(n):
            a = int(data[index])
            b = int(data[index + 1])
            index += 2
            pairs.append((a, b))
            max_val = max(max_val, a, b)

        # Ініцыялізуем DSU для ўсіх магчымых вяршынь
        dsu = DSU(2 * max_val + 1)
        selected = []

        # Сартуем пары па левым канцы інтэрвалу (гэта гарантуе greedy-упарадкаванне)
        sorted_pairs = sorted(enumerate(pairs), key=lambda x: x[1][0])

        for idx, (a, b) in sorted_pairs:
            # Калі дадаванне пары не стварае цыкл — уключаем у адказ
            if dsu.union(a, b):
                selected.append(idx + 1)  # +1, бо індэксы ў адказе — 1-базаваныя

        # Захоўваем вынік для кожнага тэсту
        results.append((len(selected), selected))

    # Вывад вынікаў у фармаце Codeforces
    for k, indices in results:
        print(k)
        if k > 0:
            print(' '.join(map(str, indices)))

# Простая рэалізацыя DSU з path compression і union by rank
class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        # Знаходзім караня кампненты (з аптымізацыяй шляху)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Аб’ядноўваем дзве кампаненты, калі яны яшчэ не злучаныя
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return False  # Пара злучае вяршыні ў адной кампаненце → цыкл
        if self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        else:
            self.parent[yr] = xr
            if self.rank[xr] == self.rank[yr]:
                self.rank[xr] += 1
        return True

main()