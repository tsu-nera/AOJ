n = int(input())
S = set(map(int, input().split()))
q = int(input())
T = set(map(int, input().split()))
 
print(len(S & T))
