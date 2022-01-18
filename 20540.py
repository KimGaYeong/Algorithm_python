from sys import stdin

Mbti = stdin.readline()
A = ['E', 'S', 'F', 'J']
B = ['I', 'N', 'T', 'P']

for index, char in enumerate(Mbti):
    if char in A:
        print(B[index], end="")
    if char in B:
        print(A[index], end="")


