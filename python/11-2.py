class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code



삼성전자 = Stock("삼성전자", "005930")
print(삼성전자.name, 삼성전자.code)

a = Stock(None, None)
a.set_name("삼성전자")
a.set_code("005930")
print(a.name, a.code)

삼성 = Stock("삼성전자", "005930")
print(삼성.get_name(), 삼성.get_code())