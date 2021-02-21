phone_number = "010-1111-2222"
str = ""
for i in range(0, len(phone_number)):
    if(phone_number[i] != "-"):
        str += phone_number[i]
    else:
        str += " "
print(str)

str2 = ""
for i in range(0, len(phone_number)):
    if(phone_number[i] != "-"):
        str2 += phone_number[i]
print(str2)

url = "http://sharebook.kr"
url2 = url.split(".")
print(url2[-1])

"""
lang = 'python'
lang[0] = 'P'
print(lang)
"""

string = 'abcdfe2a354a32a'
print(string.replace('a', 'A'))

string = "abcd"
print(string.replace('b', 'B'))

a = "3"
b = "4"
print(a+b)

print("Hi" * 3)

print('-' * 80)

t1 = 'python'
t2 = 'java'
t = t1 + ' ' + t2 + ' '
print(t * 3)

name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13

print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

print("이름: {} 나이: {}" .format(name1, age1))
print("이름: {} 나이: {}" .format(name2, age2))

상장주식수 = "5,969,782,550"
str = 상장주식수.split(",")
for i in range(len(str)):
    int(str[i])

분기 = "2020/03(E) (IFRS연결)"
print(분기[0:7])

data = "     삼성전자     "
print(data.strip())

ticker = "btc_krw"
upper_ticker = ticker.upper()
print(upper_ticker)

ticker = "BTC_KRW"
lower_ticker = ticker.lower()
print(lower_ticker)

a = 'hello'
a = a.capitalize()
print(a)

file_name = "보고서.xlsx"
file_name.endswith("xlsx")

file_name.endswith(("xlsx", "xlsx"))
file_name.endswith(("xlsx", "xls"))
print(file_name.endswith(("xlsx", "xlsx")))

file_name = "2020_보고서.xlsx"
file_name.startswith("2020")
print(file_name.startswith("2020"))

a = "hello world"
a.split(" ")

ticker = "btc_krw"
ticker.split("_")

date = "2020-05-01"
date.split("-")

data = "039490        "
data = data.rstrip()
print(data)
