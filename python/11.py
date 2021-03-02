class Human:
    """
    def __init__(self):
        print("응애응애")
    """
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        print("나의 죽음을 알리지 마라")

    def who(self):
        print("이름:", areum.name, " 나이:", areum.age, " 성별:", areum.sex)

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

#areum = Human()
areum = Human("모름", 0, "모름")

print("이름:", areum.name, " 나이:", areum.age, " 성별:", areum.sex)

areum.who()

areum.setInfo("아름", 25, "여자")

areum.who()

del areum