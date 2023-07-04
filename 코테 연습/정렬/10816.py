# 숫자 카드 2
# https://www.acmicpc.net/problem/10816
# 나의 풀이
# 시간 복잡도 : O(N log N + M log N)
# 이유 : cards 배열을 sort할 때 O(N log N), binary_search에서 O(M log N)
# import sys

# answer = []
# card_dict = dict()

# N = int(sys.stdin.readline())
# cards = list(map(int, sys.stdin.readline().strip().split()))
# cards.sort()

# M = int(sys.stdin.readline())
# nums = list(map(int, sys.stdin.readline().strip().split()))

# for card in cards:
#   if card in card_dict:
#     card_dict[card] += 1
#   else:
#     card_dict[card] = 1

# def binary_search(arr, target):
#   first, last = 0, len(arr) - 1

#   while first <= last:
#     mid = (first + last) // 2

#     if arr[mid] == target:
#       return 1
#     elif arr[mid] < target:
#       first = mid + 1
#     else:
#       last = mid - 1

#   return 0

# for n in nums:
#   result = binary_search(cards, n)
#   if result == 1:
#     answer.append(card_dict[n])
#   else:
#     answer.append(0)

# print(*answer)

# 다른 사람의 풀이
# 시간 복잡도 : O(N + M)
import sys

card_dict = dict()

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().strip().split()))

M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))

for card in cards:
  card_dict[card] = card_dict[card] + 1 if card in card_dict else 1

for n in nums:
  print(card_dict[n] if n in card_dict else 0, end = ' ')