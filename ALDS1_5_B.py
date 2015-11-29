def merge(A, left, mid, right):
    global count
    L = A[left:mid] + [1000000001]
    R = A[mid:right] + [1000000001]
    i = j = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    count += right - left


def merge_sort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)

N = int(input())
A = list(map(int, input().split()))
count = 0
merge_sort(A, 0, N)
print(*A)
print(count)
