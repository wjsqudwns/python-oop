class Stock(object):

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def to_string(self):
        return f'종목명 {self.name} 종목코드 {self.code}'

    @staticmethod
    def del_element(ls, code):
        for i, j in enumerate(ls):
            if j.code == code:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.Exit 1.Create 2.Read 3.Update 4.Delete')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Stock(input('name'), input('code')))
            elif menu == '2':
                for i in ls:
                    print(i.to_string())
            elif menu == '3':
                code = input('종목코드')
                stock = Stock(input('수정할 이름'), code)
                stock.del_element(ls, code)
                ls.append(stock)

            elif menu == '4':
                stock = Stock(None,input('종목코드'))
                stock.del_element(ls,stock.code)
            else :
                print('Wrong Number')
                continue

Stock.main()