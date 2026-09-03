L = list(range(10,0,-1))

for i in enumerate(L):
    print(i)

print()

idx = 0
for val in L:
    print((idx,val))
    idx += 1

