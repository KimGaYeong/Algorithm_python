"""
3
26 40 83
49 60 57
13 89 99
"""

# 아무리 봐도 DP문제!
from sys import stdin

N = int(input())
arr = []*3

for i in range(N):
    tmp = list(map(int, stdin.readline().split()))
    arr.append(tmp)

for i in range(1, N):
    arr[i][0] = min(arr[i - 1][1], arr[i - 1][2]) + arr[i][0]
    arr[i][1] = min(arr[i - 1][0], arr[i - 1][2]) + arr[i][1]
    arr[i][2] = min(arr[i - 1][0], arr[i - 1][1]) + arr[i][2]

print(min(arr[N-1]))