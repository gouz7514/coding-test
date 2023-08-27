# # 나의 풀이 - 정답!
# # dfs로 해결해야 할듯
# def solution(maps):
#     answer = []
#     visited = [[False] * len(maps[0]) for _ in range(len(maps))]

#     def dfs(x, y, result):
#         if visited[x][y]:
#             return
#         visited[x][y] = True
#         # X면 return
#         if result[0] == 'X':
#             return
#         queue = []
#         queue.append([x, y])

#         while len(queue):
#             x, y = queue.pop()
#             dx = [-1, 1, 0, 0]
#             dy = [0, 0, -1, 1]
            
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]

#                 # 배열 범위 벗어나면 return
#                 if (nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0])):
#                     continue
#                 if (maps[nx][ny] == 'X' or visited[nx][ny]):
#                     continue
                
#                 result.append(maps[nx][ny])
#                 visited[nx][ny] = True
#                 queue.append([nx, ny])

#         return result
    
#     for i in range(len(maps)):
#         for j in range(len(maps[0])):
#             result = dfs(i, j, [maps[i][j]])
#             if result is not None:
#                 answer.append(sum(list(map(int, result))))

#     answer.sort()
#     return answer if len(answer) else [-1]

# maps = ["X591X","X1X5X","X231X", "1XXX1"]
# print(solution(maps))

# 다른 사람의 풀이
def solution(maps):
    graph = [list(row) for row in maps]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    answer = []

    def dfs(x, y):
        cnt = 0
        if x < 0 or x >= len(graph) or y < 0 or y >= len(graph[0]):
            return cnt
        if not graph[x][y].isdigit():
            return cnt
        cnt = int(graph[x][y])
        graph[x][y] = 'X'
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            cnt += dfs(nx, ny)
        return cnt
    
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j].isdigit():
                answer.append(dfs(i, j))


    return sorted(answer) if len(answer) else [-1]

maps = ["X591X","X1X5X","X231X", "1XXX1"]
print(solution(maps))