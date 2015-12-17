class Node:
    def __init__(self,p,l,r):
        self.parent = p
        self.left = l
        self.right = r

n = int(input())
tree = {}
for i in range(n):
    nid, left, right = map(int, input().split())
    if nid not in tree:
        tree[nid] = Node(-1, left, right)
    else:
        tree[nid].left = left
        tree[nid].right = right
    if not left == -1:
        if left not in tree:
            tree[left] = Node(nid, -1, -1)
        else:
            tree[left].parent = nid
    if not right == -1:
        if right not in tree:
            tree[right] = Node(nid, -1, -1)
        else:
            tree[right].parent = nid

r = -1
for i in range(len(tree)):
    if tree[i].parent == -1:
        r = i
        break
