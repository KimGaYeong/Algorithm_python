from sys import stdin

S = stdin.readline().strip()

alpha = [-1]*26
visit = [0]*26

for idx, s in enumerate(S):
    tmp = ord(s)-97
    if visit[tmp] ==0:
        alpha[ord(s)-97] = idx
        visit[ord(s)-97] = 1

for a in alpha:
    print(a, end =" ")