from collections import deque

n, qt = map(int, input().split())

queue = deque()

for i in range(n):
    name, time = input().split()
    queue.append([name, int(time)])

total_time = 0

while queue:
    q_t = queue.popleft()
    if q_t[1] <= qt:
        total_time += q_t[1]
        print(q_t[0], total_time)
    else:
        total_time += qt
        q_t[1] -= qt
        queue.append(q_t)
