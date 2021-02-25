print(3 == 5)

print(3 < 5)

x = 4
print(1 < x < 5)

print((3 == 3) and (4 != 3))

#print(3 => 4)

if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")

if True:
    print("1")
    print("2")
else:
    print("3")
print("4")

if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")

user_input = input()
print(user_input*2)

user_input = input("숫자를 입력하세요 : ")
print(int(user_input)+10)

user_input = input()
if(int(user_input) % 2 == 1):
    print("홀수")
else:
    print("짝수")

user_input = input("입력값: ")
num = int(user_input) + 20
if num > 255:
    print(255)
else:
    print(num)

user_input = input("입력값: ")
num = int(user_input) - 20
if num < 0:
    print(0)
else:
    if num > 255:
        print(255)
    else: 
        print(num)

user_input = input("현재시간:")
time = user_input.split(":")
if time[1] == "00":
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")

fruit = ["사과", "포도", "홍시"]
user_input = input("좋아하는 과일은? ")
if user_input in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")

warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
user_input = input()
if user_input in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")

fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
user_input = input("제가 좋아하는 계절은 : ")
if user_input in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")

fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
user_input = input("좋아하는 과일은? ")
if user_input in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")

user_input = input()
if user_input.islower():
    print(user_input.upper())
else:
    print(user_input.lower())

score = int(input("score : "))
if 80 < score <= 100:
    print("grade is A")
elif 60 < score <= 80:
    print("grade is B")
elif 40 < score <= 60:
    print("grade is C")
elif 20 < score <= 40:
    print("grade is D")
else:
    print("grade is E")

money = input("입력:")
m = money.split()
if m[1] == "달러":
    print(float(m[0])*1167, "원")
elif m[1] == "엔":
    print(float(m[0])*1.096, "원")
elif m[1] == "유로":
    print(float(m[0])*1268, "원")
elif m[1] == "위안":
    print(float(m[0])*171, "원")
####
환율 = {"달러": 1167, 
        "엔": 1.096, 
        "유로": 1268, 
        "위안": 171}
user = input("입력: ")
num, currency = user.split()
print(float(num) * 환율[currency], "원")
####
num1 = int(input("input number1 : "))
num2 = int(input("input number2 : "))
num3 = int(input("input number3 : "))
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 >num3:
    print(num2)
else:
    print(num3)

phone = input("휴대전화 번호 입력: ")
if phone[0:3] == "011":
    print("당신은 SKT 사용자입니다.")
elif phone[0:3] == "016":
    print("당신은 KT 사용자입니다.")
elif phone[0:3] == "019":
    print("당신은 LGU 사용자입니다.")
else:
    print("당신은 알 수 없습니다.")

num = input("우편번호 : ")
if num[:3] in ["010", "011", "012"]:
    print("강북구")
elif num[:3] in ["013", "014", "015"]:
    print("도봉구")
else:
    print("노원구")

num = input("주민등록번호: ")
num2 = num.split("-")[1]
print(num2)
if(num2[0] == "1" or num2[0] == "3":
    print("남자")
else:
    print("여자")

num = input("주민등록번호: ")
num2 = num.split("-")[1]
if num2[1:3] in ["00", "01", "02", "03", "04", "05", "06","07", "08"]:
    print("서울 입니다.")
elif num2[1:3] in ["09", "10", "11", "12"]:
    print("부산 입니다.")
else:
    print("서울이 아닙니다.")

num = input("주민등록번호: ")
first = (int(num[0])*2+int(num[1])*3+int(num[2])*4+int(num[3])*5+
        int(num[4])*6+int(num[5])*7+int(num[7])*8+int(num[8])*9+
        int(num[9])*2+int(num[10])*3+int(num[11])*4+int(num[12])*5)%11
second = 11 - first
if(second == int(num[13])):
    print("유효한 주민등록입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")

import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

시가 = float(btc['opening_price'])
변동폭 = float(btc['max_price'] - btc['min_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")

