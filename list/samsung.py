class Samsung(object):
    def __init__(self, name, code, per, pbr, plus):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.plus = plus

    def get_name(self): # to_string
        return f'종목명 : {self.name}  종목코드 : {self.code}  per : {self.per}  pbr : {self.pbr}  배당수익률 {self.plus} \n'

    @staticmethod
    def del_element(ls, code):

        for i, j in enumerate(ls):
            if j.code == code:
                del ls[i]

    @staticmethod
    def main():
        ls = []

        while 1:
            choice = int(input('0 : 종료하기 \n1 : 입력하기 C\n2 : 출력하기 R\n3 : 삭제하기 D\n4 : 수정하기 U\n'))
            if choice == 0:
                print('종료하겟습니다.')
                break
            elif choice == 1:
                ls.append(Samsung(input(' 종목명: '), input('종목코드: '), input('per: '), input('pbr: '), input('배당수익률: ')))
            elif choice == 2:
                for i in ls:
                    print(i.get_name())
            elif choice == 3:
                stock = Samsung(input('삭제할 기업 : '),  input('삭제할 종목코드 : '), None, None, None)
                stock.del_element(ls, stock.code)

            elif choice == 4:
                code = input('수정할 종목의코드 : ')
                edit_info = Samsung(input('수정 기업명:'), None, None, None)
                edit_info.del_element(ls, code)
                ls.append(edit_info)

                print('수정되었습니다.')

            else:
                print('잘못입력하셧습니다.')
                continue


Samsung.main()
# None 부분 데이터로 출력이안됨
