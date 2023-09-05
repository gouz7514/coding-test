# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies
# easy
# 나의 풀이
def kidsWithCandies(candies, extraCandies):
  answer = [False] * len(candies)

  for i in range(len(candies)):
    if candies[i] + extraCandies >= max(candies):
      answer[i] = True

  return answer

# better mmemory
def kidsWithCandies(candies, extraCandies):
  answer = []

  for i in range(len(candies)):
    answer.append(candies[i] + extraCandies >= max(candies))

  return answer


candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))