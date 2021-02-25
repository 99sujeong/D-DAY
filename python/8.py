과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수)

for 변수 in 과일:
    print("#####")

print("A")
print("B")
print("C")

print("출력:", "A")
print("출력:", "B")
print("출력:", "C")

b = "A".lower()
print("변환:", "a")
b = "B".lower()
print("변환:", "b")
b = "C".lower()
print("변환:", "c")

for 변수 in [10,20,30]:
    print(변수)

for 변수 in [10, 20, 30]:
    print(변수)
    print("------")

print("++++")
for 변수 in [10, 20, 30]:
    print(변수)

for 변수 in range(4):
    print("-------")

리스트 = [100, 200, 300]
for i in 리스트:
    print(i+10)

리스트 = ["김밥", "라면", "튀김"]
for i in 리스트:
    print("오늘의 메뉴:", i)

리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for i in 리스트:
    print(len(i))

리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i, len(i))

for i in 리스트:
    print(i[0])

리스트 = [1, 2, 3]
for i in 리스트:
    print("3 x", i)

for i in 리스트:
    print("3 x", i, "=", i*3)

리스트 = ["가", "나", "다", "라"]
for i in 리스트:
    if i != "가":
        print(i)

for i in 리스트[::2]:
    print(i)

for i in 리스트[::-1]:
    print(i)

리스트 = [3, -20, -3, 44]
for i in 리스트:
    if i < 0:
        print(i)

리스트 = [3, 100, 23, 44]
for i in 리스트:
    if i % 3 == 0:
        print(i)

리스트 = [13, 21, 12, 14, 30, 18]
for i in 리스트:
    if i < 20 and i % 3 == 0:
        print(i)

리스트 = ["I", "study", "python", "language", "!"]
for i in 리스트:
    if len(i) >= 3:
        print(i)

리스트 = ["A", "b", "c", "D"]
for i in 리스트:
    if i.isupper():
        print(i)

for i in 리스트:
    if i.islower():
        print(i)

리스트 = ['dog', 'cat', 'parrot'] 

for i in 리스트:
    str = i[0]
    str = str.upper()
    i = str + i[1:]
    print(i)

리스트 = ['hello.py', 'ex01.py', 'intro.hwp'] 
for i in 리스트:
    str = i.split(".")
    print(str[0])

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
    if i[-2:] == ".h":
         print(i)

for i in 리스트:
    if i[-2:] == ".h" or i[-2:] == ".c":
        print(i)

for i in range(100):
    print(i)

for i in range(2002, 2051, 4):
    print(i)

for i in range(3, 31, 3):
    print(i)

for i in range(99, -1, -1):
    print(i)

for i in range(10):
    print(float(i)/10)

for i in range(1, 10):
    print("3 x",i,"=",3*i)

for i in range(1, 10, 2):
    print("3 x", i,"=", 3*i)

sum = 0
for i in range(1, 11):
    sum += i
print("합 :", sum)

sum = 0
for i in range(1, 11, 2):
    sum += i
print("합 :", sum)

mul = 1
for i in range(1, 11):
    mul *= i
print(mul)

