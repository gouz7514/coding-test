# 맞췄지만 개선이 많이 필요한 코드
def solution(n, wires):
    answer = n
    nodes = set()
    
    for wire in wires:
        x, y = wire
        nodes.add(x)
        nodes.add(y)

    for i in range(len(wires)):
        graph = {}
        visited = dict()
        arr = wires[:i] + wires[i + 1:]

        for node in nodes:
            visited[node] = False

        for a in arr:
            x, y = a
            if x in graph:
                graph[x].append(y)
            else:
                graph[x] = [y]
            if y in graph:
                graph[y].append(x)
            else:
                graph[y] = [x]
        
        network = []

        for node in nodes:
            if visited[node]:
                continue
            if node not in graph:
                visited[node] = True
                network.append(1)
            else:
                queue = [node]
                cnt = 0
                while queue:
                    x = queue.pop()
                    for y in graph[x]:
                        if visited[y]:
                            continue
                        queue.append(y)
                        visited[y] = True
                        cnt += 1
                        print(y, cnt)
                network.append(cnt)
        print(network)
        
        answer = min(answer, abs(network[0] - network[1]))

    return answer

n = 3
wires = [[1,2], [2,3]]
print(solution(n, wires))