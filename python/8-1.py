price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list[i])

for i in range(len(price_list)):
    print(i, price_list[i])

for i in range(len(price_list)):
    print(len(price_list)-i-1, price_list[i])

for i in range(1, len(price_list)):
    print(90+i*10, price_list[i])

my_list = ["가", "나", "다", "라"]
for i in range(len(my_list)-1):
    print(my_list[i], my_list[i+1])

my_list = ["가", "나", "다", "라", "마"]
for i in range(len(my_list)-2):
    print(my_list[i], my_list[i+1], my_list[i+2])

my_list = ["가", "나", "다", "라"]
length = len(my_list) - 1
for i in range(length):
    print(my_list[length - i], my_list[length-(i+1)])

my_list = [100, 200, 400, 800]

for i in range(len(my_list)-1):
    print(my_list[i+1]-my_list[i])

my_list = [100, 200, 400, 800, 1000, 1300]
sum = 0
avg = 0
for i in range(len(my_list)-2):
    sum = my_list[i] + my_list[i+1] + my_list[i+2]
    avg = sum / 3
    print(avg)

low_prices = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(low_prices)):
    volatility.append(high_prices[i] - low_prices[i])

apart = [["101호","102호"], ["201호","202호"], ["301호","302호"]]
print(type(apart))

stock = [["시가", 100, 200, 300], ["종가", 80, 210, 330]]

stock = {"시가":[100, 200, 300], "종가":[80, 210, 330]}

stock = {"10/10": [80, 110, 70, 90], "10/11": [210, 230, 190, 200]}
