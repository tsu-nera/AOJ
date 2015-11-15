n = int(input())
array = list(input().split())
array.reverse()
 
for i in range(n - 1):
    print(array[i] + " ", end = "")

print (array[n - 1])
