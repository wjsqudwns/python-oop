class Cal :
    def __init__(self,first,second): # 생성자
        self.first = first
        self.second = second


    def add(self):
        return  c.first + c.second
    def sub(self):
        return  c.first - c.second
    def mul(self):
        return  c.first * c.second
    def div(self):
        return  c.first / c.second

if __name__ == '__main__':
    c = Cal(10, 1)
    print(c.add())
    print(c.sub())
    print(c.mul())
    print(c.div())