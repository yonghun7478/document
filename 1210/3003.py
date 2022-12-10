#https://www.acmicpc.net/problem/3003

# A_TOTAL = 1
# B_TOTAL = 1
# C_TOTAL = 2
# D_TOTAL = 2
# E_TOTAL = 2
# F_TOTAL = 8

# A,B,C,D,E,F = map(int, input().split())

# print(str(A_TOTAL - A) + " ")
# print(str(B_TOTAL - B) + " ")
# print(str(C_TOTAL - C) + " ")
# print(str(D_TOTAL - D) + " ")
# print(str(E_TOTAL - E) + " ")
# print(str(F_TOTAL - F))

chess = [1,1,2,2,2,8]

a = list(map(int, input().split()))

for i in range(6):
    print(chess[i] - a[i], end=' ')