movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

movie_rank.append("배트맨")
print(movie_rank)

movie_rank.insert(1,"슈퍼맨")
print(movie_rank)

del movie_rank[3]
print(movie_rank)

del movie_rank[2]
del movie_rank[2]
print(movie_rank)

lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

nums = [1, 2, 3, 4, 5, 6, 7]
print("max: ", max(nums))
print("min: ", min(nums))

nums = [1, 2, 3, 4, 5]
sum = 0
for i in range(len(nums)):
    sum += nums[i]
print(sum)

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면"," 팥빙수", "김치전"]
print(len(cook))

nums = [1, 2, 3, 4, 5]
sum = 0
for i in range(len(nums)):
    sum += nums[i]
print(sum/len(nums))

price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

print(nums[1::2])

nums = [1, 2, 3, 4, 5]
print(nums[::-1])

interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))

print("/".join(interest))

print("\n".join(interest))

string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)

data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

