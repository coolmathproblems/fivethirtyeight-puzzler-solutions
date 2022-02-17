import functools, operator

def sum_consecutive(start, number):
    return functools.reduce(operator.add, range(start, start + number), 0)

sums = []

for i in range(0, 100):
    sums.append([])
    for j in range(0, 100):
        sums[i].append(sum_consecutive(i, j))

results = []
for n in range(0, 4950):
    results.append([])
    for i in range(0, 100):
        for j in range(0, 100):
            if sums[i][j] == n and j > 1 and i > 0:
                results[n].append([i, j])

for x in range(30, 4950):
    if len(results[x]) > 3:
        print(f"{x} is trapezoidal {len(results[x])} times")
