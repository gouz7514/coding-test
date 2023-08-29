# 주어진 문자열과 길이에 대해 나올 수 있는 모든 조합
words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
length = 4

def dfs(words, length, arr, result):
    if len(arr) == length:
        result.append(arr)
        return
    
    for i in range(len(words)):
        dfs(words[i + 1:], length, arr + words[i], result)

result = []
dfs(words, length, '', result)
print(result)
