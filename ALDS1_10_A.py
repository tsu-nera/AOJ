n = input()

if n == 0:
    print(1)
elif n == 1:
    print(1)
else:
    fib = [0 for i in range(n + 1)]

    fib[0] = 1
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    print(fib[n])
