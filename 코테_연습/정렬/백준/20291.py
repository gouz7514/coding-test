# 파일 정리
# https://www.acmicpc.net/problem/20291
import sys

files = dict()
N = int(sys.stdin.readline().strip())

for _ in range(N):
  name, extension = sys.stdin.readline().strip().split('.')

  if extension in files:
    files[extension] += 1
  else:
    files[extension] = 1

for file in sorted(files.items()):
  print(file[0], file[1])