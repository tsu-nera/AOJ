n = int(input())
c = input().split()
d = c[:]

# bubblesort
for i in range(n):
    for j in range(n - 1, i, -1):
        if d[j][1] < d[j - 1][1]:
            d[j], d[j - 1] = d[j - 1], d[j]
print(*d)
print("Stable")

# selectionsort
for i in range(n):
    minj = i
    for j in range(i, n):
        if c[j][1] < c[minj][1]:
            minj = j
    c[i], c[minj] = c[minj], c[i]

print(*c)
print("Stable" if c == d else "Not stable")
