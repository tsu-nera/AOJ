N, W = map(int, raw_input().split())

v = [0] * N
w = [0] * N
dp = [[-1 for i in range(W + 1)] for j in range(N + 1)]

for i in range(N):
    v[i], w[i] = map(int, raw_input().split())


def rec(i, j):
    if dp[i][j] != -1:
        return dp[i][j]

    if i == N:
        res = 0
    elif j < w[i]:
        res = rec(i + 1, j)
    else:
        res = max(rec(i + 1, j), rec(i + 1, j - w[i]) + v[i])

    dp[i][j] = res
    return res

print(rec(0, W))
