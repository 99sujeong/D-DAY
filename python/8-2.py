apart = [["101호","102호"], ["201호","202호"], ["301호","302호"]]
print(type(apart))

stock = [["시가", 100, 200, 300], ["종가", 80, 210, 330]]

stock = {"시가":[100, 200, 300], "종가":[80, 210, 330]}

stock = {"10/10": [80, 110, 70, 90], "10/11": [210, 230, 190, 200]}

apart = [[101, 102], [201, 202], [301, 302]]
for i in range(len(apart)):
    for j in range(len(apart[0])):
        print(apart[i][j], "호")

for i in range(len(apart)):
    for j in range(len(apart[0])):
        print(apart[(len(apart)-1)-i][j], "호")

for i in range(len(apart)):
    for j in range(len(apart[0])):
        print(apart[(len(apart)-1)-i][(len(apart[i])-1)-j], "호")

for i in range(len(apart)):
    for j in range(len(apart[0])):
        print(apart[i][j], "호")
        print("-----")

for i in range(len(apart)):
    for j in range(len(apart[0])):
        print(apart[i][j], "호")
    print("-----")

for i in range(len(apart)):
    for j in range(len(apart[0])):
        print(apart[i][j], "호")
print("-----")

data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

for i in range(len(data)):
    for j in range(len(data[0])):
        print(data[i][j]*1.00014)

for i in range(len(data)):
    for j in range(len(data[0])):
        print(data[i][j]*1.00014)
    print("----")

result = []
for i in range(len(data)):
    for j in range(len(data[0])):
        result.append(data[i][j]*1.00014)
print(result)

result = []
for i in range(len(data)):
    res = []
    for j in range(len(data[0])):
        res.append(data[i][j]*1.00014)
    result.append(res)
print(result)

ohlc = [["open", "high", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
