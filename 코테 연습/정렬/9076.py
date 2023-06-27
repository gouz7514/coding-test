# 점수 집계
# https://www.acmicpc.net/problem/9076
T = int(input())
for _ in range(T):
	lst = list(map(int, input().split(' ')))
	lst.sort()
	lst2 = lst[1:4]
	lst2.sort()
	if abs(lst2[0] - lst2[2]) >= 4:
		print('KIN')
	else:
		print(sum(lst2))