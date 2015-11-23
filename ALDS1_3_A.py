poland = input().split()
num = []
for p in poland:
    if p.isdigit():
        num.append(int(p))
    else:
        b = num.pop()
        a = num.pop()
        if p == '*':
            num.append(a * b)
        elif p == '/':
            num.append(a / b)
        elif p == '+':
            num.append(a + b)
        elif p == '-':
            num.append(a - b)
print(num.pop())
