n = int(input())

dic = set()

for i in range(n):
    cmd, key = input().split()
    if cmd == "find":
        if key in dic:
            print("yes")
        else:
            print("no")
    else:
        dic.add(key)
