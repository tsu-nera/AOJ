while True:
    a = list(map(int, input().strip().split()))
    a.sort()
    if (a[0] == 0 and a[1] == 0):
        break
    print(a[0], a[1])
