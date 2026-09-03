arr = [3, 9, 20, 5]
n = len(arr)
power_set = []
for i in range(2 ** n):
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(arr[j])

    power_set.append(subset)

print(power_set)
