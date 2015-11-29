def selection_sort(A, N):
    count = 0
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if(A[minj] > A[j]):
                minj = j
        if(minj != i):
            count += 1
            A[minj], A[i] = A[i], A[minj]

    print(" ".join(map(str, A)))
    print(count)

N = int(input())
A = list(map(int, input().split()))
selection_sort(A, N)
