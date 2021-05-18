def add_funtion(first, second):

    return first + second
def sub_funtion(first, second):

    return first - second
def mul_funtion(first, second):

    return first * second
def div_funtion(first, second):

    return first / second
class Cal :

    def meta(self,first,second):
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
    c = Cal()
    print(add_funtion(10, 2))
    print(sub_funtion(10, 2))
    print(mul_funtion(10, 2))
    print(div_funtion(10, 2))

    '''c.meta(10, 1)
    print(c.add())
    print(c.sub())
    print(c.mul())
    print(c.div())'''
