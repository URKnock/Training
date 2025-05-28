
# 9063: 대지

N = int(input())

x = {"min": 10000, "max": -10000, "val": 0}
y = {"min": 10000, "max": -10000, "val": 0}

for i in range(N):
	data = input().split(" ")
	x["val"] = int(data[0])
	y["val"] = int(data[1])
	x["min"] = min(x["val"], x["min"])
	x["max"] = max(x["val"], x["max"])
	y["min"] = min(y["val"], y["min"])
	y["max"] = max(y["val"], y["max"])

if N < 2:
	result = 0
else:
	result = abs(x["max"] - x["min"]) * abs(y["max"] - y["min"])

print(result)