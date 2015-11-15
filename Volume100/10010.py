while True:
    (a, op, b) = input().split()
    a = int(a)
    op = str(op)
    b = int(b)

    if (op == '+'):
        print(a+b)
    elif(op == '-'):
        print(a-b)
    elif(op == '*'):
        print(a*b)
    elif(op == '/'):
        print(int(a/b))
    else:
        break
