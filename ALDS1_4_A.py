n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))


def linearSearch(A, n, key):
    i = 0
    A.append(key) # 番兵
    while A[i] != key:
        i += 1
    A.pop()
    return i != n

count = 0

for i in range(q):
    if linearSearch(S, n, T[i]):
        count += 1

print(count)
