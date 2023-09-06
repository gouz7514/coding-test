# 일곱 난쟁이
# https://www.acmicpc.net/problem/2309
# 브론즈 1
# 나의 풀이
# 일곱 난쟁이의 키 합이 100이다
# 출력 양식을 잘 확인하자..
nums = []
answer = []

for _ in range(9):
  nums.append(int(input()))

def solve(idx, arr, cnt):
  global answer
  if cnt == 7:
    if sum(arr) == 100:
      answer = list(arr)
    return
  
  for i in range(idx + 1, 9):
    arr.append(nums[i])
    solve(i, arr, cnt + 1)
    arr.remove(nums[i])

solve(-1, [], 0)

for i in sorted(answer):
  print(i)

# 다른 사람의 풀이
# 7개를 고르는 게 아니라 제외할 2개를 골라도 된다
nums = []
for _ in range(9):
  nums.append(int(input()))

for i in range(9):
  for j in range(1, 9):
    if sum(nums) - (nums[i] + nums[j]) == 100:
      x, y = nums[i], nums[j]
      break

nums.remove(x)
nums.remove(y)

for num in sorted(nums):
  print(num)