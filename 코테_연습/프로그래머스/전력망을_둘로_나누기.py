# https://school.programmers.co.kr/learn/courses/30/lessons/86971
# 나의 풀이 - 맞췄지만 개선이 많이 필요한 코드
# 코드 설명
# 1. 먼저 전체 노드 목록을 찾는다 (nodes)
# 2. 노드 목록을 순회하면서 각 노드를 기준으로 그래프를 만든다 (graph)
# 3. 순회하면서 끊을 간선을 선정한다 (arr)
# 4. 방문 여부를 체크할 딕셔너리를 만든다 (visited)
# 5. nodes를 순회하면서 방문하지 않은 노드를 기준으로 dfs를 수행한다 (network)
# def solution(n, wires):
#     answer = n
#     nodes = set()
    
#     for wire in wires:
#         x, y = wire
#         nodes.add(x)
#         nodes.add(y)

#     for i in range(len(wires)):
#         graph = {}
#         visited = dict()
#         arr = wires[:i] + wires[i + 1:]

#         for node in nodes:
#             visited[node] = False

#         for a in arr:
#             x, y = a
#             if x in graph:
#                 graph[x].append(y)
#             else:
#                 graph[x] = [y]
#             if y in graph:
#                 graph[y].append(x)
#             else:
#                 graph[y] = [x]
        
#         network = []

#         for node in nodes:
#             if visited[node]:
#                 continue
#             if node not in graph:
#                 visited[node] = True
#                 network.append(1)
#             else:
#                 queue = [node]
#                 cnt = 0
#                 while queue:
#                     x = queue.pop()
#                     for y in graph[x]:
#                         if visited[y]:
#                             continue
#                         queue.append(y)
#                         visited[y] = True
#                         cnt += 1
#                         print(y, cnt)
#                 network.append(cnt)
#         print(network)
        
#         answer = min(answer, abs(network[0] - network[1]))

#     return answer

# 나의 풀이 개선
# 굳이 nodes를 쓰지 않고 set을 사용해보자
# def solution(n, wires):
#     answer = n

#     for i in range(len(wires)):
#         graph = {}
#         visited = dict()
#         divided = wires[:i] + wires[i + 1:]
#         nodes = set()

#         for d in divided:
#             x, y = d
#             nodes.add(x)
#             nodes.add(y)

#             if x in graph:
#                 graph[x].append(y)
#             else:
#                 graph[x] = [y]

#             if y in graph:
#                 graph[y].append(x)
#             else:
#                 graph[y] = [x]

#             if x not in visited:
#                 visited[x] = False
#             if y not in visited:
#                 visited[y] = False

#         network = []

#         for node in nodes:
#             if visited[node]:
#                 continue

#             queue = [node]
#             cnt = 0
#             while queue:
#                 x = queue.pop()
#                 for y in graph[x]:
#                     if visited[y]:
#                         continue
#                     queue.append(y)
#                     visited[y] = True
#                     cnt += 1
#             network.append(cnt)

#         if len(network) == 1:
#             answer = min(answer, network[0] - 1)
#         else:
#             answer = min(answer, abs(network[0] - network[1]))

#     return answer

# 다른 사람의 풀이 1
# def dfs(v, graph, visited):
#     visited[v] = True
#     return sum([1] + [dfs(u, graph, visited) for u in graph[v] if not visited[u]])

# def solution(n, wires):
#     graph = [[] for _ in range(n + 1)]
#     answer = n

#     for x, y in wires:
#         graph[x].append(y)
#         graph[y].append(x)

#     for i in range(n - 1):
#         visited = [False for _ in range(n + 1)]
#         x, y = wires[i]
#         print(x, y)
#         visited[y] = True
#         tmp = abs(dfs(x, graph, visited) - dfs(y, graph, visited))
#         answer = min(tmp, answer)

#     return answer

# union find?
uf = []

def find(a):
    global uf
    if uf[a] < 0: return a
    uf[a] = find(uf[a])
    return uf[a]

def merge(a, b):
    global uf
    pa = find(a)
    pb = find(b)
    if pa == pb:
        return
    uf[pa] += uf[pb]
    uf[pb] = pa

def solution(n, wires):
    global uf
    answer = n

    for i in range(n - 1):
        uf = [-1 for _ in range(n+1)]
        tmp = [wires[x] for x in range(n - 1) if x != i]
        
        for a, b in tmp:
            merge(a, b)
            
        v = [x for x in uf[1:] if x < 0]
        answer = min(answer, abs(v[0]-v[1]))

    return answer

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n, wires))