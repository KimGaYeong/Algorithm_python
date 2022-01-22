from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())

def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]


def union(a, b):
    p_a, p_b  = find_parent(a), find_parent(b)
    if p_a < p_b:
        parent[p_b] = p_a
    else:
        parent[p_a] = p_b

link = []
parent = [i for i in range(N)]
cost_re = 0 #Cost of result

for i in range(M):
    c_a, c_b,c_cost = map(int, stdin.readline().split())
    link.append([c_a-1, c_b-1, c_cost])

link.sort(key=lambda x : x[2])

for edge in link:
    a, b, cost = edge[0], edge[1], edge[2]

    if find_parent(a) != find_parent(b): #부모 노드가 같으면
        union(a, b) #에지를 이어준다.
        cost_re += cost

print(cost_re)