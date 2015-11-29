def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1

n = int(input())
a = list(map(int, input().split()))
m = partition(a, 0, n-1)
a = list(map(str, a))
a[m] = "[%s]"%(a[m])
print(" ".join(a))
