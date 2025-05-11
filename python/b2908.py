
# 2908: 상수

S = input()
S = S.split(" ")

A = S[0][::-1]
B = S[1][::-1]

if A > B:
	print(A)
else:
	print(B)