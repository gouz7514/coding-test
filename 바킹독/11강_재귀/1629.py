# 곱셈
# https://www.acmicpc.net/problem/1629
# 실버 1
# 1승을 계산할 수 있다
# k승을 계산했으면 2k승과 2k + 1 승도 O(1)에 계산할 수 있다
# 시간복잡도는 O(logB) 이다. B가 절반씩 깎이기 때문
A, B, C = list(map(int, input().split()))

def pow(a,b,c):
  if b == 1:
    return a % c
  result = pow(a, b // 2, c)
  result = result * result % c
  if b % 2 == 0:
    return result
  return result * a % c
print(pow(A, B, C))