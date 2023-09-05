# https://leetcode.com/problems/greatest-common-divisor-of-strings
# easy (not easy one...)
# 나의 풀이 - 문제 잘못 이해해서 오래 걸렸다
def gcdOfStrings(str1, str2):
  answer = ''
  word = str1

  # 최대공약수 찾기
  def getGcd(x, y):
    x, y = (x, y) if x > y else (y, x)
    r = x % y
    if r == 0:
        return y
    return getGcd(y, r)
  
  gcd = getGcd(len(str1), len(str2))

  if len(str1) > len(str2):
    word = str2
  elif len(str1) < len(str2):
    word = str1

  word = word[:gcd]

  while word:
    str1Divides = word * (len(str1) // len(word)) == str1
    str2Divides = word * (len(str2) // len(word)) == str2
    if str1Divides and str2Divides:
      answer = word
      break
    word = word[:-1]

  return answer

# 다른 사람의 풀이
# str1 + str2 == str2 + str1 인지 체크한다
# 앞에꺼를 잘라서 뒤에 붙여도 문제 없다면 그 순간 정답이다
def gcdOfStrings(str1, str2):
  if str1 + str2 != str2 + str1:
    return ''
  
  # 최대공약수 찾기
  def getGcd(x, y):
    x, y = (x, y) if x > y else (y, x)
    r = x % y
    if r == 0:
        return y
    return getGcd(y, r)
  
  gcd = getGcd(len(str1), len(str2))
  return str1[:gcd]
  
str1 = 'ABABCCABAB'
str2 = 'ABAB'

print('answer : ', gcdOfStrings(str1, str2))