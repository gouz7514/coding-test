# 최소 힙
# https://www.acmicpc.net/problem/1927
# 실버 2
# 나의 풀이
# 최소 힙에 삽입할 때는 마지막 인덱스에 넣고 idx / 2 와 비교하며 자리 바꾼다
# 최소 힙에서 삭제할 때는 마지막 인덱스의 원소랑 바꾸고 루트를 자식과 비교하며 자리 바꿔 나간다
import sys
input = sys.stdin.readline

heap = [0]

for _ in range(int(input())):
  x = int(input())

  if x == 0:
    if len(heap) == 1:
      print(0)
    else:
      print(heap[1])
      # 마지막 인덱스 원소와 바꾸고 마지막 원소를 삭제
      temp = heap[1]
      heap[1] = heap[len(heap) - 1]
      heap.pop() # 마지막 원소 삭제

      idx = 1

      while idx * 2 < len(heap):
        left_child = idx * 2
        right_child = idx * 2 + 1
        min_child = left_child
        if right_child < len(heap) and heap[right_child] < heap[left_child]:
          min_child = right_child
        if heap[idx] <= heap[min_child]:
          break

        temp = heap[idx]
        heap[idx] = heap[min_child]
        heap[min_child] = temp
        idx = min_child

  else: # 자연수 들어온 경우 즉, 원소 삽입
    heap.append(x)
    idx = len(heap) - 1

    if idx > 1:
      while heap[idx // 2] > heap[idx]:
        temp = heap[idx]
        heap[idx] = heap[idx // 2]
        heap[idx // 2] = temp

        idx = idx // 2
