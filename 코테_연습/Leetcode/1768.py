# https://leetcode.com/problems/merge-strings-alternately
# easey
# 나의 풀이
def mergeAlternxately(word1, word2):
  result = ''

  for (x, y) in zip(word1, word2):
    result += (x + y)

  if len(word1) > len(word2):
    result += word1[len(word2):]
  else:
    result += word2[len(word1):]

  return result

word1 = "abcd"
word2 = "pq"

print(mergeAlternxately(word1, word2))