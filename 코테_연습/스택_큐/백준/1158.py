# 요세푸스 문제
# 실버 4
# https://www.acmicpc.net/problem/1158
# 나의 풀이 - ㅠㅠ
# N, K = map(int, input().split(' '))
# arr = [i for i in range(1, N + 1)] * N
# answer = []

# cnt = 1

# for i in range(len(arr)):
#     if arr[i] in answer:
#         continue
#     if cnt < K:
#         cnt += 1
#     elif cnt == K:
#         answer.append(arr[i])
#         cnt = 1

# print('<' + ', '.join(str(x) for x in answer) + '>')

# 다른 사람의 풀이
N,K = map(int,input().split())
arr = [i for i in range(1,N+1)]    # 맨 처음에 원에 앉아있는 사람들

answer = []   # 제거된 사람들을 넣을 배열
num = 0  # 제거될 사람의 인덱스 번호

for t in range(N):
    num += K-1
    print('t, num : ', t, num)
    if num >= len(arr):   # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈  
        num = num%len(arr)

    answer.append(str(arr.pop(num)))
    # print(arr)
print("<",", ".join(answer)[:],">", sep='')