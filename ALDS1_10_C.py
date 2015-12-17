def lcs():
    A = raw_input()
    B = raw_input()

    m = len(A)
    n = len(B)

    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

    maxl = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            maxl = max(maxl, dp[i][j])

    return maxl

n = input()
for _ in range(n):
    print lcs()
