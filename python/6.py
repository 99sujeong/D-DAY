temp = {}
print(type(temp))

icecream = {"메로나":1000, "폴라포":1200, "빵빠레":1800}
print(icecream)

icecream["죠스바"] = 1200
icecream["월드콘"] = 1500
print(icecream)

ice = { '메로나':1000,
        '폴라포':1200,
        '빵빠레':1800,
        '죠스바':1200,
        '월드콘':1500 }

print("메로나 가격:", ice['메로나'])

ice['메로나'] = 1300
print(ice)

del ice['메로나']
print(ice)

inventory = { '메로나': [300, 20],
              '비비빅': [400, 3],
              '죠스바': [250, 100] }
print(inventory)

print(inventory['메로나'][0], "원")

print(inventory['메로나'][1], "개")

inventory['월드콘'] = [500, 7]
print(inventory)

icecream = {'탱크보이':1200, '폴라포':1200, '빵빠레':1800, '월드콘':1500, '메로나':1000}
ice_keys = list(icecream.keys())
print(ice_keys)

ice_values = list(icecream.values())
print(ice_values)

sum = 0
for i in range(len(ice_values)):
    sum += ice_values[i]
print(sum)

new_product = {'팥빙수' : 2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)
