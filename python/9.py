def print_coin():
    print("비트코인")

print_coin()

for i in range(100):
    print_coin()

def print_coins():
    for i in range(100):
        print("비트코인")

def print_with_smile(str):
    print(str,":D")

print_with_smile("안녕하세요")

def print_upper_price(int):
    print(str*1.3)

def print_sum(a, b):
    print(a+b)

def print_arithmeitc_operation(a, b):
    print(a, "+", b, "=", a + b)
    print(a, "-", b, "=", a - b)
    print(a, "*", b, "=", a * b)
    print(a, "/", b, "=", a / b)

print_arithmeitc_operation(3, 4)


def print_max(a, b, c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)

def print_reverse(str):
    print(str[::-1])

print_reverse("python")

def print_score(list):
    sum = 0
    avg = 0
    for i in list:
        sum += i
    avg = sum / len(list)
    print(avg)

print_score([1, 2, 3])

def print_even(list):
    for i in list:
        if i % 2 == 0:
            print(i)

print_even([1, 3, 2, 10, 12, 11, 15])

def print_keys(dict):
    for i in dict:
        print(i)

print_keys({"이름":"김말똥", "나이":30, "성별":0})

my_dict = {"10/26":[100, 130, 100, 100],
            "10/27":[10, 12, 10, 11]}

def print_value_by_key(my_dict, key):
    print(my_dict[key])

print_value_by_key(my_dict, "10/26")

def print_5xn(string):
    print(string[:5])
    print(string[5:])

print_5xn("아이엠어보이유알어걸")

def print_mxn(string, num):
    n = int(len(string)/num)
    for i in range(n+1):
        print(string[i*num:i*num+num])

print_mxn("아이엠어보이유알어걸", 3)

def make_url(url):
    url = "www."+url+".com"
    return url

print(make_url("naver"))

def make_list(str):
    my_list = []
    for i in str:
        my_list.append(i)
    return my_list

print(make_list("abcd"))

def pickup_even(num_list):
    result = []
    for i in num_list:
        if i % 2 == 0:
            result.append(i)
    return result

print(pickup_even([3, 4, 5, 6, 7, 8]))

def convert_int(str):
    num = str.split(",")
    s = ""
    for i in num:
        s += i
    s = int(s)

convert_int("1,234,567")

def calc_monthly_salary(annual_salary):
    return int(annual_salary/12)

print(calc_monthly_salary(12000000))