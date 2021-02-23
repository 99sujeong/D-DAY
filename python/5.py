my_variable = ()

movie_rank = ("닥터 스트레인지", "스플릿", "럭키")

num = (1)
print(type(num))

"""
t = (1, 2, 3)
t[0] = 'a'
"""

t = 1, 2, 3, 4
print(type(t))

t = ('a', 'b', 'c')
t = ('A', 'B', 'C')
print(t)

interest = ('삼성전자', 'LG전자', 'SK Hynix')
list_interest = list(interest)
print(list_interest)

interest = ['삼성전자', 'LG전자', 'SK Hynix']
tuple_interest = tuple(interest)
print(tuple_interest)

temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

even = tuple(range(2,100,2))
print(even)
