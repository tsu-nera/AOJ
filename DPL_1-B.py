N, W = map(int, raw_input().split())

v = [0] * N
w = [0] * N
dp = [[0 for i in range(W + 1)] for j in range(N + 1)]

for i in range(N):
    v[i], w[i] = map(int, raw_input().split())

for i in range(N - 1, -1, -1):
    for j in range(W + 1):
        if j < w[i]:
            dp[i][j] = dp[i + 1][j]
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j - w[i]] + v[i])

print(dp[0][W])
